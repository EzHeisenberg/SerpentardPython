from Classe.Ecole import Ecole
from Classe.Promotion import Promotion
from Classe.Eleve import Eleve
from Classe.Professeur import Prof
from Classe.Car import Car
import os

print("===========================================")
print("===== Bienvenue sur SchoolCar Manager =====")
print("===========================================")
print("")
# CRÉATION DE L'ÉCOLE #

ecole_epsi = Ecole("EPSI")

###################################
#               END               #
###################################


# CREATION DES CLASSE #

print("**** CRÉER VOTRE CLASSE 1 *** ")
print("**** indiquer son NOM : *** ")
name_classroom1 = input("nom classe : ")
print("-------------------------------------------")

classroom_1 = Promotion(name_classroom1)

print("**** CRÉER VOTRE CLASSE 2 *** ")
print("**** indiquer son NOM : *** ")
name_classroom2 = input("nom classe : ")
print("-------------------------------------------")
classroom_2 = Promotion(name_classroom2)



print("**** CRÉER VOTRE CLASSE 3 *** ")
print("**** indiquer son NOM : *** ")
name_classroom3 = input("nom classe : ")
print("-------------------------------------------")
classroom_3 = Promotion(name_classroom3)

###################################
#               END               #
###################################

ecole_epsi.add_promo(classroom_1)
ecole_epsi.add_promo(classroom_2)
ecole_epsi.add_promo(classroom_3)

ecole_epsi.afficher_tout_promo()


eleve_1 = Eleve("Reteau", "Lucas", ecole_epsi.nom_ecole(), True)
eleve_2 = Eleve("Poyvre", "tom", ecole_epsi.nom_ecole(), True)
eleve_3 = Eleve("Sinegre", "Florian", ecole_epsi.nom_ecole(), True)
eleve_4 = Eleve("Sekkat", "Rayan", ecole_epsi.nom_ecole(), True)
eleve_5 = Eleve("Pierre", "Coline", ecole_epsi.nom_ecole(), True)
eleve_6 = Eleve("Duval", "Amoryne", ecole_epsi.nom_ecole(), True)
eleve_7 = Eleve("Dupont", "Amandine", ecole_epsi.nom_ecole(), True)
eleve_8 = Eleve("Activia", "Louise", ecole_epsi.nom_ecole(), True)
eleve_9 = Eleve("Valise", "Camille", ecole_epsi.nom_ecole(), True)
eleve_10 = Eleve("Terzi", "Emma", ecole_epsi.nom_ecole(), True)
eleve_11 = Eleve("Thomma", "Iness", ecole_epsi.nom_ecole(), True)
eleve_12 = Eleve("Petit", "Chloé", ecole_epsi.nom_ecole(), True)
eleve_13 = Eleve("Robert", "Sarah", ecole_epsi.nom_ecole(), True)
eleve_14 = Eleve("Vince", "Bertrand", ecole_epsi.nom_ecole(), True)
eleve_15 = Eleve("Bertrand", "Alice", ecole_epsi.nom_ecole(), True)
eleve_16 = Eleve("Martin", "Charlotte", ecole_epsi.nom_ecole(), True)
eleve_17 = Eleve("Scelo", "Nicolas", ecole_epsi.nom_ecole(), True)
eleve_18 = Eleve("Lefevre", "Paul", ecole_epsi.nom_ecole(), True)
eleve_19 = Eleve("Andre", "Martin", ecole_epsi.nom_ecole(), True)
eleve_20 = Eleve("Legrand", "Alban", ecole_epsi.nom_ecole(), True)
eleve_21 = Eleve("Robin", "Arthur", ecole_epsi.nom_ecole(), True)
eleve_22 = Eleve("Clement", "Clement", ecole_epsi.nom_ecole(), True)
eleve_23 = Eleve("Henri", "Golpas", ecole_epsi.nom_ecole(), True)
eleve_24 = Eleve("Roussel", "Matteo", ecole_epsi.nom_ecole(), True)
eleve_25 = Eleve("Haribo", "Kevin", ecole_epsi.nom_ecole(), True)
eleve_26 = Eleve("Marchant", "Mathieu", ecole_epsi.nom_ecole(), True)
eleve_27 = Eleve("Sopra", "Margaux", ecole_epsi.nom_ecole(), True)
eleve_28 = Eleve("Gallard", "Victurine", ecole_epsi.nom_ecole(), True)
eleve_29 = Eleve("Schmit", "Pauline", ecole_epsi.nom_ecole(), True)
eleve_30 = Eleve("Millet", "Noémie", ecole_epsi.nom_ecole(), True)
eleve_31 = Eleve("Zazou","Théo", ecole_epsi.nom_ecole(), False)
eleve_32 = Eleve("Dasque","Timoté", ecole_epsi.nom_ecole(), False)
eleve_33 = Eleve("Michelin", "Mathieur", ecole_epsi.nom_ecole(), True)
eleve_34 = Eleve("Bitto", "Caroline", ecole_epsi.nom_ecole(), True)
eleve_35 = Eleve("Pomme", "Pauline", ecole_epsi.nom_ecole(), True)
eleve_36 = Eleve("Peni", "Perrnine", ecole_epsi.nom_ecole(), True)
eleve_37 = Eleve("Jibel","Kylle", ecole_epsi.nom_ecole(), False)
eleve_38 = Eleve("Vinaick","Vachalait", ecole_epsi.nom_ecole(), False)
eleve_39 = Eleve("Pino","Kyo", ecole_epsi.nom_ecole(), False)


