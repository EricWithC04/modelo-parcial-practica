import pandas as pd
import datetime

def over_25_years():
    ages = pd.read_csv('edades.csv', encoding="utf-8", header=None)
    formated_ages = []

    today = str(datetime.date.today()).split("-")

    for i, element in enumerate(today):
        today[i] = int(element)

    for _index, age in ages[1:].iterrows():
        formated_ages.append(age[0].split("/"))
    
    over_25 = [a for a in formated_ages if int(a[2]) < today[0] - 25]
    for age in [a for a in formated_ages if int(a[2]) == today[0] - 25]:
        if (int(age[1]) < today[1]):
            over_25.append(age)
        elif (int(age[1]) == today[1] and int(age[0]) <= today[2]):
            over_25.append(age)
    
    for i, element in enumerate(over_25):
        over_25[i] = [int(element[0]), int(element[1]), int(element[2])]
    
    calculated_ages = []
    for age in over_25:
        if (age[1] < today[1]):
            calculated_ages.append(today[0] - age[2])
        elif (age[1] == today[1] and age[0] <= today[2]):
            calculated_ages.append(today[0] - age[2])
        else:
            calculated_ages.append(today[0] - age[2] - 1)
    
    calculated_ages.sort()

    fi = {}
    for i in calculated_ages:
        if i in fi:
            fi[i] += 1
        else:
            fi[i] = 1
    
    df = pd.DataFrame({'Age':fi.keys(), 'Frequency':fi.values()})

    return df

print(over_25_years())