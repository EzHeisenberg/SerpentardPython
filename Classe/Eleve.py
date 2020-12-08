from Classe.Personne import Person


class Eleve(Person):
    def __init__(self, nom, prenom, ecole, est_present):
        super().__init__(nom, prenom)
        self.ecole = ecole
        self.est_present = est_present

    def est_present(self):
        self.est_present = True