import datetime
from datetime import date, timedelta
from time import time



def GetDatesOutOfProofNumber(*arg):
    if arg:
        Woche = arg[1]
        Jahr = arg[0]
        mondaytemp = datetime.datetime.strptime(f"{arg[0]}-{arg[1]}-1", "%Y-%W-%w")         #
        sundaytemp  = datetime.datetime.strptime(f"{arg[0]}-{arg[1]}-0", "%Y-%W-%w")
        monday= datetime.datetime.strftime(mondaytemp, "%d.%m.%y")
        sunday=datetime.datetime.strftime(sundaytemp, "%d.%m.%y")
        print(arg)
        return [monday, sunday , Woche, Jahr] 
    else:
        today = date.today()
        mondaytemp = today - timedelta(today.weekday())                                     #timedelta lässt dich mit Datumeinheiten rechnen (Parameter ab Tage möglich)
        sundaytemp = mondaytemp + timedelta(days=6)
        monday=datetime.datetime.strftime(mondaytemp, "%d.%m.%y")
        sunday=datetime.datetime.strftime(sundaytemp, "%d.%m.%y")
        Woche=datetime.datetime.now().strftime("%W")
        Jahr=datetime.datetime.now().strftime("%Y")
        # print(arg)
    return [monday, sunday ,Woche, Jahr]

# print(GetDatesOutOfProofNumber(2021, 5))

# monday=datetime.datetime.strftime(GetDatesOutOfProofNumber()[0], "%d.%m.%Y")
# sunday=datetime.datetime.strftime(GetDatesOutOfProofNumber()[1], "%d.%m.%Y")

# print(GetDatesOutOfProofNumber()) # Jahr Kalenderwoche
