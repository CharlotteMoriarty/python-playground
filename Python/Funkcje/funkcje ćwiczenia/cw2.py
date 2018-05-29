#2. pobierz łańcuch znaków i go wyświetl
#dodatkowo zastosowano obsługę wyjątku

def myInput():
    try :
        a = input('write something')
        a = int(a)
        print('you wrote number', a)
    except ValueError:
        print('You wrote word',a)
myInput()
