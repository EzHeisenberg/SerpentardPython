import random


class Promotion:
    def __init__(self, nom):
        self.list_eleves = []
        self.nom = nom
        self.nombre_max = random.randint(11, 15)


    def add_eleve(self, eleve):
        if len(self.list_eleves) < self.nombre_max:
            self.list_eleves.append(eleve)
            print(f"{eleve.prenom} a été ajouter a la classe : {self.nom}")

        else:
            print("===========================================")
            print(f"Vous ne pouvez plus ajouter d'eleve a cette classe, nombre eleve max : {len(self.list_eleves)}/{self.nombre_max}")
            print("===========================================")



    def afficher_promo(self):
        print("===========================================")
        print(f"==== Classe : {self.nom} : {len(self.list_eleves)}/{self.nombre_max} ====")
        for eleve in self.list_eleves:
            print(f"{eleve.nom}, {eleve.prenom}")
        print("===========================================")
