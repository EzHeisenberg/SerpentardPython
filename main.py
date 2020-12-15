
from Classe.Ecole import Ecole
from Classe.Promotion import Promotion
from Classe.Eleve import Eleve
from Classe.Professeur import Prof
from Classe.Car import Car



print('============================================')
print('=====  Bienvenu sur SchoolCar Manager  =====')
print('============================================')





###################################
#          CREATION ECOLE         #
###################################

ecole_epsi = Ecole("EPSI")

###################################
#               END               #
###################################

prof_classroom_1 = Prof("Braux", "Mathias")
prof_classroom_2 = Prof("Reinold", "Fréderic")
prof_classroom_3 = Prof("Henry", "Guillaume")
prof_1 = Prof("Henry", "Guillaume")
prof_2 = Prof("Gabs", "Maki")
prof_3 = Prof("Vichen", "Bart")
prof_4 = Prof("Palok", "Nicolas")
prof_5 = Prof("Bolid", "Vincent")







###################################
#       CREATION DES CLASSE       #
###################################

print("=====    VOUS DEVEZ CREER 3 CLASSES    =====")
print("=====       CREER VOTRE CLASSE 1       =====")
print("=====        indiquer son NOM :        =====")
print('============================================')
name_classroom1 = input("===== NOM classe 1 : ")
classroom_1 = Promotion(name_classroom1, prof_classroom_1)

print("============================================")
print("=====       CREER VOTRE CLASSE 2       =====")
print("=====        indiquer son NOM :        =====")
print("============================================")

name_classroom2 = input("===== NOM classe 2 : ")
classroom_2 = Promotion(name_classroom2, prof_classroom_2)

print("============================================")
print("=====       CREER VOTRE CLASSE 3       =====")
print("=====        indiquer son NOM :        =====")
print("============================================")
name_classroom3 = input("===== NOM classe 3 : ")
classroom_3 = Promotion(name_classroom3, prof_classroom_3)

###################################
#               END               #
###################################








###################################
#     AJOUT CLASSES DANS ECOLE    #
###################################

ecole_epsi.add_promo(classroom_1)
ecole_epsi.add_promo(classroom_2)
ecole_epsi.add_promo(classroom_3)

###################################
#               END               #
###################################




###################################
#       CREATION DES ELEVES       #
###################################

eleve_1 = Eleve("Reteau", "Lucas", ecole_epsi.nom, True, False)
eleve_2 = Eleve("Poyvre", "tom", ecole_epsi.nom, True, False)
eleve_3 = Eleve("Sinegre", "Florian", ecole_epsi.nom, True, False)
eleve_4 = Eleve("Sekkat", "Rayan", ecole_epsi.nom, True, False)
eleve_5 = Eleve("Pierre", "Coline", ecole_epsi.nom, True, False)
eleve_6 = Eleve("Duval", "Amoryne", ecole_epsi.nom, True, False)
eleve_7 = Eleve("Dupont", "Amandine", ecole_epsi.nom, True, False)
eleve_8 = Eleve("Activia", "Louise", ecole_epsi.nom, True, False)
eleve_9 = Eleve("Valise", "Camille", ecole_epsi.nom, True, False)
eleve_10 = Eleve("Terzi", "Emma", ecole_epsi.nom, False, False)
eleve_11 = Eleve("Thomma", "Iness", ecole_epsi.nom, True, False)
eleve_12 = Eleve("Petit", "Chloe", ecole_epsi.nom, True, False)
eleve_13 = Eleve("Robert", "Sarah", ecole_epsi.nom, True, False)
eleve_14 = Eleve("Vince", "Bertrand", ecole_epsi.nom, True, False)
eleve_15 = Eleve("Bertrand", "Alice", ecole_epsi.nom, False, False)
eleve_16 = Eleve("Martin", "Charlotte", ecole_epsi.nom, True, False)
eleve_17 = Eleve("Scelo", "Nicolas", ecole_epsi.nom, True, False)
eleve_18 = Eleve("Lefevre", "Paul", ecole_epsi.nom, True, False)
eleve_19 = Eleve("Andre", "Martin", ecole_epsi.nom, True, False)
eleve_20 = Eleve("Legrand", "Alban", ecole_epsi.nom, True, False)
eleve_21 = Eleve("Robin", "Arthur", ecole_epsi.nom, True, False)
eleve_22 = Eleve("Clement", "Clement", ecole_epsi.nom, True, False)
eleve_23 = Eleve("Henri", "Golpas", ecole_epsi.nom, False, False)
eleve_24 = Eleve("Roussel", "Matteo", ecole_epsi.nom, True, False)
eleve_25 = Eleve("Haribo", "Kevin", ecole_epsi.nom, True, False)
eleve_26 = Eleve("Marchant", "Mathieu", ecole_epsi.nom, True, False)
eleve_27 = Eleve("Sopra", "Margaux", ecole_epsi.nom, True, False)
eleve_28 = Eleve("Gallard", "Victurine", ecole_epsi.nom, True, False)
eleve_29 = Eleve("Schmit", "Pauline", ecole_epsi.nom, True, False)
eleve_30 = Eleve("Millet", "Noemie", ecole_epsi.nom, True, False)
eleve_31 = Eleve("Zazou","Theo", ecole_epsi.nom, False, False)
eleve_32 = Eleve("Dasque","Timote", ecole_epsi.nom, False, False)
eleve_33 = Eleve("Michelin", "Mathieu", ecole_epsi.nom, True, False)
eleve_34 = Eleve("Bitto", "Caroline", ecole_epsi.nom, True, False)
eleve_35 = Eleve("Pomme", "Pauline", ecole_epsi.nom, True, False)
eleve_36 = Eleve("Peni", "Perrnine", ecole_epsi.nom, True, False)
eleve_37 = Eleve("Jibel","Kylle", ecole_epsi.nom, False, False)
eleve_38 = Eleve("Vinaick","Vachalait", ecole_epsi.nom, False, False)
eleve_39 = Eleve("Pino","Kyo", ecole_epsi.nom, False, False)


