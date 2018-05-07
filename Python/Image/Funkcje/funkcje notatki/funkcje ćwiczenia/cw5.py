#5 konwertowanie łańcucha na float wraz obsługą  wyjątku
def konwertowanie():
    try:
        price = input('przelicz')
        price = float(price)
        print('Cena wynosi : ',price)
    except ValueError: 
        print('podaj liczbę')
konwertowanie()
