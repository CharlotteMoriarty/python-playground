"""
utorzenie słownika dla jednego z wybranych szczytów oraz utworzenie programu
pozwalającego pytać o poszczególne dane
"""
wyszukiwarka = ['Państwo','Położenie','Wysokość','Wybitność','Pierwsze wejście']


print('Których informacji szukasz: ' ,wyszukiwarka)#test danych
szczyt_krywan = {'Państwo':'Słowacja',
                 'Położenie':'Tatry Wysokie',
                 'Wysokość':'2494m n.p.m.',
                 'Wybitność':'400m',
                 'Pierwsze wejście': 'Pierwsze odnotowane wejście :1772'}

informacje = input('Interesuje mnie...  ')

if informacje in szczyt_krywan:
    szczyt_krywan = szczyt_krywan[informacje]
    print(szczyt_krywan)
    
    if informacje == 'Wybitność':
        print('''WYBITNOŚĆ to liczba określająca, na ile szczyt wyróżnia się ze swojego otoczenia. Wybitność definiuje się jako różnicę wysokości między danym szczytem i najniższą warstwicą go okalającą,\n
          która nie obejmuje żadnego wyższego szczytu. Wysokość tej warstwicy określa wysokość przełęczy zwanej kluczową, oddzielającej dany szczyt od wyższego,
          kolejnego szczytu na grzbiecie (wododziale). Spośród przełęczy oddzielających dany szczyt od wyższych sąsiadów przełęczą kluczową jest przełęcz najwyższa.
          Wybitność szczytu to inaczej jego wysokość względna nad przełęczą kluczową.''')
    
else:
    print('Nie posiadany danych o ', informacje)
    
