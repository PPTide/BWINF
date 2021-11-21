import sys
from typing import List

def neededChange(dates:List[int]):
  """
    Für die Liste an Verfügbarkeiten die benötigten Änderungen
    für jedes Datum ausrechnen
  """
  neededChanges = []
  for i in dates:
    # Für jedes Datum sind die benötigten Änderungen
    # die Anzahl an Werten vor dem niedrigsten vorkommen
    # dieses Wertes in einem sortierten Array
    neededChanges.append(sorted(dates).index(i))
  return neededChanges

def main() -> None:
  """
    main
  """
  dataFileLocation = sys.argv[1]          #
  dataFile = open(dataFileLocation, "r")  # Datei einlesen und in data als String 
  data = dataFile.read()                  # speichern. 


  dates = []
  for i in range(int(data.split(" ")[0])):
    preferences = data.splitlines()[i + 1]
    preference = []
    for j in range(int(data.split(" ")[1].split("\n")[0])):
      preference.append(int(preferences.split(" ")[j]))
    dates.append(preference)


  # Vieleicht
  #dates = [[j - min(i) for j in i] for i in dates]

  neededChanges = [neededChange(i) for i in dates]


  # rotieren (+spiegeln)
  neededChangesR = list(zip(*neededChanges))

  neededChangesS = [sum(i) for i in neededChangesR]

  solutionCost = min(neededChangesS)
  solutionDate = neededChangesS.index(solutionCost)

  print("Für den {solutionDate}. Termin {muss} {solutionCost} {eintrag} verändert werden."
    .format(solutionDate=solutionDate+1, solutionCost=solutionCost,
    # Gramatik :)
    muss="muss" if solutionCost == 1 else "müssen",
    eintrag="Eintrag" if solutionCost == 1 else "Einträge"))


if __name__ == "__main__":
  main()