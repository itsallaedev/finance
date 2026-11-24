class Societe:
    def __init__(self, id_societe, nom, symbole_boursier, secteur, pays):
        self.id_societe = id_societe
        self.nom = nom
        self.symbole_boursier = symbole_boursier
        self.secteur = secteur
        self.pays = pays

    def __repr__(self):
        return f"Societe({self.id_societe}, {self.nom}, {self.symbole_boursier})"