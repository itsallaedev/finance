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