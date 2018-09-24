import sys
from logging import exception

# on  demande a l'utilisateur de renseigner le jour
day = int(input("Entrez le numéro du jour : "))

# on vérifie que le jour rentré est compris entre 1 et 31
if 1 > day > 31:
    exception(" le jour rentré n'est pas bon")
    sys.exit(0)
# on  demande a l'utilisateur de renseigner le mois
month = input("Entrez le mois : ").lower()
# on  demande a l'utilisateur de renseigner le l'année
year = int(input("Entrez l'année : "))

# On créer des bibliothèque contenant les valeurs permettant de trouver le bon jour de la semaine en fonction du mois, de l'année et du jour
monthsIds = {'janvier': 0, 'fevrier': 3, 'mars': 3, 'avril': 6, 'mai': 4, 'juin': 4, 'juillet': 6, 'août': 2, 'septembre': 5, 'octobre': 0, 'novembre': 3, 'decembre': 5}
yearsIds = {'1600': 6, '1700': 4, '1800': 2, '1900': 0, '2000': 6, '2100': 4}
daysIds = {'1': "lundi", '2': "mardi", '3': "mercredi", '4': "jeudi", '5': "vendredi", '6': "samedi", '7': "dimanche"}

# on récupère les 2 derniers caractères de l'année et on le divise par 4, on récupère le résultat sans reste
endCutYear = year % 100
divYear = endCutYear // 4

# on vérifie que le mois rentré est correcte et on récupère sa valeur sinon on arrète le programme
if month in monthsIds:
    monthId = monthsIds[month]
else:
    exception(" le mois rentré n'est pas bon")
    sys.exit(0)

# on regarde si c'est une anné bissextile
if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and (month == "janvier" or month == "février"):
    monthId = monthId - 1

# on calcule le numéro du jour et on récupère le bon jour grâce a lui
total = endCutYear + divYear + day + monthId + yearsIds[str(year - endCutYear)]
dayInString = daysIds[str(total % 7)]

# on affiche le résultat
print("le " + str(day) + " " + month + " " + str(year) + " est un : " + dayInString)

