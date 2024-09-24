prixHT=float(input("Saisir le prix ht du produit"))
print("Pour une TVA de 5,5%, saisissez 1")
print("Pour une TVA de 19,6%, saisissez 2")
print("Pour une TVA de 33%, saisissez 3")
TVA=float(input("Faites votre choix, quel code choisissez-vous ?"))
if TVA==1:
    print(prixHT*1.055)
if TVA==2:
    print(prixHT*1.196)
if TVA==3:
    print(prixHT*1.33)