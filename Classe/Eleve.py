from Classe.Personne import Person


class Eleve(Person):
    def __init__(self, nom, prenom, ecole):
        super().__init__(nom, prenom)
        self.ecole = ecole
