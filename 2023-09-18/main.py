import os, random

def main() -> None:
    #"Főprogram" függvénye
    egyenleg = 1000
    m = ''
    while m != 0:
        informacio(egyenleg)
        m = menu()
        match m:
            case '1':
                tet = osszegBekeres(egyenleg)
                szam = sorsolas()
                if szam == 0 or szam % 2 == 1:
                    egyenleg -= tet
                    print(f'VESZTETT, az új egyenlege: {egyenleg}')
                else:
                    egyenleg += tet
                    print(f'Nyert, az új egyenlege: {egyenleg}') 
                input('\n\nENTER')
            case '2':
                tet = osszegBekeres(egyenleg)
                szam = sorsolas()
                if szam % 2 == 0:
                    egyenleg -= tet
                    print(f'VESZTETT, az új egyenlege: {egyenleg}')
                else:
                    egyenleg += tet
                    print(f'Nyert, az új egyenlege: {egyenleg}')
                input('\n\nENTER')
            


def informacio(penz: int) -> None:
    os.system('cls')
    # \t => tabulátor
    print(f'Rulett játék \t\t\t Jelenlegi egyenleg: {penz} $')

def menu() -> int:
    # \n => sortörés
    print('\n')
    print('1.. Tét: Páros')
    print('2..Tét: Páratlan')
    #print('3..Tét: ')
    print('\n0..Kilépés')

    return input('\nVálasztás: ')

def osszegBekeres(maxOsszeg: int) -> int:
    osszeg = 0
    while osszeg <= 0 or osszeg > maxOsszeg:
        informacio(maxOsszeg)
        osszeg = int(input('Mekkora osszeget tesz vel? '))
    return osszeg

def sorsolas() -> int:
    szam = random.randint(0,36)
    print(f'\n\nA "gurított" szám: {szam}')
    return szam

main()