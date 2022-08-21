import Exercicio4


populationA = int(input("Digite a populacao de A:   "))
growthA = int(input("Digite o crscimento em anos da populacao de A:   "))

populationB = int(input("Digite a populacao de B:   "))
growthB = int(input("Digite o crescimento em anos da populacao de B:  "))

thisYear = 2022

Exercicio4.verifyPopulation(populationA, growthA, populationB, growthB, thisYear)

Exercicio4.printYears(thisYear)
