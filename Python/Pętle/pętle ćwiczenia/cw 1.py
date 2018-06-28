"""
-wyświetalnie elementów listy (wszystkich)
-wyswietlanie listy wraz z numerem indeksu
"""
Hp = ["HARRY POTTER I KAMIEŃ FILOZOFICZNY", "HARRY POTTER I KOMNATA TAJEMNIC", "HARRY POTTER I WIĘZIEŃ AZKABANU"]
for index, movie in enumerate (Hp):
    print(index)
    print(movie)
"""
enumerate(iterable) fn wbudowana

Zwraca obiekt wyliczenia. Parametr iterable musi być sekwencją,
iteratorem lub innym obiektem obsługującym protokół iteracji.
Metoda next() iteratora zwróconego z funkcji enumerate() zwraca krotkę
zawierającą kolejny numer elementu (licząc od zera) oraz odpowiadający temu
numerowi element parametru iterable. Funkcja enumerate() jest użyteczna w celu
uzyskania poindeksowanej serii typu: (0, seq[0]), (1, seq[1]), (2, seq[2]),
"""
