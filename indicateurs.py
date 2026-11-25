def marge_nette(resultat_net, chiffre_affaires):
    """Calcule la marge nette en pourcentage."""
    if chiffre_affaires == 0:
        return None

    return round((resultat_net / chiffre_affaires) * 100, 2)


def ratio_liquidite(actifs_courants, passifs_courants):
    """Calcule le ratio de liquidité générale."""
    if passifs_courants == 0:
        return None

    return round(actifs_courants / passifs_courants, 2)


def ratio_endettement(dettes_totales, capitaux_propres):
    """Calcule le ratio d'endettement."""
    if capitaux_propres == 0:
        return None

    return round(dettes_totales / capitaux_propres, 2)


def ratio_rendement(cours_debut, cours_fin):
    """Calcule le rendement boursier en pourcentage."""
    if cours_debut == 0:
        return None

    return round(((cours_fin - cours_debut) / cours_debut) * 100, 2)


