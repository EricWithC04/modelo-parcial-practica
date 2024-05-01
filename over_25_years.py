import pandas as pd
import datetime

def over_25_years():
    ages = pd.read_csv('edades.csv', encoding="utf-8", header=None)
    formatedAges = []

    today = str(datetime.date.today()).split("-")

    for _index, age in ages[1:].iterrows():
        formatedAges.append(age[0].split("/"))
    
    over_25 = [a for a in formatedAges if int(a[2]) <= 1998]
    for age in [a for a in formatedAges if int(a[2]) == 1999]:
        if (int(age[1]) < 5):
            over_25.append(age)
        elif (int(age[1]) == 5 and int(age[0]) <= 1):
            over_25.append(age)
    print(over_25)

over_25_years()