import random

# option de triche 
cheat = 0

# syntawe des couleurs
class bcolors:
    WIN = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


# selection de niveaux (prompt,terminal)
print("NIVEAUX : \"Débutant\" (10 vies) \"Intermédiaire\" (5 vies) \"Expert\" (1 vie)")
lvl = input("choisissez votre niveaux : ")

# sélection des niveaux
if lvl == "débutant" or lvl == "debutant" or lvl == "Débutant" or lvl == "Debutant":
    vie = 10
    print(" mode débutant choisie")
elif lvl == "intermédiaire" or lvl == "intermediaire" or lvl == "Intermédiaire" or lvl == "Intermediaire":
    vie = 5
    print(" mode intermédiaire choisie")
elif lvl == "Expert" or lvl == "expert":
    vie = 1
    print(" mode expert choisie")
# option de triche 
elif lvl == "cheat":
    vie = 999
    cheat = 1
else:
    # si aucune entrée valable, on passe en dificulté débutant
    print(
        bcolors.WARNING + "\naucun niveaux choisit, niveaux débutant (10 vies) sélectioné par default\n" + bcolors.RESET)
    vie = 10

# ouvre le dico
with open('dico_france.txt', 'rt', encoding='latin1') as dico:
    """#lit le nombre de lignes 
    nb_lignes = len(dico.readlines())
    print('lignes : ', nb_lignes)
    """

    # choisit une ligne au hasard entre 0 et 22740 (nombre de mots dans le dico)
    rd_nb = random.randint(0, 22740)

    # choisit le mot a la ligne selectionné
    all_lines = dico.readlines()

# choisit les mots en fonction de la position dans le texte
mot_choisis = all_lines[rd_nb]

# Eviter les accidents de MAJ
mot_choisis=mot_choisis.lower()

# ferme le dico
dico.close()

# si la triche est activée, le mot sera affiché
if cheat == 1:
    print(mot_choisis)
# compte le nombre de caractere dans les mots (-1, car il en donne toujours 1 en trop(retours à la ligne ?)
longueur = len(mot_choisis) - 1

# enlève le saut a la ligne en fin de mot
mot_choisis = mot_choisis.rstrip()
# fait variable qui sera affiché et on l'affiche
mot_devine = "-" * len(mot_choisis)
print(bcolors.WARNING + mot_devine + bcolors.RESET)

lettres_deja_proposees = []

# tant que l'on a pas trouvé le mot et qu'il nous reste des vies
while mot_devine != mot_choisis and vie != 0:
    # on affiche les vies et les lettres déja proposé à chaque début de boucle
    print("il vous reste : ", vie, " vies")
    print("Vous avez proposée : ", lettres_deja_proposees)
    lettre = input("\nEntrez une lettre : ")

    # on perd une vie si la lettre n'est pas dans le mot et qu'elle n'a pas déja été proposé (je suis gentil)
    if lettre not in mot_choisis and lettre not in lettres_deja_proposees:
        vie -= 1

    if lettre not in lettres_deja_proposees:
        lettres_deja_proposees += [lettre]

    elif lettre in lettres_deja_proposees:
        print(bcolors.FAIL + "\nla lettre \"", lettre,
              "\" à déja été proposé !\nAucune vie ne vous à été déduite\n" + bcolors.RESET)

    for i in range(len(mot_choisis)):
        if lettre == mot_choisis[i]:
            mot_devine = mot_devine[:i] + lettre + mot_devine[i + 1:]
    print(bcolors.WARNING + mot_devine + bcolors.RESET)

if vie == 0:
    print(bcolors.FAIL + "\nGame Over !\nLe mot a trouver était :", mot_choisis + bcolors.RESET)
if mot_choisis == mot_devine:
    print(bcolors.WIN + '\n Félicitation ! Le mot :', mot_choisis, 'a été trouvé\n' + bcolors.RESET)