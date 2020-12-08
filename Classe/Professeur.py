from Classe.Personne import Person


class Prof(Person):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.salaire = 1000

    def changer_salaire(self, salaire):
        self.salaire = salaire
