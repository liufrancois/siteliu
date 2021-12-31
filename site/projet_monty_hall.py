from random import randint

def MH():
    liste= ["chevre", "chevre", "chevre"]
    liste[randint(0,2)]= "voiture" #liste pour dire definir ou est la voiture aleatoirement
    apparence = ["porte", "porte", "porte"] #apparence : liste qu on va affichier au fur et a mesure qu on ouvre des portes
    choix = randint(0,2)
    for i in range (3):
        if liste [i] == "chevre" and i != choix and " " not in liste: #rentre dans la liste si deriere la porte il y a 1 chevre, si ce n est pas la porte de l utilisateur et si on n est pas encore rentrer dans le if
            liste[i] = " " #modifie pour eviter de rerentrer dans la liste
            apparence[i] = "chevre" #modifie l apparence
    print(apparence) #affiche apparence
    #print("voulez vous changer de porte? (oui/non)")
    #rep = input()
    #rep = "non"
    if liste[choix] == "voiture":
        #print("gagné")
        return 1
    else:
        #print("perdu")
        return 0


score_gagné = 0
score_perdu = 0 #initialise les scores
for i in range(1000): #ajoute 1 point a score_gagné si on trouve la voiture sinon +1 a score_perdu
    if MH() == 1:
        score_gagné +=1
    else:
        score_perdu +=1
print("sur 1000 essais on a gagné ",score_gagné," et perdu ",score_perdu,)



def MH2():
    liste= ["chevre", "chevre", "chevre"]
    liste[randint(0,2)]= "voiture" #liste pour dire definir ou est la voiture aleatoirement
    apparence = ["porte", "porte", "porte"] #apparence : liste qu on va affichier au fur et a mesure qu on ouvre des portes
    choix = randint(0,2)
    for i in range (3):
        if liste[i] == "chevre" and i != choix and " " not in liste: #rentre dans la liste si deriere la porte il y a 1 chevre, si ce n est pas la porte de l utilisateur et si on n est pas encore rentrer dans le if
            liste[i] = " " #modifie pour eviter de rerentrer dans la liste
            apparence[i] = "chevre" #modifie l apparence
    print(apparence)#affiche apparence
    #print("voulez vous changer de porte? (oui/non)")
    #rep = int(input())
    #rep = "non"
    for i in range (3): #boucle qui va changer de porte de l utilisateur pour l autre porte as encore ouverte
        if apparence[i] == "porte" and i != choix:
            nchoix = i
    choix= nchoix

    if liste[choix] == "voiture":
        #print("gagné")
        return 1
    else:
        #print("perdu")
        return 0




score_gagné = 0
score_perdu = 0 #initialise les scores
for i in range(1000): #ajoute 1 point a score_gagné si on trouve la voiture sinon +1 a score_perdu
    if MH2() == 1:
        score_gagné +=1
    else:
        score_perdu +=1
print("sur 1000 essais on a gagné ",score_gagné," et perdu ",score_perdu,)
