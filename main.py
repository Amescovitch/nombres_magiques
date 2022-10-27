import random

print("\nAMESCOVITCH_____________ DEVINETTE DU NOMBRE MAGIQUE______________AMESCOVITCH\n""")

reprendre = True
while reprendre:
    reprendre = False
    def demander_nombre(nb_min, nb_max):
        nombre_int = 0
        while nombre_int == 0:
            nombre_str = input(f"Quel est le nombre magique ?? (entre {nb_min} et {nb_max}): ")
            try:
                nombre_int = int(nombre_str)
            except ValueError:
                print("ERREUR: Vous devez enter un nombre entier. Reéssayez !\n")
            else:
                if not nb_min <= nombre_int <= nb_max:
                    print(f"ERREUR: Le nombre magique est compris entre {nb_min} et {nb_max}. Reéssayer !\n")
                    nombre_int = 0
        return nombre_int


    NOMBRE_MIN = 1
    NOMBRE_MAX = 20
    NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    NB_VIES = 5

    '''nombre = 0
    
    
    vies  = NB_VIES
    while not nombre == NOMBRE_MAGIQUE and vies >0:
        if vies == NB_VIES:
            print(f"Vous avez {vies} vies. C'est parti !!!\n")
        nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    
        if nombre > NOMBRE_MAGIQUE:
            print(f"""Le nombre magique est plus petit !
                             Il vous reste {vies-1} vies.""")
            vies -= 1
        elif nombre < NOMBRE_MAGIQUE:
            print(f"""Le nombre magique est plus grand !
                             Il vous reste {vies - 1} vies.""")
            vies -= 1
        else:
            print("Bravo, vous avez gagné !\n")
    
    if vies == 0:
        print(f"""Vous avez perdu !
                    Le nombre magique était juste: {NOMBRE_MAGIQUE}""")'''

    gagné = False
    vies  = NB_VIES
    for i in range (0, NB_VIES):
        vies = NB_VIES - i
        if vies == NB_VIES:
            print()
            print(f"Vous avez {vies} vies. C'est parti !!!\n")
        nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)

        if nombre > NOMBRE_MAGIQUE:
            print(f"""Le nombre magique est plus petit !
                             Il vous reste {vies-1} vies.""")
        elif nombre < NOMBRE_MAGIQUE:
            print(f"""Le nombre magique est plus grand !
                             Il vous reste {vies - 1} vies.""")
        else:
            print("Bravo, vous avez gagné !")
            gagné = True
            break

    if not gagné:
        print(f"""Vous avez perdu !
                    Le nombre magique était juste: {NOMBRE_MAGIQUE}""")


    reprendre = True if input("\nReprendre la partie (O/N)?? : ").lower() == "o" else False
print("\n____AU REVOIR..............GOOD BYE..............AU REVOIR____")