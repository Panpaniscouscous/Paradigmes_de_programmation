#Création des deux listes pour la liste des étudiants et les notes que l'utilisateur va saisir
list_etudiants = []
list_notes = []

#Cette fonction sert à calculer la moyenne des notes dans une liste. Elle prend en compte 1 paramètre : une liste
def calculer_moyenne(list):
    nbr = 0
    for i in range(len(list)):
        nbr = nbr + list[i]
    nbr = nbr / len(list)
    return f"La moyenne de classe est de {nbr}."

#Cette fonction permet d'afficher la répartir les étudiants de la manière suivant (elle prend en compte 2 paramètres, les notes et les étudiants) :
#Ce qui ont plus ou égale à 10 vont dans ue liste appelé list_etudiants_sup et ceux qui ont strictement moins de 10, ils sont placés dans une liste nommée list_etudiants_inf
def afficher_repartition(list_notes, list_etudiants):
    list_etudiants_sup = []
    list_etudiants_inf = []
    for i in range(len(list_notes)):
        if list_notes[i] >= 10:
            list_etudiants_sup.append(list_etudiants[i])
        else:
            list_etudiants_inf.append(list_etudiants[i])
    print(f"Étudiants ayant réussi : {list_etudiants_sup}")
    print(f"Étudiants en échec : {list_etudiants_inf}")

#Cette fonction sert à calculer la meilleure_note parmi une liste notes et affichera le nom de cette étudiant. Elle prend en compte 2 paramètres : noms (des étudiants) et les notes (des étudiants)
def meilleure_note(noms, notes):
    indices = 0
    meilleure_note = 0
    for i in range(len(notes)):
        if meilleure_note < notes[i]:
            meilleure_note = notes[i]
            indices = i
        else:
            pass
    print(f"L'étudiant ayant la meilleure note est {noms[indices]} avec {meilleure_note}.")

#nbr = float(input("Test : "))
#float(nbr)
#print(type(nbr))

#Cette boucle infinie permet de demander à l'utilisateur combien de notes il veut saisir. S'il tape un string, la boucle infinie va lui dire qu'il y a une erreur et lui redemande de taper le nombre d'étudiants qu'il veut saisir. S'il tape un int, on sort de la boucle grâce à break 
while True:
    try:
        nbr_etudiants = int(input("Combien d'étudiants voulez-vous saisir (un chiffre) ? "))
        break
    except:
        print("Il y a une erreur dans la saisie.")



#nbr_etudiants=int(nbr_etudiants)

#On définit i pour répépter la boucle à certains nombres de fois pour qu'il s'arrête après avoir fait toutes la liste des étudiants à taper.
i = 0
#Le premier while permet de faire une boucle et se termine jusqu'à ce qu'on tape le nombre d'étudiants exacte à taper.
#Le deuxième while permet de créer une boucle infinie qui permet de vérifier si la note saisie est bien un nombre ou un nombre à virgule.
while (i < nbr_etudiants):
    list_etudiants.append(input("Tapez le nom de votre étudiant à ajouter : "))
    while True:
        try:
            valeur = float(input(f"Tapez la note de {list_etudiants[i]} : "))
            break
        except:
            print("Il y a une erreur dans la saisie de la note")
    i += 1
    list_notes.append(valeur)

#Je print pour afficher la moyenne de la list_notes, avec la séparation des notes au-dessus et en-dessous de 10 puis affiche la meilleure note
#print(list_etudiants)
#print(list_notes)
print(calculer_moyenne(list_notes))
afficher_repartition(list_notes,list_etudiants)
meilleure_note(list_etudiants,list_notes)


