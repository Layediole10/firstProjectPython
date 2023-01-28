data = input("Entrez des nombres séparés par des virgules: ")
list = data.split(",") #divise la chaine de nombres en une liste de nombres individuels a l'aide de "split()" qui prend un séparateur en entrée
print(list)
print(tuple(list))

