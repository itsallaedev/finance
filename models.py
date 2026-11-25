class Societe:
    def __init__(self, id_societe, nom, symbole_boursier, secteur, pays):
        self.id_societe = id_societe
        self.nom = nom
        self.symbole_boursier = symbole_boursier
        self.secteur = secteur
        self.pays = pays

    def __repr__(self):
        return f"Societe({self.id_societe}, {self.nom}, {self.symbole_boursier})"
class Bilan:
    def __init__(self, id_societe, annee, chiffre_affaires, resultat_net,
                 actifs_courants, passifs_courants, dettes_totales,
                 capitaux_propres, total_actifs):
        self.id_societe = id_societe
        self.annee = annee
        self.chiffre_affaires = chiffre_affaires
        self.resultat_net = resultat_net
        self.actifs_courants = actifs_courants
        self.passifs_courants = passifs_courants
        self.dettes_totales = dettes_totales
        self.capitaux_propres = capitaux_propres
        self.total_actifs = total_actifs

    def __repr__(self):
        return f"Bilan({self.id_societe}, {self.annee})"


class Cours:
    def __init__(self, id_societe, date_cours, cours_cloture, volume):
        self.id_societe = id_societe
        self.date_cours = date_cours
        self.cours_cloture = cours_cloture
        self.volume = volume

    def __repr__(self):
        return f"Cours({self.id_societe}, {self.date_cours}, {self.cours_cloture})"