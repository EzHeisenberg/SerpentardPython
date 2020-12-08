class Promotion:
    def __init__(self, nom, nombre_max, prof_principal):
        self.list_eleves = []
        self.nom = nom
        self.nombre_max = nombre_max
        self.prof_principal = prof_principal


    def add_eleve(self, eleve):
        if len(self.list_eleves) < self.nombre_max:
            self.list_eleves.append(eleve)
            print(f"{len(self.list_eleves)}/{self.nombre_max}")
        else:
            print(f"Vous ne pouvez plus ajouter d'eleve a cette classe, nombre eleve max : {self.nombre_max}")


    def afficher_promo(self):
        print(self.list_eleves)
        print(f"Votre promotion est de {len(self.list_eleves)}/{self.nombre_max} élèves")