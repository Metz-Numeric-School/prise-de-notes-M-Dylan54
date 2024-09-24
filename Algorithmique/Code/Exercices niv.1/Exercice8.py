prixHT=float(input("quel est le prix du produit HT en euros?"))
quantité=float(input("combien en voulez-vous?"))
commande=prixHT*quantité
print(commande,"€")
print("La commande bénéficie d'une remise de 15%, cette dernière s'élève donc à")
remise=commande*0.85
print(remise,"€")
TVA=float(1.2)
print("Le prix TTC est finalement de")
print(remise*TVA,"€")
