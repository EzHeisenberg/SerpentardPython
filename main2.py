from Classe.Ecole import Ecole
from Classe.Promotion import Promotion
from Classe.Eleve import Eleve
from Classe.Professeur import Prof
from Classe.Car import Car



# Declaration d'un ecole
ecole_epsi = Ecole("EPSI")


# Déclaration des professeurs #
prof_python = Prof("MALABRY", "Emmanuel", "Python")
prof_algo = Prof("BRAUX", "Mathias", "Algorithmie")
prof_math = Prof("Robin", "Olivier", "Mathématique")

# Déclaration des classes
promotion_terminal_a = Promotion("Terminal A", 12, prof_algo)
promotion_seconde_b = Promotion("Seconde B", 9, prof_math)
promotion_premiere_c = Promotion("Première C", 14, prof_python)

# Déclaration des élèves
eleve_tom = Eleve("Poyvre","Tom", ecole_epsi.nom_ecole(), False)
eleve_lucas = Eleve("Reteau","Lucas", ecole_epsi.nom_ecole(), False)
eleve_theo = Eleve("Zazou","Théo", ecole_epsi.nom_ecole(), False)
eleve_florian = Eleve("Sinegre","Florian", ecole_epsi.nom_ecole(), False)
eleve_coline = Eleve("Pierre","Coline", ecole_epsi.nom_ecole(), False)
eleve_timote = Eleve("Dasque","Timoté", ecole_epsi.nom_ecole(), False)



# Ajouter les promotions a l'ecole
ecole_epsi.add_promo(promotion_seconde_b)
ecole_epsi.add_promo(promotion_premiere_c)
ecole_epsi.add_promo(promotion_terminal_a)

# Ajout des élèves dans les promoiton
#Terminal A
promotion_terminal_a.add_eleve(eleve_tom)
promotion_terminal_a.add_eleve(eleve_lucas)
promotion_terminal_a.add_eleve(eleve_theo)
promotion_terminal_a.add_eleve(eleve_florian)
promotion_terminal_a.add_eleve(eleve_coline)

eleve_tom.eleve_present()
eleve_theo.eleve_present()
eleve_lucas.eleve_present()
eleve_florian.eleve_present()


#Créer un car
c1 = Car(3)


#Ajout promo dans car
c1.add_passager(promotion_terminal_a)








# Faire l'appel
#prof_algo.faire_appel(promotion_terminal_a)


