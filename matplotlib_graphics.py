import matplotlib.pyplot as plt
from over_25_years import over_25_years as o25

def graphics():
    ages = o25()

    plt.plot(ages["Age"], ages["Frequency"], color="blue")
    plt.title("Frecuencia de cada edad")
    plt.xlabel("Edades")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.show()

graphics()