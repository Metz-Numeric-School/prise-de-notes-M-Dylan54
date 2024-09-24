TTC=float(input("Saisir le montant TTC"))
if TTC>=500 and TTC<1000:
    print(TTC*0.98)
if TTC>=1000 and TTC<=2000:
    print(TTC*0.95)
if TTC>2000:
    print(TTC*0.9)
else:
    print(TTC)