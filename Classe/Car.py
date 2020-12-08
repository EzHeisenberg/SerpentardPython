from Classe.Eleve import Eleve

class Car:
    def __init__(self, place_max):
        self.list_passager = []
        self.nombre_place_max = place_max

    def add_passager(self, promotion):
        for eleve in promotion.list_eleves:
            if eleve.est_present == True and len(self.list_passager) < self.nombre_place_max:
                self.list_passager.append(eleve)
                print(f"{eleve.nom} est rentré dans le bus")
            elif eleve.est_present == False :
                print(f"{eleve.nom} est absent")
            else :
                print(f"{eleve.nom}, n'a pas pu rentré dans le bus, il n'y a plus de place")

        print(f"{len(self.list_passager)}/{self.nombre_place_max}")