liste_eleve_1 = [ eleve_1, eleve_2, eleve_3, eleve_4, eleve_5, eleve_6,  eleve_7,  eleve_8, eleve_9, eleve_10, eleve_11, eleve_12, eleve_13 ]
liste_eleve_2 = [ eleve_14, eleve_15, eleve_16, eleve_17, eleve_18, eleve_19,  eleve_20,  eleve_21, eleve_22, eleve_23, eleve_24, eleve_25, eleve_26 , eleve_38, eleve_39]
liste_eleve_3 = [ eleve_27, eleve_28, eleve_29, eleve_30, eleve_31, eleve_32,  eleve_33,  eleve_34, eleve_35, eleve_36, eleve_37 ]

# AJOUTE DE LA LISTE ELEVE UN A LA PROMO
for liste_1 in liste_eleve_1:
    classroom_1.add_eleve(liste_1)

 # AJOUTE DE LA LISTE ELEVE UN A LA PROMO
for liste_2 in liste_eleve_2:
    classroom_2.add_eleve(liste_2)

# AJOUTE DE LA LISTE ELEVE UN A LA PROMO
for liste_3 in liste_eleve_3:
    classroom_3.add_eleve(liste_3)


classroom_1.afficher_promo()
classroom_2.afficher_promo()
classroom_3.afficher_promo()


os.system('cls')

stay = "oui"
while stay == "oui":
    print("===========================================")
    print("=========          MENU           =========")
    print("===========================================")
    print("== Veuillez choisir une option :         ==")
    print("==   1- Programmer un voyage             ==")
    print("==   2- Afficher les voyages             ==")


    choix = 0

    while (choix < 1) or (choix > 2):
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
                Car.add_passager(car1, classroom_1)
            elif promo == 2:
                Car.add_passager(car1, classroom_2)
            else:
                Car.add_passager(car1, classroom_3)

            ajouter = input("Voulez-vous ajouter une autre promotion ? (oui/non)")

        print("Voulez-vous revenir au menu ? (oui/non) ")
        stay = input()

    else:
        #print("choix 2")
        print("Voici les différents cars au départ: ")
        print(f"  --> {car1.nom}")
        car1.afficher_eleves()

        print("Voulez-vous revenir au menu ? (oui/non) ")
        stay = input()


