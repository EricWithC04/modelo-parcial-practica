import pandas as pd

def over_25_years():
    ages = pd.read_csv('edades.csv', encoding="utf-8")
    print(ages[0:10])

over_25_years()