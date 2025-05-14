print("""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jarmila Kroulová
email: jarmilxxx@seznam.cz
"""
)

import random


def pocet_hracu():
    """
    Dává uživateli možnost výběru hry 
    proti jinému uživateli nebo proti počítači.
    Vrací:
    True pro hru proti počítači(1 hráč)
    False pro hru proti jinému uživateli(2 hráči).
    """
    while True:    
        pocet = input("How many players will play (1 or 2)?: ")
        if pocet.isdigit():
            if 1 <= int(pocet) <= 2:
                if int(pocet) == 1:
                    return True
                else:
                    return False
            else:
                print("Please enter only 1 or 2.")
        else:
            print("Please enter a valid number.")

def zobraz_herni_plochu(box, separator):
    """
    Z proměnné "box" což je list stringů a z proměnné "separator"
    vytvoří tabulku 3x3 pole.

    Parametry:
    box - list stringů představující herní plochu
    separator - řetězec oddělující řádky tabulky
    """
    for i in range(0, 9, 3):
        print(separator)
        print(f"| {box[i]} | {box[i+1]} | {box[i+2]} |")
    print(separator)
    print()

def uvitani():
    oddelovac = "=" * 44
    pozdrav = "Welcome to Tic Tac Toe"
    pravidla = """GAME RULES:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:
    * horizontal,
    * vertical or
    * diagonal row"""
    cara = "-" * 44
    print(pozdrav, oddelovac, pravidla, sep = "\n")
    print(f"{oddelovac}\nLet's start the game\n{cara}")  

def tah_hrace(znacka, box):
    """
    Přijme a zpracovává vstup od uživatele, 
    ověří platnost a zapíše značku do pole.
    Pokud je pole obsazené, funkce se ptá na nový vstup.
    Zároveň umožňuje hráči ukončit hru.

    Parametry: 
    znacka - značka hráče("x" nebo "o")
    box - list stringů představující herní plochu

    Vrací: 
    Upravený list s nově zapsanou značkou.
    """
    while True:
        move = input(f"Player {znacka} | Please enter your move number or q for quit: ")
        if move == "q":
            print("Terminate the game.")
            quit()
        elif move.isdigit() and 1 <= int(move) <= 9:
            index = int(move) - 1
            if box[index] not in ["x", "o"]:
                box[index] = znacka
                return box
            else:
                print("This field is already taken. Try another.")
        else:
            print("Invalid number!Please enter a number from 1 to 9!")
            continue

def tah_pocitace(znacka, box):
    """
    Přijme a zpracovává vstup od počítače,
    zapíše značku do pole. Pokud je pole obsazené, 
    funkce se ptá na nový vstup.

    Parametry: 
    znacka - značka hráče("x" nebo "o")
    box - list stringů představující herní plochu

    Vrací: 
    Upravený list s nově zapsanou značkou.
    """
    print(f"Player {znacka} (computer) is making a move . . . ")
    while True:
        index = random.randint(0, 8)
        if box[index] not in ["x", "o"]:
            box[index] = znacka
            return box

def kontrola_vyhry(znacka, box):
    """
    Zkontroluje, zda hráč vyhrál, nebo je hra ukončena bez vítěze.
    
    Parametry:
    znacka - značka hráče("x" nebo "o")
    box - list stringů představující herní plochu
    
    Vrací:
    True, pokud je hra ukončena vítězstvím, nebo remízou
    False, pokud hra pokračuje.
    """
    oddelovac = "=" * 44
    vyherni_pozice = [
        [0, 1, 2],  # horní řada
        [3, 4, 5],  # prostřední řada
        [6, 7, 8],  # dolní řada
        [0, 3, 6],  # levý sloupec
        [1, 4, 7],  # prostřední sloupec
        [2, 5, 8],  # pravý sloupec
        [0, 4, 8],  # úhlopříčka \
        [2, 4, 6],  # úhlopříčka /
    ]
    for kombinace in vyherni_pozice:
            if all(box[i] == znacka for i in kombinace):
                print(f"{oddelovac}\nCongratulation! Player {znacka} WON!\n{oddelovac}")
                return True
    # Pokud všechna pole jsou obsazena a není výhra, je to remíza.
    if all(p in ["o", "x"] for p in box):
        print(f"{oddelovac}\nGame over! NO WINNER!\n{oddelovac}")
        return True
    return False
            
def hlavni_hra():
    oddelovac = "=" * 44
    pole = "+---+---+---+"
    pole_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    znacka_1 = "o"
    znacka_2 = "x"
    uvitani() 
    hraje_pocitac = pocet_hracu()
    zobraz_herni_plochu(pole_list, pole)
    kolo = 0
    while True:
        if kolo % 2 == 0:
            print(oddelovac)
            tah_hrace(znacka_1, pole_list)
            zobraz_herni_plochu(pole_list, pole)
            kolo += 1
            if kontrola_vyhry(znacka_1, pole_list):
                break
        elif hraje_pocitac:  
            print(oddelovac)
            tah_pocitace(znacka_2,pole_list)
            zobraz_herni_plochu(pole_list, pole)
            kolo += 1
            if kontrola_vyhry(znacka_2, pole_list):
                break
        else:
            print(oddelovac)
            tah_hrace(znacka_2, pole_list)
            zobraz_herni_plochu(pole_list, pole)
            kolo += 1
            if kontrola_vyhry(znacka_2, pole_list):
                break

if __name__ == "__main__":
    hlavni_hra()   
