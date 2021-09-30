from os import write

def resetConfigData():
    cfgDatei = open("cfgBerichtsheft.md", "w+")
    cfgDatei.write("Nachweisnummer;0\r")
    cfgDatei.write("Name,Vorname;Otto, Christian\r")
    cfgDatei.write("Woche/Jahr;0/0000\r")
    cfgDatei.write("WocheMontag;WeekStart\r")
    cfgDatei.write("WocheSontag;WeekEnd\r")
    cfgDatei.write("Klasse;IT 32.VC\r")
    cfgDatei.write("Ausbildung;Fachinformatiker AE\r")
    cfgDatei.write("Mo;;;;\r")
    cfgDatei.write("Di;;;;\r")
    cfgDatei.write("Mi;;;;\r")
    cfgDatei.write("Do;;;;\r")
    cfgDatei.write("Fr;;;;")

resetConfigData()


###### 56 Zeichen pro ;; Eintrag