class Ecole:
    def __init__(self, nom):
        self.list_promos = []
        self.nom = nom

    def add_promo(self, promo):
        self.list_promos.append(promo)

    def afficher_tout_promo(self):
        for promotion in self.list_promos:
            print(f"Classe : {promotion.nom}")