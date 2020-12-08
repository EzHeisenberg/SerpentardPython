from Classe.Ecole import Ecole
from Classe.Promotion import Promotion
from Classe.Eleve import Eleve
from Classe.Professeur import Prof


############################
## Declaration d'un ecole ##
############################

ecole = Ecole("EPSI")


# Déclaration des professeurs #
prof_python = Prof("MALABRY", "Emmanuel")
prof_algo = Prof("BRAUX", "Mathias")
prof_oracle = Prof("Ontaro", "Phillips")

promotion_b1 = Promotion("B1", prof_python)
promotion_b2 = Promotion("B2", prof_oracle)
promotion_b3 = Promotion("B3", prof_algo)


eleve_tom = Eleve("Poyvre","Tom", ecole.nom_ecole())
eleve_lucas = Eleve("Reteau","Lucas", ecole.nom_ecole())
eleve_theo = Eleve("Zazou","Théo", ecole.nom_ecole())
eleve_florian = Eleve("Sinegre","Florian", ecole.nom_ecole())
eleve_coline = Eleve("Pierre","Coline", ecole.nom_ecole())
eleve_timote = Eleve("Dasque","Timoté", ecole.nom_ecole())
