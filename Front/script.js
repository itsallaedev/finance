let estConnecte = true;

function toggleConnexion() {
    estConnecte = !estConnecte;
    const dot = document.getElementById("onlineDot");
    const status = document.getElementById("userStatus");
    const name = document.getElementById("userName");

    if (estConnecte) {
        dot.classList.remove("offline");
        status.classList.remove("offline");
        name.textContent = "Allae (app_user)";
        status.textContent = "● Connecté (Droits restreints)";
    } else {
        dot.classList.add("offline");
        status.classList.add("offline");
        name.textContent = "Session fermée";
        status.textContent = "● Déconnecté";
    }
}

const societes = [
    {
        nom: "TechNova SAS", secteur: "Technologie", devise: "EUR",
        ca: 1200000, rn: 170400, actifs: 540000, passifs: 291890, dettes: 310000, capitaux: 500000,
        cours: [105.0, 106.5, 108.0, 107.2, 109.5, 111.0, 112.4, 113.8, 115.0, 113.87]
    },
    {
        nom: "AgroVert SA", secteur: "Agroalimentaire", devise: "EUR",
        ca: 850000, rn: 51000, actifs: 320000, passifs: 210000, dettes: 400000, capitaux: 350000,
        cours: [42.0, 41.8, 42.5, 43.0, 42.9, 43.4, 44.1, 43.9, 44.5, 45.1]
    },
    {
        nom: "MedCare Bio", secteur: "Santé", devise: "EUR",
        ca: 2400000, rn: 456000, actifs: 1100000, passifs: 450000, dettes: 280000, capitaux: 950000,
        cours: [210.0, 212.5, 215.0, 214.0, 218.0, 220.5, 219.0, 222.0, 225.0, 228.5]
    },
    {
        nom: "LogiTrans", secteur: "Transport", devise: "EUR",
        ca: 0, rn: -15000, actifs: 100000, passifs: 0, dettes: 300000, capitaux: 150000,
        cours: [60.0, 59.5, 58.0, 57.5, 56.0, 55.8, 55.0, 54.2, 53.5, 52.8]
    }
];

function formatValue(elId, result, isError = false, color = null) {
    const el = document.getElementById(elId);
    if (isError) {
        el.className = "error-text";
        el.textContent = result;
    } else {
        el.className = "kpi-value";
        el.style.color = color || "var(--text-main)";
        el.textContent = result;
    }
}

function afficherResultats() {
    const s = societes[document.getElementById("selectSociete").value];

    document.getElementById("infosSociete").innerHTML =
        `<span class="badge">Secteur : ${s.secteur}</span> <span class="badge">Devise : ${s.devise}</span>`;

    // 1. Marge nette
    if (s.ca === 0) formatValue("marge", "Impossible (CA = 0)", true);
    else formatValue("marge", ((s.rn / s.ca) * 100).toFixed(2) + " %");

    // 2. Liquidité
    if (s.passifs === 0) formatValue("liquidite", "Impossible (Passifs = 0)", true);
    else formatValue("liquidite", (s.actifs / s.passifs).toFixed(2));

    // 3. Endettement
    if (s.capitaux === 0) formatValue("endettement", "Impossible (Capitaux = 0)", true);
    else formatValue("endettement", (s.dettes / s.capitaux).toFixed(2));

    // 4. Rendement
    const debut = s.cours[0], fin = s.cours[s.cours.length - 1];
    const rend = ((fin - debut) / debut) * 100;
    const sign = rend >= 0 ? "+" : "";
    formatValue("rendement", sign + rend.toFixed(2) + " %", false, rend >= 0 ? "#16a34a" : "#dc2626");

    // 5. Moyenne mobile (5 jours)
    const slice = s.cours.slice(-5);
    const mm = slice.reduce((a, b) => a + b, 0) / 5;
    formatValue("moyenneMobile", mm.toFixed(2) + " " + s.devise);
}

afficherResultats();
