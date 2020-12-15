from Classe.Eleve import Eleve
from Classe.Promotion import Promotion

class Car:
    def __init__(self, nom, place_max, depart, arrive):
        self.list_passager = []
        self.list_promotion = []
        self.max_promotion = 3
        self.nom = nom
        self.place_max = place_max
        self.depart = depart
        self.arrive = arrive

    def add_passager(self, promotion):
        if len(self.list_promotion) >= self.max_promotion:
            print(f"Imposible d'ajouter la classe de {promotion.nom} car le bus n'accepte {self.max_promotion} promotion")
        else:
            for eleve in promotion.list_eleves:
                if eleve.est_present == True and len(self.list_passager) < self.place_max and len(self.list_promotion) < self.max_promotion:
                    if eleve.dans_bus == False:
                        self.list_passager.append(eleve)
                        print(f"{eleve.prenom}, {eleve.nom} est rentré dans le bus {self.nom}")
                    else:
                        print(f"\033[31m{eleve.prenom}, {eleve.nom} est déja rentré dans un bus\033[39m")

                elif eleve.est_present == False :
                    print(f"\033[35m{eleve.prenom}, {eleve.nom} est absent\033[39m")

                else:
                    print(f"\033[31m{eleve.prenom}, {eleve.nom}, n'a pas pu rentré dans le bus, il n'y a plus de place\033[39m")


        if len(self.list_promotion) < self.max_promotion:
            self.list_promotion.append(promotion)

        print(f"{len(self.list_promotion)}/{self.max_promotion} promotion")
        print(f"{len(self.list_passager)}/{self.place_max} places")



    def partir(self):
        if len(self.list_passager) > 10 and len(self.list_promotion) >= self.max_promotion:
            print(f"Le car est parti de {self.depart} et arrive en direction de {self.arrive}")
        else:
            print(f"le car ne peut pas partir car il y a moins de 10 personnes : {len(self.list_passager)}/{self.place_max} places")


    def afficher_eleves(self):
        for eleve in self.list_passager:
            print(f"        - {eleve.nom}, {eleve.prenom}")