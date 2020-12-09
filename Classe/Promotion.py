import random


class Promotion:
    def __init__(self, nom):
        self.list_eleves = []
        self.nom = nom
        self.nombre_max = random.randint(11, 15)


    def add_eleve(self, eleve):
        if len(self.list_eleves) < self.nombre_max:
            print(f"{eleve.prenom} a été ajouter a la classe : {self.nom}")
            self.list_eleves.append(eleve)
            print(f"{len(self.list_eleves)}/{self.nombre_max}")
        else:
            print(f"Vous ne pouvez plus ajouter d'eleve a cette classe, nombre eleve max : {self.nombre_max}")
            print(f"{len(self.list_eleves)}/{self.nombre_max}")

    def afficher_promo(self):
        print(f"Classe : {self.nom}")
        for eleve in self.list_eleves:
            print(eleve.nom)
        print(f"Votre promotion est de {len(self.list_eleves)}/{self.nombre_max} élèves")