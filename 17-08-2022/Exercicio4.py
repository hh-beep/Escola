# Ha 2 paises, o 1 tem 80.000 habitantes e cresce 3% a.a. , o 2 tem 200.000 e cresce a 1.5% a.a.
# Calcule a quantidade de anos para o 1 passar o 2


populationA = 80000
growthA = 3

populationB = 200000
growthB = 1.5

thisYear = 2022

def verifyPopulation(populationA, growthA, populationB, growthB, thisYear):
    while (  populationA <= populationB  ):
        populationA += (populationA * (  growthA / 100  ))
        populationB += (populationB * (  growthB / 100  ))
    
        thisYear += 1

def printYears(thisYears):
    print("")
    print("-" * 75)
    print("|")
    print(f"| Demora aproximadamente {thisYear - 2022} anos para o 1 passar o 2, em {thisYear} ")
    print("|")
    print("-" * 75)
    print("")

verifyPopulation(populationA, growthA, populationB, growthB, thisYear)
printYears(thisYear)
