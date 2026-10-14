nom = input("Ton prénom : ")

while True:
    try:
        moyenne = float(input("Ta moyenne sur 20 : "))
    except ValueError:
        print("Erreur : entre un nombre (ex. 13.5).")
        continue
    if 0 <= moyenne <= 20:
        break
    print("Erreur : la moyenne doit être comprise entre 0 et 20.")

if moyenne >= 16:
    mention = "Très bien"
elif moyenne >= 14:
    mention = "Bien"
elif moyenne >= 10:
    mention = "Passable"
else:
    mention = "Ajourné(e)"

print(f"{nom}, ta mention est : {mention}")

for i in range(1, 4):
    print(f"Révision numéro {i}")