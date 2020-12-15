import random


class Promotion:
    def __init__(self, nom, prof_ref):
        self.list_eleves = []
        self.nom = nom
        self.nombre_max = random.randint(11, 15)
        self.prof_ref = prof_ref


    def add_eleve(self, eleve):
        if len(self.list_eleves) < self.nombre_max:
            self.list_eleves.append(eleve)
            print(f"\033[32m{eleve.prenom} {eleve.nom},\033[0m a été ajouter a la classe")

        else:
            print(f"\033[31mVous ne pouvez plus ajouter d'eleve\033[0m a cette classe, nombre eleve max : {len(self.list_eleves)}/{self.nombre_max}")



    def afficher_promo(self):
        print("===========================================")
        print(f"==== Classe : {self.nom} : {len(self.list_eleves)}/{self.nombre_max} ====")
        for eleve in self.list_eleves:
            print(f"{eleve.nom}, {eleve.prenom}")
        print(f"==== Professeur Référant : {self.prof_ref} ====")
        print("===========================================")
