import csv
DonneesPartie = []
with open('PartieEnCours.csv', 'r', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        DonneesPartie.append(row)
print(len(DonneesPartie))