liste_eleve_1 = [ eleve_1, eleve_2, eleve_3, eleve_4, eleve_5, eleve_6,  eleve_7,  eleve_8, eleve_9, eleve_10, eleve_11, eleve_12, eleve_13 ]
liste_eleve_2 = [ eleve_14, eleve_15, eleve_16, eleve_17, eleve_18, eleve_19,  eleve_20,  eleve_21, eleve_22, eleve_23, eleve_24, eleve_25, eleve_26 , eleve_38, eleve_39]
liste_eleve_3 = [ eleve_27, eleve_28, eleve_29, eleve_30, eleve_31, eleve_32,  eleve_33,  eleve_34, eleve_35, eleve_36, eleve_37 ]

###################################
#               END               #
###################################









#########################################
#   AJOUT LES ELEVES DANS LES CLASSES   #
#########################################
print("===========================================")
print(f"=====\033[32m           {classroom_1.nom}            \033[39m=====")
print("===========================================")
for liste_1 in liste_eleve_1:
    classroom_1.add_eleve(liste_1)
print("===========================================")
print(f"=====\033[32m           {classroom_2.nom}            \033[39m=====")
print("===========================================")

for liste_2 in liste_eleve_2:
    classroom_2.add_eleve(liste_2)
print("===========================================")
print(f"=====\033[32m           {classroom_3.nom}            \033[39m=====")
print("===========================================")

for liste_3 in liste_eleve_3:
    classroom_3.add_eleve(liste_3)
print("===========================================")
###################################
#               END               #
###################################




#########################################
# CREATION DU MENU POUR CREATION DE BUS #
#########################################


