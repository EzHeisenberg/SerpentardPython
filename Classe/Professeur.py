from Classe.Personne import Person


class Prof(Person):
    def __init__(self, nom, prenom, matiere):
        super().__init__(nom, prenom)
        self.matiere = matiere


    def faire_appel(self, promotion):
        for eleve in promotion.list_eleves:
            if eleve.est_present:
                print(f"{eleve.prenom}, {eleve.nom} est présent")
            else:
                print(f"{eleve.prenom}, {eleve.nom} n'est pas présent")
