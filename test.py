from inndatakontroll import Inndatakontroll
ik = Inndatakontroll()
#Generell funksjon for å teste metodene
def testMetode(testnavn, tester, metode):
    print("----",testnavn,"----")
    ok = True
    for test in tester:
        print(("Test: {} //Forventet resultat: {} // Faktisk resultat:{}").format(test[0],test[1],metode(test[0])))
        if metode(test[0]) != test[1]:
            ok = False     
    if not ok:
        print("Metoden gir ikke riktig resultat i alle test-caser")
    else:
        print("Metoden gir riktig resultat i alle test-caser")
    print("----",testnavn,"ferdig ----")   
#Sjekk om et tall er et heltall
testnavn = "Sjekke om et tall (float/int) er et heltall"
heltall_tester = [(5,True),(60,True),(10.0,True),(-5,True),(-4.0,True),(3.000,True),(13.4,False),(-5.1,False),("4",False),("14.8",False)]
# testMetode(testnavn, heltall_tester, ik.numIsInteger)



tekst = 15.8
print(ik.sjekkMinStringLengde(tekst,5))

