from Classe.Personne import Person


class Eleve(Person):
    def __init__(self, nom, prenom, ecole, est_present, dans_bus):
        super().__init__(nom, prenom)
        self.ecole = ecole
        self.est_present = est_present
        self.dans_bus = False

    def eleve_present(self):
        self.est_present = True

    def rentre_dans_bus(self):
        self.dans_bus = True