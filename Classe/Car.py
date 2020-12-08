class Car:
    def __init__(self, place_max):
        self.list_passager = []
        self.nombre_place_max = place_max

    def add_passager(self, promotion):
        for eleve in promotion.list_eleves:
            if eleve.est_present == True:
                self.list_passager.append(eleve)
