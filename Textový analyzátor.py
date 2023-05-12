"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Rostislav Vymazal
email: rostislav.vymazal@centrum.cz
discord: Rostislav V.
"""

# Registrovaní uživatelé
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = [
    """
    Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive 
    topographic feature that rises sharply some 1000 feet above Twin Creek Valley 
    to an elevation of more than 7500 feet above sea level. The butte is located just 
    north of US 30N and the Union Pacific Railroad, which traverse the valley. 
    """
    ,
    """
    At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch 
    Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor 
    and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper 
    buff-to-white beds of the Green River Formation, which are about 300 feet thick.
    """
    ,
    """
    The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish 
    fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, 
    which lie some 100 feet below the top of the butte. The fossils represent several varieties of 
    perch, as well as other freshwater genera and herring similar to those in modern oceans. 
    """,
]

# Registrovaní uživatelé
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

# Hlavička programu
print("----------------------------------------")
print("Vítejte v aplikaci!")
username = input("Uživatelské jméno: ")
password = input("Heslo: ")
print("----------------------------------------")


# Kontrola přihlašovacích údajů
if username in users and users[username] == password:
    print(f"Vítejte v aplikaci, {username}!")
    print(f"Máme {len(TEXTS)} textů k analýze.")
    print("----------------------------------------")


    # Výběr textu uživatelem
    text_index = input("Zadejte číslo od 1 do 3 pro výběr textu: ")
    if text_index.isnumeric():
        text_index = int(text_index)
        if 1 <= text_index <= len(TEXTS):
            text = TEXTS[text_index - 1]
            slova = text.split()

            # Statistiky
            word_count = len(slova)
            titlecase_count = sum(1 for slovo in slova if slovo.istitle())
            uppercase_count = sum(1 for slovo in slova if slovo.isupper())
            lowercase_count = sum(1 for slovo in slova if slovo.islower())
            numeric_count = sum(1 for slovo in slova if slovo.isnumeric())
            numeric_sum = sum(int(slovo) for slovo in slova if slovo.isnumeric())

            # Graf délek slov
            delky_slov = [len(slovo.strip(".,?!")) for slovo in slova]
            statistiky_delky = {}
            for delka in delky_slov:
                if delka in statistiky_delky:
                    statistiky_delky[delka] += 1
                else:
                    statistiky_delky[delka] = 1

            print("----------------------------------------")
            print(f"Ve vybraném textu je {word_count} slov.")
            print(f"Ve vybraném textu je {titlecase_count} slov začínajících velkým písmenem.")
            print(f"Ve vybraném textu je {uppercase_count} slov psaných velkými písmeny.")
            print(f"Ve vybraném textu je {lowercase_count} slov psaných malými písmeny.")
            print(f"Ve vybraném textu je {numeric_count} číselných řetězců.")
            print(f"Součet všech čísel ve vybraném textu je {numeric_sum}.")
            print("----------------------------------------")
            print("DÉLKA|   VÝSKYT   |POČET")
            print("----------------------------------------")
            for length, occurrences in sorted(statistiky_delky.items()):
                bar = "*" * occurrences
                print(f"{length:3}|{bar:14}|{occurrences:2}")
            print("----------------------------------------")

        else:
            print("Neplatné číslo textu. Program ukončen.")
    else:
        print("Neplatný vstup. Program ukončen.")

else:
    print("Neregistrovaný uživatel, ukončení programu.")