notefrancais=float(input("Note de francais"))
notemaths=float(input("Note de maths"))
notegeo=float(input("Note de géométrie"))
noteinfo=float(input("Note d'informatique"))
coefffrancais=float(input("coefficient francais"))
coeffmaths=float(input("coefficient maths"))
coeffgeo=float(input("coefficient géométrie"))
coeffinfo=float(input("coefficient informatique"))
sommenotesponderee=((notefrancais*coefffrancais)+(notemaths*coeffmaths)+(notegeo*coeffgeo)+(noteinfo*coeffinfo))
sommecoeff=coefffrancais+coeffmaths+coeffgeo+coeffinfo
moyenne=sommenotesponderee/sommecoeff
print(moyenne)