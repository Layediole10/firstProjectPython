import random
nbrSecret = random.randrange(0, 9)
nbrChance = 0
nbrEssai = 3
while nbrChance < nbrEssai:
    devinette = input('donnez un nombre entre 0 et 9 ')
    nbrChance += 1
    if int(devinette) == int(nbrSecret):
        print('BRAVO!!!')
        break
else:
    print('Vous avez perdu!')

"""listElem = [30, 6, 14, 77, 8, 9, 1]
element = listElem[0]
for maxElem in listElem:
    if maxElem >= element:
        element = maxElem
print(f"le plus grand nombre de la liste est : {element}")"""

"""liste = [11, 34, 5, 2, 8, 1, 3, 2, 4, 5, 0, 9, 7, 0, 5, 8]
for elem in liste:
    if liste.count(elem) > 1:
        liste.remove(elem)
#print(liste)
liste.sort()
print(liste)"""

tel = input("Entrez votre numero telephone: ")
chiffre_caract = {
    "1": "un",
    "2": "deux",
    "3": "trois",
    "4": "quatre",
}
mon_num = ""
for item in tel:
    mon_num += chiffre_caract.get(item, "?")+ " "
print(mon_num)


def carre_num(num):
    return num * num


print(carre_num(3))
print(carre_num(13))
