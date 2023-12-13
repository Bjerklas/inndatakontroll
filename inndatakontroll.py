class Inndatakontroll:
    #Ingen eksplisitt definert constructor for nå
    #Sjekk om et tall er et heltall
    def numIsInteger(self,number):
        try:
            return number.is_integer()
        except AttributeError:
            return False
    #TODO: Sjekke om en string representerer et tall
    #TODO: Sjekke om en string har en minimumslengde
    #TODO: Sjekke om en string har en maksimumslengde
    """ 
        Tanke: Kanskje de to siste der kan kombineres?
        Men da må man kunne definere i input hvis man ikke vil ha
        minimum eller maksimum, f.eks. ved å sette -1 for en av verdiene
    """
    #TODO: Sjekke at en dato er i fremtiden
    #TODO: Sjekke at en dato er i fortiden
    #TODO: Sjekke at en fødselsdato gir en alder som er større enn et tall, f.eks. over 18
    #TODO: Sjekke at en fødselsdato gir en alder som er mindre enn et tall, f.eks. under 18
    #Lance claimer passord
    #TODO: Passord1: Sjekke at et passord har minst X tegn og inneholder små og store bokstaver
    #TODO: Passord2: Sjekke at et passord tilfredsstiller passord1 og inneholder tall
    #TODO: Passord3: Sjekke at et passord tilfredsstiller passord2 og inneholder spesielle symboler
    #TODO: Sjekke at en string kun inneholder bokstaver, og ikke andre symboler eller tall
    #TODO: Sjekke om en string kun har store bokstaver
    #TODO: SJekke om en string kun har små bokstaver
    #TODO: Sjekke at en string er ett ord, hvor første bokstav er stor og alle andre er små
    #TODO: Sjekke at en setning er gyldig
    """En setning er gyldig hvis den har stor forbokstav og eller små bokstaver. Videre må den bestå av 
       ord som er satt sammen (bokstaver) og mellomrom. Det går også an å ha med tall i en setning
       så lenge tallene står alene med mellomrom mellom seg. 
       En setning kan også ha bindestreker og komma på slutten av ord,
       også avslutter den  med et terminalsymbol (punktum, utropstegn, spørsmålstegn)
    """
    #TODO: Sjekke at en tekst kun består av gyldige setninger
    #TODO: Sjekke at en string ikke inneholder visse symboler som kan defineres i input
    #TODO: Navn1: Sjekke at en string kun er ett ord, f.eks. bare et fornavn. Kan bare være bokstaver
    #TODO: Navn2: Sjekke at en string er kun to ord og at begge ordene har en viss lengde, f.eks. fornavn etternavn
    #TODO: Navn3: Samme som forrige, men fornavn mellomnavn etternavn
    #TODO: Finnes i fil: la input være en string og en fil med strings, sjekk om stringen finnes i filen
    #Den forrige kan f.eks. brukes til å bestemme at visse verdier ikke er lov i brukernavn, passord eller annen input
    #TODO: Wholesome check: sjekke at et brukernavn ikke inneholder støtende ord og varianter av disse.
    #Kanskje lage en datafil for den forrige som kan fylles med ulovlige verdier over tid?
    #TODO: Epostadresse: Sjekke at en string er på formatet tekst.tekst.tekst.,,,.tekst@tekst.com/no/osv
    #TODO: Unikhet: Sjekke at en liste kun inneholder unike verdier
    #TODO: Filer basic: Sjekke at en input-fil har filtypen vi ser etter, f.eks. pdf eller txt ved å se på filendingen
    #TODO: Filer avansert: sjekk at ikke noen prøver å laste opp ulovlige filer ved å manipulere filendingen
    #Sjekk https://www.geeksforgeeks.org/determining-file-format-using-python/ for hjelp med den forrige