choix_menu = "0"
liste_bus = []
while choix_menu == "0":
    print("===========================================")
    print("=========          MENU           =========")
    print("===========================================")
    print("==     Veuillez choisir une option :     ==")
    print("==      1- Programmer un voyage          ==")
    if liste_bus:
        print("==     2- Ajouter classe dans bus        ==")
        print("==      3- Afficher les voyages          ==")

    print("==    666-         \033[31mquit\033[39m                  ==")



    choix_menu = input("===== choix : ")

    #########################################
    #         PROGRAMMER UN VOYAGE          #
    #########################################
    while choix_menu == "1":


        print("===========================================")
        print("=====  Choisir nombre de BUS a creer  =====")
        print("===========================================")

        nombre_bus = int(input("===== Nombre de BUS : "))
        destination = input(f"===== Saisir la destination des bus  : ")

        i = 1
        while i < nombre_bus + 1:
            nom = input(f"==== Veuillez saisir un nom pour le car n°{i} : ")
            max = int(input(f"==== Veuillez saisir un maximum de place pour le car n°{i} : "))
            print("===========================================")

            globals()[f"car{i}"] = Car(nom, max, ecole_epsi.nom, destination)
            liste_bus.append(globals()[f"car{i}"])

            i = i + 1


        print("=====           LISTE DE BUS          =====")
        print("===========================================")
        print("\033[32mN°    \033[0m|   \033[33mNOM BUS   \033[0m|   \033[35mMAX PLACE   \033[0m|\033[36m   DÉPART   \033[0m|\033[31m   ARRIVÉE   \033[0m")
        i = 1
        while i < nombre_bus + 1:
            print(f"\033[32m n°{i}",
                  "\033[0m   |   \033[33m", globals()[f"car{i}"].nom,
                  "\033[0m   |   \033[35m", globals()[f"car{i}"].place_max,
                  "\033[0m   |   \033[36m", globals()[f"car{i}"].depart,
                  "\033[0m   |   \033[31m", globals()[f"car{i}"].arrive, "\033[0m")
            i = i + 1
        print("=====         LISTE DE ClASSE         =====")
        print(f" \033[32m 1- {classroom_1.nom} \033[0m")
        print(f" \033[32m 2- {classroom_2.nom} \033[0m")
        print(f" \033[32m 3- {classroom_3.nom} \033[0m")

        choix_menu = "0"

    ###################################
    #               END               #
    ###################################






    #########################################
    #         AJOUTER ELEVE DANS BUS        #
    #########################################
    while choix_menu == "2":

        # si la liste des bus est remplit, sinon on demande a en emplir une
        if liste_bus:
            print("===========================================")
            print("=========  AJOUT CLASSE DANS BUS  =========")
            print("===========================================")

            choix_bus = int(input("===== Choix du n° du bus : "))
            choix_classroom = int(input("===== Choix de la classe : "))
            while choix_bus > 0 and choix_bus <= nombre_bus and choix_classroom > 0 and choix_classroom <= 3:


                bus_choisi = globals()[f"car{choix_bus}"]
                if choix_classroom == 1:
                    bus_choisi.add_passager(classroom_1)
                elif choix_classroom == 2:
                    bus_choisi.add_passager(classroom_2)
                elif choix_classroom == 3:
                    bus_choisi.add_passager(classroom_3)

                choix_bus = 0
                choix_classroom = 0
                choix_menu = "0"




        else:
            print("===========================================")
            print("=== \033[31mVOUS DEVEZ DABORD PROGRAMMER UN BUS\033[39m ===")
            choix_menu = "0"

    ###################################
    #               END               #
    ###################################

    #########################################
    #         AFFICHEZ BUS PROGRAMME        #
    #########################################
    while choix_menu == "3":

        # si la liste des bus est remplit, sinon on demande a en emplir une
        if liste_bus:
            print("=====           LISTE DE BUS          =====")
            print("===========================================")
            print(
                "\033[32mN°    \033[0m|   \033[33mNOM BUS   \033[0m|   \033[35mMAX PLACE   \033[0m|\033[36m   DÉPART   \033[0m|\033[31m   ARRIVÉE   \033[0m")
            i = 1
            while i < nombre_bus + 1:
                print(f"\033[32m n°{i}",
                      "\033[0m   |   \033[33m", globals()[f"car{i}"].nom,
                      "\033[0m   |   \033[35m", globals()[f"car{i}"].place_max,
                      "\033[0m   |   \033[36m", globals()[f"car{i}"].depart,
                      "\033[0m   |   \033[31m", globals()[f"car{i}"].arrive, "\033[0m")
                i = i + 1

            choix_menu = "0"


        else:
            print("===========================================")
            print("==  \033[31mVOUSDEVEZ DABORD PROGRAMMER VOYAGE\033[39m   ==")
            choix_menu = "0"

    ###################################
    #               END               #
    ###################################














    if choix_menu == "666":
        print("===========================================")
        print("=========        A BIENTOT        =========")
        print("===========================================")
        exit()









































