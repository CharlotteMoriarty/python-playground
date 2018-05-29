#metody są pojęciem zbliżony do fn ale wywoływane są na rzecz konkretnego obiektu
#można im przekazywać parametry
'zmiana wielkości'.upper()
'karolina'.replace('k','K')
def zmiana():
    print('karolina'.replace('k','K'))
zmiana()  
#listy []
"""
pusta lista zapis :
1 students = list()
2 Hogwart =[]* -> tu można dodawać gotowe elementy od razu
"""
Hogwart = ['Gryffindor','Slytherin','Ravenclaw','Hufflepuff']
Hogwart.append('Hogwart school') #dodawanie elementów
print(Hogwart)
Hogwart[1] # pobieranie konkretnego indeksu
Hogwart[4] = 'Szkoła' #zmiana elementu
print(Hogwart,' po zmianie')
#Łączenie list
Gryffindor = ['Harry', 'Hermiona', 'Ron']
print(Hogwart + Gryffindor)
'Harry' in Gryffindor #sprawdzanie dostępności elementu na liście
'Harry' not in Hogwart #sprawdzanie braku dostępności elementu na liście
len(Hogwart) #sprawadzanie ilości elementów
"""
Opcje sprawdzającą można wykorzystać do napisania prostej funkcji, której celem
sprawdzenie czy wybór użytkownika jest na naszej liście
w tym przypadku lista ma dwa elementy, użytownik zgaduje swój dom w szkole efekt
w zależności od tego czy opcja użytkownika jest na liście 
"""

def guess():
    Hogwart2 = ['Gryffindor','Slytherin']
    house = input('Guess your Hogwart House ')
    if house in Hogwart2:
        print('Yes, ',house,'is your new house')
    elif house not in Hogwart2:
         print('Try again')
guess()
#krotki TUPLE to kontenery przechowujące obiekty w określonej kolejności i są niemodyfikowalne
#zapisywane za pomocą () lub = tuple() i nawet jeśli ma jeden element musi być po nim przecinek
name =('Hermiona',)
print(name)
#imię to coś co się nie zmiania dlatego zapisujemy je za pomocą krotki, nazwisko zapisalibyśmy za pomocą
#edytowalnej listy gdyż istnieje prawdopodobieństwo, że dana ta może zostać zmieniona

#Słowniki - modyfikowalne, nieiterowalne,nazwa = {} lub nazwa=dict(), oparte na odwzorowywaniu tzn kojarzeniu
#klucza z wartością, wyszukiwanie po kluczu nie po wartości
GryffindorTeam = {'Harry':'Potter','Hermiona':'Granger'}
GryffindorTeam['Ron'] = 'Weasley' #dodawanie pary
print(GryffindorTeam)
print(GryffindorTeam['Harry']) #pobranie wartości
#klucz jest niezmienialny należy o tym pamiętać, wartości mogą być wpisywane jako modyfikowalne obiekty
GryffindorTeam['Hermiona']= 'Weasley'
print(GryffindorTeam)
#słownik / klucze można przeszukać za pomocą in ale nie wartości
'Hermiona' in GryffindorTeam
'Draco' not in GryffindorTeam
del GryffindorTeam['Hermiona'] #usuwanie pary ze słownika
print(GryffindorTeam)
"""
Napiszmy wyszukiwarkę nauczycieli  Hogwartu z wykorzystaniem słownika
"""
przedmioty = ['Astronomia','Eliksiry', 'Historia magii','Latanie',
                'Mugoloznastwo','Obrona przed czarną magią']
print('Przedmioty w tym semestrze ',przedmioty)
nauczyciele =  {'Astronomia':'Aurora Sinistra',
                'Eliksiry': 'Severus Snape',
                'Historia magii': 'Cuthbert Binns',
                'Latanie' : 'Rolanda Hooch',
                'Mugoloznastwo': 'Kwiryniusz Quirrel',
                'Obrona przed czarną magią': 'Remus Lupin'}
lekcja = input('Podaj przedmiot, który chesz sprawdzić  ')
if lekcja in nauczyciele:
    nauczyciele = nauczyciele[lekcja]
    print('Lekcje prowadzi  ',nauczyciele)
else:
    print('Nie znaleziono przedmiotu!!')
                
#kontenery w kontenerach
dziennik = []
dziennik_gryffindor = ["Harry Potter", "Hermiona Granger", "Ron Weasley"]
dziennik_slytherin = ["Draco Malfoy","Gregory Goyle","Vincent Crabbe"]
dziennik_ravenclaw = ["Luna Skamander","Cho Chang","Marta Warren"]
dziennik_hufflepuff = ["Ernie Macmillan","Susan Bones","Hanna Abbott"]
    
dziennik.append(dziennik_gryffindor)
dziennik.append(dziennik_slytherin)
dziennik.append(dziennik_ravenclaw)
dziennik.append(dziennik_hufflepuff)
print(dziennik)

#odwołanie do indeksu dziennika a konkretnie do rupy ravenclaw
dziennik_ravenclaw = dziennik[2]
print(dziennik_ravenclaw)
#dodawanie elementów do dziennika
dziennik_ravenclaw.append("Padma Patil")
print(dziennik_ravenclaw)
"""
krotki można zapisac w listach listy w krotkach ,
słowniki też w krotkach jak i listach
"""

#input zabezpieczzenie konsoli przed wyłączeniem się ;)

input()
    
