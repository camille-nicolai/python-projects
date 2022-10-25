
tempo=0

# fonction qui affiche la grille de jeux
def affichage():
    # affiche le terrainbcolors.WIN +
    print("\n   [1][2][3]       <    Colonne")
    print("[1]", ligne1[0], ligne1[1], ligne1[2])
    print("[2]", ligne2[0], ligne2[1], ligne2[2])
    print("[3]", ligne3[0], ligne3[1], ligne3[2])
    print("\n^")
    print("ligne")
# Fonction qui dit qui joue
def tempocontrol(tempo):
    if tempo == 0:
        tempo=1
    elif tempo==1:
        tempo=0
    return tempo

# fonction de déroulement d'un tour
def tour(tempo):
    global token, joueur

    # selon valeur de tempo, c'est le tour du joueur 1 ou 2
    if tempo == 0 :
        joueur = joueur1
    elif tempo == 1:
        joueur = joueur2

    # annonce qui doit jouer
    print("\ntour de ",joueur,"\n")

    # selon le joueur leur token sera soit la croix, soit le rond
    if joueur == joueur1:
        token = "X "
    elif joueur == joueur2:
        token = "O "
    # demande la ligne et la colone sur laquelle entrer le token
    colone = int(input("colone : ")) - 1 # moins 1 pour alligner les coordonée x et y sur la grille  (sinon X =0 ,1 ,2  et  y = 1, 2 et 3)
    ligne = int(input("ligne : "))

    if colone <= 2:
        # Logique de positionnement sur la grille
        if ligne == 1:
            if ligne1[colone] == "_ ":
                ligne1[colone] = token
                tempo = tempocontrol(tempo)
            else:
                print("case déja posé")

        elif ligne == 2:
            if ligne2[colone] == "_ ":
                ligne2[colone] = token
                tempo=tempocontrol(tempo)
            else:
                print("case déja posé")
        elif ligne == 3:
            if ligne3[colone] == "_ ":
                ligne3[colone] = token
                tempo = tempocontrol(tempo)
            else:
                print("case déja posé")

        else:
            print("pas la bonne ligne")
    else:
        print("pas la bonne colonne")

    return tempo,joueur

#Fonction de condition de victoire
def gagné():
    if (ligne1[0] == ligne1[1]) and (ligne1[1] == ligne1[2]) and (ligne1[0] != "_ "):
        return 1
    if (ligne2[0] == ligne2[1]) and (ligne2[1] == ligne2[2]) and (ligne2[0] != "_ "):
        return 1
    if (ligne3[0] == ligne3[1]) and (ligne3[1] == ligne3[2]) and (ligne3[0] != "_ "):
        return 1
    if (ligne1[0] == ligne2[1]) and (ligne2[1] == ligne3[2]) and (ligne1[0] != "_ "):
        return 1
    if (ligne3[0] == ligne2[1]) and (ligne2[1] == ligne1[2]) and (ligne1[2] != "_ "):
        return 1
    if (ligne1[0] == ligne2[0]) and (ligne2[0] == ligne3[0]) and (ligne3[0] != "_ "):
        return 1
    if (ligne1[1] == ligne2[1]) and (ligne2[1] == ligne3[1]) and (ligne1[1] != "_ "):
        return 1
    if (ligne1[2] == ligne2[2]) and (ligne2[2] == ligne3[2]) and (ligne1[2] != "_ "):
        return 1


#menu de lancement
print("Bonjour voulez vous jouer ou voir les scores")
menu=0
#boucle meni
while menu ==0:
    choix = input("jouer   scores\n")
    if choix == "jouer" or choix == "Jouer":
        joueur1=input("Username 1 Croix :")
        joueur2=input("Username 2 Rond  :")
        menu=1
    elif choix == "scores" or choix == "Scores" or choix == "score" or choix == "Score":
    
        menu=1
        exit()
    else:
        print (choix)

#init du tableau
ligne1=['_ ','_ ','_ ']
ligne2=['_ ','_ ','_ ']
ligne3=['_ ','_ ','_ ']


affichage()

#lance la partie
while '_ ' in ligne1  or  '_ ' in ligne2  or  '_ ' in ligne3:
    tempo,joueur =tour(tempo)
    victoire=gagné()
    if victoire==1:
        affichage()
        print("\nle joueur",joueur,"a gagné")
        break
    affichage()

if victoire !=1:
    print("EGALITE")