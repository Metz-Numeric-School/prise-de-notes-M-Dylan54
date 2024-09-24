nbdedoigtsa=int(input("combien de doigts montre le joueur A ?"))
nbdedoigtsb=int(input("combien de doigts montre le joueur B ?"))
somme=nbdedoigtsa+nbdedoigtsb
if somme%2==0 :
    print("Le joueur A est le gagnant !")
else :
    print("Le joueur B est le gagnant !")
