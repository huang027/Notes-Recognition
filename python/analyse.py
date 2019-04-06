import math
import numpy as np
import scipy.io.wavfile as wave
from numpy.fft import fft
import dico as dico

def Fondamental(data,rate,debut,duree):
	"""Déterminer le fondamental du signal DATA entre une durée [DEBUT:DEBUT+DUREE]"""
	# Initialisation de la zone d'analyse
	start = int(debut*rate)
	stop = int((debut+duree)*rate)
	# Fenêtrage de la zone d'analyse
	fen = np.hanning(data[start:stop].size)*data[start:stop]
	# Spectre fréquentiel
	spectre = np.absolute(fft(fen))
	spectre = spectre/spectre.max() # Max = 1
	# Lecture graphique du spectre
	n = spectre.size
	freq = np.zeros(n)
	for k in range(n):
		freq[k] = 1.0/n*rate*k
	indFond = spectre[0:n//2].argmax() # Indice du fondamental dans la liste fft
	if indFond != len(data)-1: # Fondamental n'est pas le dernier élément de la liste => présence d'harmoniques
		# Interpolation quadratique autour du fondamental, max = -b/2a
	    y0,y1,y2 = spectre[indFond-1],spectre[indFond],spectre[indFond+1]
	    xmax = (y2-y0)/(2*(2*y1 - y2 - y0))
	    result = (indFond+xmax)
	else: # Pas d'harmonique, on a le fondammental
	    result = indFond
	return result # result = [[fréquences],[notes]]

def Spider(l,f,err):
	""" Vérifier la présence de f dans l à err près """
	if len(l)!=0:
		if f>=l[-1]-err and f<=l[-1]+err: # x{+-e} = a <=> x € [a-e ; a+e]
			return 1
		else:
			return 0
	else: #l est vide
		return 0

def Analyse(nom,dT=0.1,T_ANAL=0.5,ERR_SONORE=2e-2,ERR_FREQ=2):
	"""
		Analyse du fichier WAVE.
		dT -> déplacement de la fenêtre, précision de l'étude,  def : 0.1
		T_ANAL -> largeur de la fenêtre étudiée, def : 0.5
		ERR_SONOR -> erreur sur le signal sonore (détection du bruit), def : 2e-2
		ERR_FREQ -> erreur sur la fréquence (en Hz), def : 4
	"""
	frequences=[]
	# récupération du signal
	rate,data = wave.read(nom)
	# Traitement stéréo => conversion en mono
	if data[1].size == 2:
	    data = data[:,0]

	n = data.size # Taille de l'échantillon
	duree = 1.0*n/rate # Durée

	# Traitement du "vide sonore", commence lorsque l'amplitude du signal > ERR_SONORE
	i=0
	data=data/data.max() # MAX = 1
	while data[i] <= ERR_SONORE : # Amplitude sonore <= ERR_SONORE
	    i=i+1 # data[i] est du bruit : on passe
	d = 1.0*i/rate # début = index de signal / fe -> flottant

	# Détection des notes
	while d+T_ANAL<duree: # Parcours du signal
		f=Fondamental(data,rate,d,T_ANAL) # Récupération du fondamental dans la fenêtre d'étude
		d+=dT # Déplacement de la fenêtre d'étude
		if Spider(frequences,f,ERR_FREQ)==1 or f<20 or f>20000: # Fréquence détectée auparavant OU fréquence inaudible
			continue
		else:
			frequences.append(f)
	result=[frequences,dico.TabFreqToTabNote(frequences,ERR_FREQ)]

	return result
