import sys
import math
from typing import List, Tuple

def main():
  """
    main
  """
  dataFileLocation = sys.argv[1]          #
  dataFile = open(dataFileLocation, "r")  # Datei einlesen und in data als String 
  data = dataFile.read()                  # speichern. 

  houses:List[Tuple] = []
  winds:List[Tuple] = []
  windHeight:List[int] = []

  for idx, building in enumerate(data.splitlines()):
    if idx == 0:
      houseNum = int(building.split(" ")[0])
      windNum = int(building.split(" ")[1])
    elif idx <= houseNum:
      houses.append((int(building.split(" ")[0]), int(building.split(" ")[1])))
    else:
      winds.append((int(building.split(" ")[0]), int(building.split(" ")[1])))

  for idx, wind in enumerate(winds):
    distances = []
    for house in houses:
      distance = (wind[0] - house[0], wind[1] - house[1])
      distances.append(math.sqrt((distance[0]**2)+(distance[1]**2)))
    windHeight.append(min(distances)/10)

  for idx, height in enumerate(windHeight):
    print("Die " + str(idx + 1) + ". Windturbine kann ca. " + str(round(height)) + " meter hoch sein.")

if __name__ == "__main__":
  main()