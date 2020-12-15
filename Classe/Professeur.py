from Classe.Personne import Person


class Prof(Person):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)


    def faire_appel(self, promotion):
        for eleve in promotion.list_eleves:
            if eleve.est_present:
                print(f"{eleve.prenom}, {eleve.nom} est présent")
            else:
                print(f"\033[35m{eleve.prenom}, {eleve.nom} est absent\033[39m")


    def faire_appel_bus(self, bus):
        for eleve in bus:
            if eleve.dans_bus:
                print(f"{eleve.prenom}, {eleve.nom} est dans le bus")
            else:
                print(f"\033[35m{eleve.prenom}, {eleve.nom} n'est pas dans le bus\033[39m")
