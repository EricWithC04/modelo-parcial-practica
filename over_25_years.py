import pandas as pd
import datetime

def over_25_years():
    ages = pd.read_csv('edades.csv', encoding="utf-8", header=None)
    formated_ages = []

    today = str(datetime.date.today()).split("-")

    for _index, age in ages[1:].iterrows():
        formated_ages.append(age[0].split("/"))
    
    over_25 = [a for a in formated_ages if int(a[2]) <= 1998]
    for age in [a for a in formated_ages if int(a[2]) == 1999]:
        if (int(age[1]) < 5):
            over_25.append(age)
        elif (int(age[1]) == 5 and int(age[0]) <= 1):
            over_25.append(age)
    
    calculated_ages = []
    for age in over_25:
        if (int(age[1]) < 5):
            calculated_ages.append(int(today[0]) - int(age[2]))
        elif (int(age[1]) == 5 and int(age[0]) <= 1):
            calculated_ages.append(int(today[0]) - int(age[2]))
        else:
            calculated_ages.append(int(today[0]) - int(age[2]) - 1)
    
    calculated_ages.sort()

    fi = {}
    for i in calculated_ages:
        if i in fi:
            fi[i] += 1
        else:
            fi[i] = 1
    print(fi)

over_25_years()