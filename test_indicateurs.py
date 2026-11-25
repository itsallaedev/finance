from indicateurs import (
    marge_nette,
    ratio_liquidite,
    ratio_endettement,
    ratio_rendement,
)

# Données fictives
chiffre_affaires = 200000
resultat_net = 20000
actifs_courants = 60000
passifs_courants = 30000
dettes_totales = 90000
capitaux_propres = 60000
total_actifs = 150000

# Calcul des indicateurs
print("Marge nette :", marge_nette(resultat_net, chiffre_affaires), "%")
print("Liquidité :", ratio_liquidite(actifs_courants, passifs_courants))
print("Endettement :", ratio_endettement(dettes_totales, capitaux_propres))
print("Ratio de rendement :", ratio_rendement(100, 110), "%")

# Vérification manuelle des résultats attendus
assert marge_nette(resultat_net, chiffre_affaires) == 10.0
assert ratio_liquidite(actifs_courants, passifs_courants) == 2.0
assert ratio_endettement(dettes_totales, capitaux_propres) == 1.5
assert round(ratio_rendement(100, 110), 2) == 10.0

print("Tous les tests sont réussis !")
