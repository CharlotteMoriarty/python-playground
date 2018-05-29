#def funkcji
def f(x):
    return x * 2
#wywołanie funkcji
result =  f(4) 
print(result) 

def f(a,b,c):
    return a + b +c
result = f(1,2,9)
print(result)
#bez return zwraca none
#do czego to można wykorzystać
def f():
    z = 1+2
result = f()
print(result)
#fn wbudowane
len('dlugosc')
str(100) #zmieni na nowy obiekt string
int("12") #zmiei string na nowy obiekt int
float(2) #zmmiana całkowitych na rzeczywiste 
age = input('Podaj swój wiek') #pobiera dane
int_age= int(age)
if int_age <40:
    print('super')
else:
    print('też ok')
#zmiana zapis w zmiennej globalnej wewnątrz fn
price = 10
def f():
    global price
    price-=2
    print(price)
f()
#obsługa wyjątków

try:
    a = input('wpisz liczbę , którą chcesz podzielić')
    b = input('podziel przez')
    a = int(a)
    b = int(b)
    print(a/b)
except(ZeroDivisionError, ValueError): #wpisanie 0, problem str zamiast liczny
    print('Pamiętaj nie dzielimy przez 0 lub podaj inną liczbę')
"""
łancuch dokumentacyjny
komentrarz blokowy
"""
#parametry wymagane mają przypisywaną wartości domyślne, opcjonalne mają nadawaną przez nas wartość domyślną
