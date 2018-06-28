#moduły to obszary kodu zawietrające mniejsze jego części

#moduły wbudowane importowane za pomocą import[nazwa]
import math
import random
import statistics
print(math.pow(4,4))
print (random.randint(0,10))


num = [12,24,36,48,50,62]
print (statistics.mean(num))
#średnia

print(statistics.median(num))
#mediana
"""
Mediana, wartość środkowa, wartość przeciętna, drugi kwartyl –
wartość cechy w szeregu uporządkowanym, powyżej i poniżej której znajduje się
jednakowa liczba obserwacji. ... Aby obliczyć medianę ze zbioru n obserwacji,
sortujemy je w kolejności od najmniejszej do największej i numerujemy od 1 do n.
"""
from statistics import mode, StatisticsError
try:
    m = mode(num)
except StatisticsError:
    print ("No unique mode found")
#dominanta
#w przypadku wybranych liczb gdy nie obsłuzymy wyjątku statistic error  pojawi
#się błąd no unique mode found    
"""
Dominanta (wartość modalna, moda, wartość najczęstsza) to jedna z miar tendencji
centralnej, statystyka dla zmiennych o rozkładzie dyskretnym, wskazująca na
wartość o największym
prawdopodobieństwie wystąpienia, lub wartość najczęściej występująca w próbie.
PONIŻEJ PRZYKŁAD BEZ KONIECZNOŚCI OBSŁUGI WYJĄTKU STATISTIC ERROR
"""
nums = [1, 5,33,12,46,12,12, 33,2]
print(statistics.mode(nums))

#sprawdzanie czy dane słowa są kluczowe
import keyword
print(keyword.iskeyword('random'))
print(keyword.iskeyword('for'))
"""
lista słów kluczowych
and       del       for       is        raise    
assert    elif      from      lambda    return   
break     else      global    not       try      
class     except    if        or        while    
continue  exec      import    pass      yield    
def       finally   in        print
"""
