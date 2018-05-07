# 4 definiowanie dwóch fn

"""
Napisz funkcje sprawiającą by jedna drużyna wygrywała a druga pregrywała
pierwsza fn wyswietla  pobrany parametr dzielony na 2
druga podwyższa wynik mnożąc wcześniejszy wynik przez 4
"""
print('Game day')
slytherin = input('Write points for slytherin :')
slytherin = int(slytherin)
slTotal = (slytherin//2)
def slytherinTotal():
    print(slTotal)
slytherinTotal()    
def gryfindor():
    print('Gryfindor points: ', slTotal*4)
gryfindor()
