#PLOUVIN Patrice
#Le jeu du pendu
#25/10/17




#Exercice 1 :

from random import randint
from string import ascii_letters
ALPHABET=ascii_letters
def choisis_mot(liste):
    '''la fonction permet de choisir un mot entre plusieurs
        argument : liste --- une liste de chaînes de caractères 
        retourne : str --- une chaîne aléatoirement choisie dans la liste'''
    pos = randint(0,len(liste)-1)
    return liste[pos]






#Exercice 2 :

def input_lettre(lettres_entrees):
    '''La fonction reçoit une chaîne de caractères
       argument : lettres_entrees --- str
       retourne : une lettre --- str'''
    terminer = False
    while not terminer:
        x = input("Entrez une lettre : ")
        if len(x)!=1 :
            print("Entrez une seule lettre, s'il vous plait")
        elif x in  lettres_entrees:
            print("Vous avez déjà entré cette lettre")
        elif x not in  ALPHABET:            
            print("Ceci n'est pas une lettre")
        else:
            terminer = True         
    return x
        





#Exercice 3 :

FIGURES_PENDU = ['''
   +---+
   |   |
       |
       |
       |
       |
==========''','''
   +---+
   |   |
   O   |
       |
       |
       |
==========''','''
   +---+
   |   |
   O   |
   |   |
       |
       |
==========''','''
   +---+
   |   |
   O   |
  /|   |
       |
       |
==========''','''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
==========''','''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
==========''','''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
==========''']

# 3.1

def dessine_pendu(n):
    '''La fonction affiche un dessin du pendu
       argument : n --- position dans la liste
       retour : affiche la figure du pendu a la n-eme place'''
    print(FIGURES_PENDU[n])
    
# 3.2

def affiche_erreurs(chaine):
    '''la fonction affiche les erreurs du joueur
       argument : chaine d'erreur --- str
       retour : affiche la chaine'''
    v = ' '
    for i in range(len(chaine)):
        v = v + chaine[i]+ ' '
    print("Erreurs :", v)

# 3.3

def affiche_correctes(correctes, mot_secret):
    '''la fonction affiche les bonnes reponses du joueur
       argument : reponse correctes --- str
                  mot_secret ---str
       retour : affiche les lettres correctes du joueur'''
    for i in mot_secret:
        if i in correctes:
            print(i, end=' ')
        else :
            print('_',end=' ')

#Exercice 4 :
            
def main():
    mot_secret=choisis_mot(['dysharmonique', 'hypogastrique', 'phénocristaux','pythagoriques'])
    incorrectes=''
    correctes=''
    fin=False
    n=-1
    while not fin :
        lettres = input_lettre(incorrectes+correctes)
        if lettres in mot_secret:
            correctes = correctes + lettres
            affiche_correctes(correctes, mot_secret)
            print()
            if len(correctes)==len(mot_secret):
                print("vous avez gagné")
                fin=True
        else:
            incorrectes = incorrectes + lettres
            n+=1
            if n==len(FIGURES_PENDU)-1:
                dessine_pendu(n)
                print("vous avez perdu")
                print("Le mot était : ", mot_secret)
                fin = True
            else :
                dessine_pendu(n)
                affiche_correctes(correctes, mot_secret)
                print()
                affiche_erreurs(incorrectes)
        print()


    
        




















            
