import pandas as pd
import datetime

def over_25_years():
    ages = pd.read_csv('edades.csv', encoding="utf-8", header=None)
    formatedAges = []

    today = str(datetime.date.today()).split("-")

    for _index, age in ages[1:].iterrows():
        formatedAges.append({
            "date": age[0].split("/"),
            "name": age[1],
        })
    
    over_25 = [a for a in formatedAges if int(a["date"][2]) <= 1998]
    for age in [a for a in formatedAges if int(a["date"][2]) == 1999]:
        if (int(age["date"][1]) < 5):
            over_25.append(age)
    print(today)

over_25_years()