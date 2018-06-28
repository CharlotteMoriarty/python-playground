#for wykonywane jeden raz dla każdego elementu

name = "Hermiona"
for character in name:
    print(character)
movie = ["Harry Potter i Kamień Filozoficzny","Harry Potter i Komnata Tajemnic", "Harry Potter i więzień Azkabanu"]
for movie_title in movie:
    print(movie_title)
movie_2 = ("Harry Potter i Czara Ognia","Harry Potter i Zakon Feniksa","Harry Potter i Książę Półkrwi")
for movie_title in movie_2:
    print(movie_title)
movie_3 = {"Harry Potter i Insygnia Śmierci: Część I": "7a" ,"Harry Potter i Insygnia Śmierci: Część II":"7b"}
for movie_title in movie_3:
    print(movie_title)
#upper dla zmiennej
    print(name.upper())
#z wykorzystaniem zmiennej indeksowej

tv =["Harry Potter i Kamień Filozoficzny","Harry Potter i Komnata Tajemnic", "Harry Potter i więzień Azkabanu"]
i=0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i+= 1

print(tv) 

#funkcja range: tworzenie sekwencji liczb
for i in range(5,10):
    print(i)

#while wykonująca kod tak długo jak warunke będzie mieć
x = 1
while x <9:
    print('{}'.format(x))
    x+=1
print("Harry Potter dotychczasowa liczba filmów")    
"""
jeśli warunek zawsze będzize true , pętla będzie wykonywała się przez cały czas (pętla nieskończona
"""
#break - przerwanie działania pętli
while True:
    print("I like the Harry Potter movies")
    break
questions = ["Would you like to vist Warner Bross Studio in London? ",
             "Would you like to plan your visit now? ",
             "Do you need a bus ticket for your trip? "]
i = 0
while True:
    print("Write  [Y/N] ")
    answer = input(questions[i])
    if answer == "N":
        break;
    i = (i+1) % 3 #pozwoli na cykliczne zadawanie każdego z pytania jeśli odpowiedzi są Y
#continue - przerwanie bieżącej pętli i kontynuowanie następnej
"""
czyli jeśli mielibyśmy zestaw liczb chcielibyśmy wyswietlić wszystkie poza jedną
skorzystamy z instrukcji contiunue
"""
for i in range (1,5):
    if i ==3:
        continue
    print(i)
#pętle zagnieżdzone (wewnętrzna) i obejmująca ją pętla zewnętrzna
"""
wewnętrzna przegląda całą swoją zmienną w ramach jednego przejścia /iteracji/ pętli zewnętrznej
"""
list1 = ["Harry Potter i "]
list2 = ["Kamień Filozoficzny", "Komnata Tajemnic", "Więzień Azkabanu", "Czara Ognia"," itd"]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)        
