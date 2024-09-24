a=float(input("saisir la valeur de a"))
b=float(input("saisir la valeur de b"))
if a==0 and b==0:
    x="L'ensemble R"
if a==0 and b!=0:
    x="L'ensemble vide"
if a!=0:
    x=(-b/a)
print("La valeur de x est", x)

