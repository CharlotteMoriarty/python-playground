"""
Napisz program, który zawiera pętle nieskończoną z opcją q/quit
oraz listę liczb.
Podczas każdej iteracji pętli poproś u zgadniecie liczby i wyswietl informacje
zwrotną
"""
number = [12, 44, 22, 9]

while True:
    answer = input("Guess the number or wtite Q for exit")
    if answer == "Q":
        break
    try: #obsługa wyjątku na wypadek wpisania litery zamiast liczby
        answer = int(answer)
    except ValueError:
        print("Write the number")
    if answer in number:
        print("It's your lucky day")
    else:
         print("Try again")
