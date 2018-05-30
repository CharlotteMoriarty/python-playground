
#indeksy powtórka (liczone od zera)
movie = "Harry Potter"
movie[2]
print(movie[2])
print(movie[-1])
#kontkatenacja czyli łączenie
print("Harry Potter" +" i kamień filozoficzny")

#powielanie
print ("uczeń " * 3)

#formatowanie za pomocą metody format zastepująca {} podanym parametrem
print('Harry{}'.format(' Potter'))
gryffindor = " Hermiona Ron"
print('Harry{} '.format(gryffindor))

name = input('Your name: ')
carracter = input('Your favourite carracter is? : ')
movie = input('Your favourite Harry Potter movie is ? : ')

information = """The {} favourite carracter is {} and you really like {}""".format(name, carracter, movie)
print(information)

#dzielenie łańcuchów za pomocą split
movie1 = "Harry.Potter i kamień filozoficzny".split(".")
print(movie1)

#metoda join czyli dodawanie znaków pomiędzy wszystkimi znakami łańcucha

name = "Hermiona"
result = "*".join(name)
print(result)

#strip usuwanie pustych znaków np spacji
house = "   Gryffindor"
house = house.strip()
#print(house)

#zastepowanie replace
house2 = "Slytherin"
result = house2.replace("S","g")
print(result)

#znajdowanie indeksu w tym przypadku W ma index 4
ron = "Ron Weasley"
print(ron.index("W"))

#szukanie z zastosowaniem wyjątku
try:
    "Ron Weasley".index("H")
except:     
    print("Nie znaleziono")
    
#zapisywanie cytatów
print("\"Harry Potter i insygnia śmierci\"")

#wycinki
"""
tworzenie ich polega na utworzeniu danej iterowalnej będącej podzbiorem elementów danej
pierwotnej
gdzie indeks początkowy to pierrwszy element wycinka a
indeks końcowy to index ostatniego elementu
"""
gryffindor = ["Ron", #0
              "Hermiona",#1
              "Harry"] #2
print(gryffindor[0:2])
print(gryffindor[:3])
print(gryffindor[:])
