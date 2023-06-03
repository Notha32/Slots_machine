import numpy

jetons = 100
print("Bienvenue sur la machine à sous DevFruit")
print("Taper 'lancer' pour lancer la machine ou 'stop' pour stopper la machine")

while True:
    a = input("Que souhaitez vous faire : ")
    fruit = ["cerise", "ananas", "orange", "pasteque", "pommes dorées"]
    proba_fruits = [0.25, 0.2, 0.4, 0.1, 0.05]
    hasard = numpy.random.choice(fruit, 3, p=proba_fruits)
    if a.lower() == "lancer":
        jetons = jetons - 10
        print(f"Vous avez ", {jetons}, "jetons")
        print("-"*20)

        print(hasard)

        if hasard[0] == hasard[1] == hasard[2]:
            print(f"Vous avez 3 {hasard[0]}")
            print("-"*20)
            
            if hasard[0] == "orange":
                jetons = jetons+5
                print(f"Vous avez ", {jetons}, "jetons")

            if hasard[0] == "cerise":
                jetons = jetons+15
                print(f"Vous avez ", {jetons}, "jetons")

            if hasard[0] == "ananas":
                jetons = jetons+50
                print(f"Vous avez ", {jetons}, "jetons")

            if hasard[0] == "pasteque":
                jetons = jetons+150
                print(f"Vous avez ", {jetons}, "jetons")

            if hasard[0] =="pommes dorées":
                jetons = jetons+10000
                print(f"jackpot vous avez : ", {jetons}, "jetons")

        elif jetons <= 0:
            print("vous avez perdu, vous n'avez plus d'argent !")
            break
        else:
            print("Perdu")
            print(f"Vous avez ", {jetons}, "jetons")
            print("-"*20)

    elif a.lower() == "stop":
        break

    else:
        print("Entrer une action valide !")
        continue
        
print("Le jeu c'est stopé !")









