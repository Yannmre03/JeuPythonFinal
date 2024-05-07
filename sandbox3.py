import csv

def fonction_Sortie(nomF, ScoreF):
    row = [nomF, ScoreF]
    with open('Scores.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row)
def fonction_afficher_scores():
    Scores = []
    with open('Scores.csv', 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            Scores.append(row)
    scoreBis = []
    for i in range(len(Scores)):
        cmpt = len(Scores) - i
        scoreBis.append(Scores[cmpt - 1])
    return scoreBis

from colorama import Fore, Style, init
def fonctionAfficherScores(scores):
    print(Fore.GREEN + "Tableau des scores:")
    for i in range(len(scores)):
        nom, score = scores[i]
        print(Fore.YELLOW + f"{nom}" + Fore.CYAN + " a eu le score de: " + Fore.RED + f"{score}")
def fonctionAfficherScores(scores):
    print("Tableau des scores: ")
    for i in range(len(scores)):
        print(str(scores[i][0]) + " a eu le score de: "+ str(scores[i][1]))
# Exemple d'utilisation
print(5//2)

print("Yann : "+Fore.GREEN + str(Score) + Style.RESET_ALL if int(
                Score) >= 0 else Fore.RED + "Score actuel: " + str(Score) + Style.RESET_ALL)