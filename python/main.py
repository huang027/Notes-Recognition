from analyse_demo import *
from dico import *
from tkinter import *
from tkinter import filedialog

#-----------------------------------------
# CLASSES ET FONCTIONS
#-----------------------------------------
class Fichier:
    def __init__(self,nom):
        self.nom = str(nom).split('/')[-1:][0] # Suppression de l'arborescence
    def __repr__(self):
        return self.nom
def ouvrir():
	""" Ouverture du fichier """
	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Sélectionner un fichier audio",filetypes = (("Fichiers audio","*.wav"),("all files","*.*")))
	if root.filename != "" and root.filename[-3:]=="wav": # vérification du fichier (nom et extension)
		L_fichier_nom["text"] = "Le fichier est : "+str(Fichier(root.filename))
		print(Fichier(root.filename))
		choix.pack()
def detectNotes():
	""" Lancement de l'analyse """
	global resultAnalyse
	L_statut["text"] = "Traitement en cours..."
	resultAnalyse = Analyse(str(root.filename))
	L_statut["text"] = "Traitement terminé !"
	watch.pack(anchor="center")
def afficher():
	""" Résultat après l'analyse """
	global resultAnalyse
	toplevel = Toplevel()
	toplevel.geometry('500x100')
	L_aff_txt = Label(toplevel,text="")
	L_aff_txt["text"]="Les notes détectées sont :"
	L_aff_txt.pack()
	Label(toplevel,text=str(resultAnalyse[1])).pack()

#-----------------------------------------
# INTERFACE
#-----------------------------------------
root = Tk()
root.minsize(width=860, height=350)
root.maxsize(width=860, height=350)
root.wm_title("- Projet 2018 INSA 1A -")
root.filename=""

# Titres
Label(root,text="Projet réalisé par : Robin BARDON, Louis MONNIER, Edwin ROUCH, Raphaël SFEIR").pack(side=TOP,fill=X,anchor='center')
Label(root,text="Bienvenue dans l'interface de notre projet. Sélectionnez le fichier audio que vous souhaitez analyser (.wav)").pack(side=TOP,fill=X,anchor='center')

# Menu
Button(root,text="Ouvrir un fichier audio", command=ouvrir).pack()
L_fichier_nom = Label(root,text="")
L_fichier_nom.pack()

choix = Frame(root)
Button(choix, text='Détecter les notes',command=detectNotes).pack(side=LEFT)

L_statut = Label(root,text="")
L_statut.pack()
watch=Button(root,text='Afficher le résultat',command=afficher)
root.mainloop()
