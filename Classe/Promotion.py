class Promotion:
    def __init__(self, nom, prof):
        self.list_eleves = []
        self.nom = nom
        self.prof = prof

    def add_eleve(self, eleve):
        self.list_eleves.append(eleve)

