notefr=float(input("note de francais"))
notemath=float(input("note de math"))
noteinfo=float(input("note d'info"))
notegeo=float(input("note de géo"))
moyenne=(notefr+notemath+noteinfo+notegeo)/4
print(moyenne)
if moyenne>=16 and moyenne<=20:
    print("Mention Très bien")
if moyenne>=12 and moyenne<16:
    print("Mention bien")
if moyenne>=8 and moyenne<12:
    print("Mention Assez bien")
if moyenne>=4 and moyenne<8:
    print("Mention Insuffisant")
if moyenne>=0 and moyenne<4:
    print("Mention Nul")
