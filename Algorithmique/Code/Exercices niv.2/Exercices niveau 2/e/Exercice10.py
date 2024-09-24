tempambiante=float(input("Saisir la température ambiante"))
tempbassin=float(input("Saisir la température du bassin"))
difference=0
if tempambiante>=tempbassin:
    difference=tempambiante-tempbassin
if tempambiante<=tempbassin:
    difference=tempbassin-tempambiante
print(difference, "°C")
if difference<20 or difference>40:
    print("ALAAAAAAAAAAAAAAAAAAAAARME")

