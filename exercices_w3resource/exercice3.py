import datetime
the_date = datetime.datetime.now() #definie la date et l'heure
print(the_date.strftime("%x"), the_date.strftime("%X")) #format la date et l'heure avec la methode "strfime()"