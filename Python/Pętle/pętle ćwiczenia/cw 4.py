"""
pomnóż wszystkie liczby z pierwszej listy przez wszystkie z drugiej
wynik zapisz w trzeciej
"""
num1 = [1,2,3,4]
num2 = [5,6,7,8]
multi = []
for i in num1:
    for j in num2:
        multi.append(i*j)
print(multi)        
