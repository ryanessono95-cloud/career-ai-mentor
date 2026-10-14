matieres = [
    {"nom": "Langage C", "coef": 4, "note": 17},
    {"nom": "Analyse", "coef": 3, "note": 16.5},
    {"nom": "Système", "coef": 3, "note": 18},
    {"nom": "Probabilités", "coef": 3, "note": 15.5},
]

somme_ponderee = 0
somme_coefs = 0

for matiere in matieres:
    print(f"{matiere['nom']} : {matiere['note']} (coef {matiere['coef']})")
    somme_ponderee += matiere["note"] * matiere["coef"]
    somme_coefs += matiere["coef"]

moyenne = somme_ponderee / somme_coefs
print(f"Moyenne pondérée : {moyenne:.2f}")