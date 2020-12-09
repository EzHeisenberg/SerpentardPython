from Classe.Ecole import Ecole
from Classe.Promotion import Promotion
from Classe.Eleve import Eleve
from Classe.Professeur import Prof
from Classe.Car import Car

stay = "oui"
while stay == "oui":
    print("===========================================")
    print("=========          MENU           =========")
    print("===========================================")
    print("== Veuillez choisir une option :         ==")
    print("==   1- Programmer un voyage             ==")
    print("==   2- Afficher les voyages             ==")
    print("==   3- Saisir une promotion             ==")

    choix = 0

    while ((choix < 1) or (choix > 3)):
        choix = input("     Votre choix : ")
        choix = int(choix)

    if choix == 1:
        # print("choix 1")
        nom = input("Veuillez saisir un nom pour le car: ")
        car1 = Car(nom, 15, "école", "Marseille")

        print("")
        print("Voici la liste des différentes promotions d'élèves:")
        print(" 1- Terminale A")
        print(" 2- Terminale B")
        print(" 3- Terminale C")

        ajouter = "oui"
        while ajouter == "oui":
            promo = 0
            while ((promo < 1) or (promo > 3)):
                promo = input(f"Veuillez choisir des passagers pour le {car1.nom} (1, 2 ou 3): ")
                promo = int(promo)

            if promo == 1:
                Car.add_passager(promotion_terminal_a)
            elif promo == 2:
                Car.add_passager(promotion_seconde_b)
            else:
                Car.add_passager(promotion_premiere_c)

            ajouter = input("Voulez-vous ajouter une autre promotion ? (oui/non)")

        print("Voulez-vous revenir au menu ? (oui/non) ")
        stay = input()

    elif choix == 2:
        #print("choix 2")
        print("Voici les différents cars au départ: ")
        print(f"  -> {car1.nom}")
        print(f"        - {car1.list_passager}")

        print("Voulez-vous revenir au menu ? (oui/non) ")
        stay = input()

    else:
        #print("choix 3")
        # Déclaration des professeurs
        prof_python = Prof("MALABRY", "Emmanuel", "Python")
        prof_algo = Prof("BRAUX", "Mathias", "Algorithmie")
        prof_math = Prof("Robin", "Olivier", "Mathématique")
        # Déclaration des classes
        promotion_terminal_a = Promotion("Terminal A", 12, prof_algo)
        promotion_seconde_b = Promotion("Seconde B", 9, prof_math)
        promotion_premiere_c = Promotion("Première C", 14, prof_python)

        print("Voulez-vous revenir au menu ? (oui/non) ")
        stay = input()

