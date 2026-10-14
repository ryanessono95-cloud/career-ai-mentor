matiere = {"nom": "Langage C", "coef": 4, "note": 17}
matiere1 = {"nom": "Analyse", "coef": 3, "note": 16.5}
matiere2= {"nom": "Systeme", "coef": 3, "note": 18}
matiere3 = {"nom": "Proba", "coef": 3, "note": 15.5}
notes =[matiere, matiere1, matiere2, matiere3]
s=0
c=0
for i in range(0,4):
    print(notes[i]) 
    s += notes[i]["note"] * notes[i]["coef"]
    c += notes[i]["coef"]
moyenne = s/c
print("la moyenne est : ",moyenne)
    
