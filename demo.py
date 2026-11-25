from dao import get_societe_by_id

print(get_societe_by_id(1))
print(get_societe_by_id(999))
from dao import get_societe_by_symbole, get_latest_bilan, get_cours_by_societe
from indicateurs import (
    marge_nette,
    ratio_liquidite,
    ratio_endettement,
    moyenne_mobile,
)

FENETRE = 5  # moving average window (days)

def afficher_societe(societe):
    print("=" * 50)
    print(f"{societe.nom} ({societe.symbole_boursier})")
    print(f"Sector: {societe.secteur} | Country: {societe.pays}")


def afficher_indicateurs(id_societe):
    bilan = get_latest_bilan(id_societe)
    print("=" * 50)
    if bilan is None:
        print("No balance sheet available for this company.")
        return
    print(f"Indicators for {bilan.annee}")
    print("Net margin     :", marge_nette(bilan.resultat_net, bilan.chiffre_affaires), "%")
    print("Current ratio  :", ratio_liquidite(bilan.actifs_courants, bilan.passifs_courants))
    print("Debt-to-equity :", ratio_endettement(bilan.dettes_totales, bilan.capitaux_propres))


def afficher_moyenne_mobile(id_societe):
    cours = get_cours_by_societe(id_societe)
    prix = [float(c.cours_cloture) for c in cours]
    moyennes = moyenne_mobile(prix, FENETRE)
    print("=" * 50)
    if not moyennes:
        print(f"Not enough prices for a {FENETRE}-day moving average.")
        return
    print(f"{FENETRE}-day moving average ({len(prix)} prices)")
    for c, moyenne in zip(cours[FENETRE - 1:], moyennes):
        print(f"{c.date_cours} : {moyenne}")


def main():
    print("Finance demo - type a ticker symbol (e.g. CYBR), or 'q' to quit.")
    while True:
        symbole = input("\nTicker symbol: ").strip().upper()
        if symbole in ("Q", "QUIT", "EXIT"):
            break
        if not symbole:
            continue

        societe = get_societe_by_symbole(symbole)
        if societe is None:
            print(f"No company found for '{symbole}'.")
            continue

        afficher_societe(societe)
        afficher_indicateurs(societe.id_societe)
        afficher_moyenne_mobile(societe.id_societe)


if __name__ == "__main__":
    main()