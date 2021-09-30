import subprocess, os
import codecs
import datetime
from datetime import date, timedelta
from time import time

import MetaDatenBekommen

# print(MetaDatenBekommen)

# WeekTimeList = ["timeMon", "timeTue", "timeWed", "timeThu", "timeFri"]
EntryChangeList = ["logEntryNumber", "firstNameLastName", "weekYear", "wStart", "wEnd", "className", "educationGoal", ["timeMon", "timeTue", "timeWed", "timeThu", "timeFri"], ["MetaMo", "MetaTu", "MetaWe", "MetaTh", "MetaFr"], "timeWeek"] # Signature muss noch gefunden werden.

### Tex Datei logEntryNumber , firstNameLastName , weekYear ,wStart , wEnd , className , educationGoal , timeWeek , SignaturePNG , todayDate
MetaDatenBekommen.Metalist 

#### auslesen der Datei + Textstellen finden die mit eintragungen ersetzt werden sollen


def NewTex (string):
    with codecs.open (f"BerichtsheftNr{MetaDatenBekommen.Metalist[0][1][:2]}Otto.tex", "a", "utf-8")as file:
        file.write(string) 

with open(f"BerichtsheftNr{MetaDatenBekommen.Metalist[0][1][:2]}Otto.tex","w")as file:
    file.write("")
file.close()


with codecs.open("BerichtheftVorlage.tex","r+", "utf-8") as file:
    counter=1
    TimeCounter = 0 
    DayCounter = 0
    EntryListCounter = 0 
    MetaCounter = 7 
    hourCounter = 0          
    for line in file:                                                               # for schleife macht aus der jeder line eine List
        linestripped = line.strip().split(" ")
        for word in range(0,len(linestripped)):                                     # for schleife macht aus jeder Liste ein String 
            if linestripped[word] == (f"{EntryChangeList[EntryListCounter]}"):
                linestripped[word] = str(MetaDatenBekommen.Metalist[EntryListCounter][1])
                EntryListCounter+=1
                if EntryListCounter >= len(EntryChangeList):
                    EntryListCounter = 0
            if linestripped[word] == (f"{EntryChangeList[EntryListCounter][TimeCounter]}"):
                if TimeCounter >= 4:                                                     
                    TimeCounter = 4
                    if len(MetaDatenBekommen.Metalist[MetaCounter][1]) > 1:
                        linestripped[word] = "4"
                        hourCounter = hourCounter+4
                    else:
                        linestripped[word] = "0"
                        hourCounter= hourCounter+0
                else:                           
                    TimeCounter+=1
                    if len(MetaDatenBekommen.Metalist[MetaCounter][1]) > 1:
                        linestripped[word] = "9"
                        hourCounter = hourCounter+9
                    else:
                        linestripped[word] = "0"
                        hourCounter = hourCounter+0                                      
            if linestripped[word] == (f"{EntryChangeList[8][DayCounter]}{counter}"):
                linestripped[word] = str(MetaDatenBekommen.Metalist[MetaCounter][counter]) #7 8 9 10 11
                counter +=1
            if counter >= 5:
                counter = 1
                DayCounter+=1
                MetaCounter+=1
            if DayCounter >= 5:
                EntryListCounter = 9
                DayCounter = 0
            if linestripped[word] == "timeTotal": 
                linestripped[word] = str(hourCounter)
            if linestripped[word] == "Datum":
                today = date.today().strftime("%d.%m.%Y")
                linestripped[word] = (f"Datum {today}")
        NewTex(" ".join(linestripped)+"\n")



# subprocess.call("pdflatex BerichtsheftTemp.tex")
# os.system("BerichtsheftTemp.pdf")
            
subprocess.call(f"pdflatex BerichtsheftNr{MetaDatenBekommen.Metalist[0][1][:2]}Otto.tex")
os.system(f"BerichtsheftNr{MetaDatenBekommen.Metalist[0][1][:2]}Otto.pdf")
                

                    

            


                
