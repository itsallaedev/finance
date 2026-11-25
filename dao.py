from db import get_connection
from models import Societe


def get_societe_by_id(id_societe):
    connexion = get_connection()
    try:
        with connexion.cursor() as curseur:
            curseur.execute(
                "SELECT id_societe, nom, symbole_boursier, secteur, pays "
                "FROM societe WHERE id_societe = %s",
                (id_societe,),
            )
            ligne = curseur.fetchone()
            if ligne is None:
                return None
            return Societe(**ligne)
    finally:
        connexion.close()
from models import Bilan, Cours

def get_latest_bilan(id_societe):
    connexion = get_connection()
    try:
        with connexion.cursor() as curseur:
            curseur.execute(
                "SELECT id_societe, annee, chiffre_affaires, resultat_net, "
                "actifs_courants, passifs_courants, dettes_totales, "
                "capitaux_propres, total_actifs "
                "FROM bilan WHERE id_societe = %s "
                "ORDER BY annee DESC LIMIT 1",
                (id_societe,),
            )
            ligne = curseur.fetchone()
            if ligne is None:
                return None
            return Bilan(**ligne)
    finally:
        connexion.close()

def get_cours_by_societe(id_societe):
    connexion = get_connection()
    try:
        with connexion.cursor() as curseur:
            curseur.execute(
                "SELECT id_societe, date_cours, cours_cloture, volume "
                "FROM cours WHERE id_societe = %s "
                "ORDER BY date_cours ASC",
                (id_societe,),
            )
            return [Cours(**ligne) for ligne in curseur.fetchall()]
    finally:
        connexion.close()

def get_societe_by_symbole(symbole_boursier):
    connexion = get_connection()
    try:
        with connexion.cursor() as curseur:
            curseur.execute(
                "SELECT id_societe, nom, symbole_boursier, secteur, pays "
                "FROM societe WHERE symbole_boursier = %s",
                (symbole_boursier,),
            )
            ligne = curseur.fetchone()
            if ligne is None:
                return None
            return Societe(**ligne)
    finally:
        connexion.close()
