from functools import reduce

#Exercice 1
list_prix = [50, 20, 35, 100, 80]
conv_dollars = map(lambda x: f"{x * 1.1} $", list_prix)

print(list(conv_dollars))

#Exercice 2
list_age = [12, 25, 17, 18, 40, 15, 22, 61, 72, 54, 8, 32, 95]
list_senior = []
extraction_age = list(filter(lambda x: x >= 18, list_age))
list_senior = list(filter(lambda x: x >= 60, list_age,))

print(list_age)
print(list_senior)

#Exercice 3
list_ventes = [120, 50, 30, 20, 90, 100]

total_ventes = reduce(lambda x, y: x + y, list_ventes)
produit_calcul_list = reduce(lambda x, y : x * y, list_ventes)
print(total_ventes)
print(produit_calcul_list)

#Exercice 4
list_notes = [12, 15, 9, 18, 6, 20, 14]
#convert_notes = list(map(lambda x: x * 5, list_notes))
list_notes = list(map(lambda x: x * 5, list_notes))
#extract_notes = list(filter(lambda x: x >= 50, list_notes))
list_notes = list(filter(lambda x: x >= 50, list_notes))
print(list_notes)
moyenne = reduce(lambda x, y: x + y, list_notes)
#print(moyenne)
moyenne = moyenne / len(list_notes)
#print(list_notes)
print(moyenne)
#print(extract_notes)