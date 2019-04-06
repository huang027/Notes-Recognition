Dictionnaire_Notes = {"do":[32,65,131,261,523,1046,2093,4186,8372,16744],
	"do#":[35,69,138,277,554,1109,2217,4435,8870,17740],
	"re":[37,73,147,294,587,1175,2349,4978,9396,18792],
	"re#":[39,78,156,311,622,1244,2489,4978,9956,19912],
	"mi":[41,82,165,330,659,1318,2637,5274,10548,21098],
	"fa":[44,87,175,349,698,1397,2794,5588,11176],
	"fa#":[46,93,185,370,740,1480,2960,5920,11840],
	"sol":[49,98,196,392,784,1568,3316,6272,12544],
	"sol#":[52,104,208,416,831,1661,3322,6645,13290],
	"la":[55,110,220,440,880,1760,3520,7040,14080],
	"la#":[58,117,233,466,932,1865,3729,7458,14918],
	"si":[62,124,247,494,988,1975,3951,7902,15804]}


def FreqToNote(f,erreur):
	""" Retourne la note d'une fréquence """
	for cle,valeur in Dictionnaire_Notes.items(): # Parcours du dictionnaire
		for note in valeur: # Parcours de la liste des fréquences de la note active
			if (note <= f+erreur and note >= f-erreur): # x{+-e} = a <=> x € [a-e ; a+e]
				return cle
	return "NaN" # impossible de trouver une note

def TabFreqToTabNote(tf,erreur):
	""" Retourne la liste des notes correspondant à la liste des fréquences TF """
	tn = []
	for f in tf: # Parcours du dictionnaire
		tn.append(FreqToNote(f,erreur))
	return tn
