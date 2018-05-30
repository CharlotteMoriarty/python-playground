"""
Zwróć indeks dla litery h w słowie Sherlock
rozpisz opcje obsługi wyjąku dla przykładowej litery nie bedącej w łańcuchu
"""
title = "Sherlock"
print(title.index("h"))


try:
    print(title.index("g"))
except:
    print("Nie znaleziono")
