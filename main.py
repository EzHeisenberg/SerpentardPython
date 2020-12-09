from Classe.Ecole import Ecole
from Classe.Promotion import Promotion
from Classe.Eleve import Eleve
from Classe.Professeur import Prof
from Classe.Car import Car




print('============================================')
print('====== Bienvenu sur SchoolCar Manager ======')
print('============================================')
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







# CRÉATION DES PROF #

prof_python = Prof("MALABRY", "Emmanuel", "Python")
prof_algo = Prof("BRAUX", "Mathias", "Algorithmie")
prof_math = Prof("Robin", "Olivier", "Mathématique")



# CREATION DES ELEVES #










































# Declaration d'un ecole



# Déclaration des professeurs







# Déclaration des élèves
eleve_tom = Eleve("Poyvre","Tom", ecole_epsi.nom_ecole(), False)
eleve_lucas = Eleve("Reteau","Lucas", ecole_epsi.nom_ecole(), False)
eleve_theo = Eleve("Zazou","Théo", ecole_epsi.nom_ecole(), False)
eleve_florian = Eleve("Sinegre","Florian", ecole_epsi.nom_ecole(), False)
eleve_coline = Eleve("Pierre","Coline", ecole_epsi.nom_ecole(), False)
eleve_timote = Eleve("Dasque","Timoté", ecole_epsi.nom_ecole(), False)






#Créer un car
