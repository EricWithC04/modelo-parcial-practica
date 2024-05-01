import pandas as pd

def over_25_years():
    ages = pd.read_csv('edades.csv', encoding="utf-8", header=None)
    formatedAges = []

    for _index, age in ages[1:].iterrows():
        formatedAges.append({
            "date": age[0].split("/"),
            "name": age[1],
        })

over_25_years()