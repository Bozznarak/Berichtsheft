# with open("cfgBerichtsheft.txt", "w")as file:
#     file.write("Nachweisnummer;0\nName,Vorname;Otto, Christian\nWoche/Jahr;0/0000\nWocheMontag;WeekStart\nWocheSontag;WeekEnd\nKlasse;IT 32.VC\nAusbildung;Fachinformatiker AE")


import csv                                                          # CSV wird gebraucht um Listen aus der Metadatei zu erstellen
import Kalenderwoche
import codecs

######## MD Dateien übertragen ÄÜÖ richtig an Python, txt und csv dateien haben dabei probleme. 

def FuncMetaList():
    with codecs.open("cfgBerichtsheft.md", "r+", "utf-8") as csvdatei:                   # Funktion um Metadaten aus der CFG Datei zu ziehen
        csv_reader_object = csv.reader(csvdatei, delimiter=";")
        list = []
        for row in csv_reader_object:
            list.append(row)
        return list

# Metaliste [[Mo, "", "","",""],[Di, "",""]]...

Metalist = FuncMetaList()
print(Metalist)

def FuncAkteulleWoche():
    AktWeek = input(str("Möchtest du die Aktuelle Woche oder eine Manuelle Wochen- Jahreingabe? n / y :"))
    if AktWeek == "n":
        Kalenderwoche.GetDatesOutOfProofNumber()
        monday = Kalenderwoche.GetDatesOutOfProofNumber()[0]
        sunday = Kalenderwoche.GetDatesOutOfProofNumber()[1]
        week = Kalenderwoche.GetDatesOutOfProofNumber()[2]
        year = Kalenderwoche.GetDatesOutOfProofNumber()[3]
        return monday , sunday , week , year
    else:
        Metalist[2][1] = input(str("Bitte gebe Kalenderwoche und Jahr an in X/XXXX: "))
        year = Metalist[2][1][3:]
        week = Metalist[2][1][0:2]
        monday, sunday, week , year = Kalenderwoche.GetDatesOutOfProofNumber(year, week)
        return monday , sunday , week , year

monday, sunday, week, year = FuncAkteulleWoche()

Metalist[3][1] = monday
Metalist[4][1] = sunday
Metalist[2][1] = (f"{week}/{year}")
Nachweisnummer = int(week) - 1
Metalist[0][1] = str(Nachweisnummer)


# print(len(Metalist))
print(Metalist)




