import csv

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Écriture dans un fichier CSV
with open('GrilleAdmin.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in data:
        writer.writerow(row)


data2 = []


with open('GrilleAdmin.csv', 'r', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        # Convertir les éléments de la ligne en type approprié si nécessaire
        # Ici, nous convertissons chaque élément en entier
        data2.append([int(item) for item in row])

# Affichage du tableau 2D récupéré
print(data2)