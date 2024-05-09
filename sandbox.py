import random
from colorama import Back, Fore, Style

def initialiser_grille():
    tailleGrillei = random.randint(9, 19)

    tailleGrillej = random.randint(19, 39)
    GrilleJoueur = [[(Back.BLACK + " " + Style.RESET_ALL)] * (tailleGrillej) for _ in range(tailleGrillei)]
    positionJoueur = [random.randint(0, tailleGrillei - 1), random.randint(0, tailleGrillej - 1)]
    GrilleJoueur[positionJoueur[0]][positionJoueur[1]] = (Fore.RED + "▲" + Style.RESET_ALL)  # on place le joueur
    GrilleV1 = [[" "] * tailleGrillej for _ in range(tailleGrillei)]
    GrilleV1[positionJoueur[0]][positionJoueur[1]] = (Fore.RED + "▲" + Style.RESET_ALL)  # on place le joueur
    tailleSituation = int(0.025 * tailleGrillej * tailleGrillei)
    tailleMur = int(0.1 * tailleGrillej * tailleGrillei)
    for i in range(tailleSituation):  # positifs
        while True:
            chiffreX = random.randint(0, tailleGrillei - 1)
            chiffreY = random.randint(0, tailleGrillej - 1)
            if GrilleV1[chiffreX][chiffreY] == " ":
                GrilleV1[chiffreX][chiffreY] = "P"
                break
    for i in range(tailleSituation):  # negatifs
        while True:
            chiffreX = random.randint(0, tailleGrillei - 1)
            chiffreY = random.randint(0, tailleGrillej - 1)
            if GrilleV1[chiffreX][chiffreY] == " ":
                GrilleV1[chiffreX][chiffreY] = "N"
                break
    for i in range(tailleMur):  # negatifs
        while True:
            chiffreX = random.randint(0, tailleGrillei - 1)
            chiffreY = random.randint(0, tailleGrillej - 1)
            if GrilleV1[chiffreX][chiffreY] == " ":
                GrilleV1[chiffreX][chiffreY] = "M"
                break
    while True:
        chiffreX = random.randint(0, tailleGrillei - 1)
        chiffreY = random.randint(0, tailleGrillej - 1)
        if GrilleV1[chiffreX][chiffreY] == " ":
            GrilleV1[chiffreX][chiffreY] = "S"
            break
    return GrilleJoueur, GrilleV1, positionJoueur, tailleGrillei - 1, tailleGrillej - 1


def afficher_grille(ma_grille, pseudo, score,boolDebug):
    print("Si la fenêtre de jeu est trop étroite, vous pouvez dézoomer le terminal avec la molette de votre souris")
    print((Fore.BLUE + "┌" + Style.RESET_ALL) + (Fore.BLUE + "─" + Style.RESET_ALL) * (len(ma_grille[0]) - 1) + (
                Fore.BLUE + "─┐" + Style.RESET_ALL))
    for i, ligne in enumerate(ma_grille):
        print(Fore.BLUE + "│" + Style.RESET_ALL, end="")
        for valeur in ligne:
            print((Fore.BLUE + "" + Style.RESET_ALL) + valeur + "", end="")

        print(
            Fore.BLUE + "│ " + Style.RESET_ALL + Fore.RED + " ▲" + Style.RESET_ALL + " curseur joueur" if i == 1 else Fore.BLUE + "│  " + Style.RESET_ALL + Fore.RED + Back.GREEN + "▲" + Style.RESET_ALL + " devant une situation" if i == 2 else Fore.BLUE + "│  " + Style.RESET_ALL + Back.WHITE + " " + Style.RESET_ALL + " case déjà traversee" if i == 3 else Fore.BLUE + "│ " + Style.RESET_ALL +(" "+pseudo+": "+Fore.GREEN + str(score) + Style.RESET_ALL if int(
                score) >= 0 else " "+pseudo+": "+Fore.RED + str(score) + Style.RESET_ALL) if i ==0 else Fore.BLUE + "│ " + Style.RESET_ALL + " M : Mur" if i ==4 and boolDebug else Fore.BLUE + "│ " + Style.RESET_ALL + " P : Situation Positive" if i==5 and boolDebug else Fore.BLUE + "│ " + Style.RESET_ALL + " N : Situation negative" if i==6 and boolDebug else Fore.BLUE + "│ " + Style.RESET_ALL + " S : Sortie" if i == 7 and boolDebug else Fore.BLUE + "│ " + Style.RESET_ALL)
    #24 +2
    print((Fore.BLUE + "└") + (Fore.BLUE + "─" + Style.RESET_ALL) * (len(ligne) - 1) + (
                Fore.BLUE + "─┘" + Style.RESET_ALL))

grilleJ, GrilleA, posJ, tailleGi, tailleGj = initialiser_grille()
afficher_grille(grilleJ, "Yann", "0", False)