import sys
from typing import List, Tuple


class carDiagonal:
  """
    Klasse für die quer stehenden Autos
  """
  name:int
  blocking:List[int]

  def __init__(self, name:int, blocking:List[int]) -> None:
    self.name = name
    self.blocking = blocking

  @property
  def blocking(self):
    return self._blocking

  @blocking.setter
  def blocking(self, value:int) -> None:
    self._blocking = [value, value+1]

  def __str__(self) -> str:
      return str(self.name)+": "+str(self.blocking)

class carStraight:
  """
    Klasse für die gerade stehenden Autos
  """
  name:int
  blockedBy:carDiagonal

  def __init__(self, name:int, blockedBy:carDiagonal) -> None:
    self.name = name
    self.blockedBy = blockedBy

  def __str__(self) -> str:
    if self.blockedBy:
      return(str(self.name) + "_" + str(self.blockedBy))
    else:
      return str(self.name)

def toChr(number:int) -> chr:
  """
    Aus einer Zahl einen Buchstaben Machen. 
    Beginent bei 0 = A, 1 = B...
  """
  return chr(number + ord("A"))

def createParkingLot(data) -> Tuple[List[carStraight], List[carDiagonal]]:
  """
    Erstellt den Parkplatzt, sodass er vom
    Program verstanden werden kann. 
  """
  parkingRow:List[carStraight] = []
  blockingRow:List[carDiagonal] = []

  i:int = ord(data[0])

  # Parkreihe füllen
  while i <= ord(data[2]):
    parkingRow.append(carStraight(i - ord("A"), None))
    i += 1

  fillBlock(data, blockingRow)

  # Für parkende Autos einstellen, wer sie blockiert
  for car in blockingRow:
    for block in car.blocking:
      blockCar = parkingRow[block]
      blockCar.blockedBy = car

  # Prüft, ob die Datei richtig gelesen wurde
  assert len(blockingRow) == int(data.splitlines()[1])

  return parkingRow, blockingRow

def fillBlock(data, blockingRow):
  """Blockierende Reihe füllen"""
  i = 2 # beginnt bei der 3. Reihe
  while i < len(data.splitlines()):
    line = data.splitlines()[i]
    position = int(line[2:len(line)])
    blocking=position
    blockingRow.append(carDiagonal(ord(line[0]) - ord("A"), blocking))
    i += 1

def canMove(blockingRow:List[carDiagonal], car:carDiagonal, size:int, amount:int):
  """
    Gibt aus, ob das Blockierende Auto die Angegebene Menge an Plätzen
    bewegt werden kann. (Positive Menge nach rechts, negativ nach links)
  """
  if amount == 0: # Das Auto kann immer stehen bleiben
    return True

  if not canMove(blockingRow, car, size, amount - (amount/abs(amount))):
    # Gucken, ob das Auto zu der Position einen näher an der Startposition gehen kann
    return canMove(blockingRow, car, size, amount - (amount/abs(amount)))
    
  if  car.blocking[0] + amount < 0 or \
      car.blocking[1] + amount >= size: # Fährt das Auto über den Rand? 
    return False

  for cars in blockingRow: # Es wird probiert ob mit einem der Autos kollidiert
    if ((cars.blocking[0] == car.blocking[0] + amount and cars != car) or \
        (cars.blocking[1] == car.blocking[0] + amount and cars != car) or \
        (cars.blocking[0] == car.blocking[1] + amount and cars != car) or \
        (cars.blocking[1] == car.blocking[1] + amount and cars != car)):  
      return cars

  return True

def move(car, dir, blockingRow, size):
  """
    Führt die Bewegung aus und gibt das Ergebnis als String zurück. \n
    Diese Funktion läuft rekursiv.
  """
  movement = canMove(blockingRow, car, size, dir[0])
  if movement == True:
    return ""
  elif movement == False:
    return "Error"
  else: 
    return str(move(movement, [dir[0]/abs(dir[0]), dir[1]], blockingRow, size)) + toChr(movement.name) + " 1 " + dir[1] + "; "

def main() -> None:
  """
    main
  """
  dataFileLocation = sys.argv[1]          #
  dataFile = open(dataFileLocation, "r")  # Datei einlesen und in data als String 
  data = dataFile.read()                  # speichern. 

  parkingRow, blockingRow = createParkingLot(data) # Aus den daten den Parkplatz "erstellen"

  solution = ""
  for car in parkingRow:
    solution += toChr(car.name) + ": "
    if car.blockedBy:
      #solution += toChr(car.blockedBy.name)

      if car.blockedBy.blocking[0] == car.name:
        dir = [[1, "rechts"], [-2, "links"]]
      else:
        dir = [[-1, "links"], [2, "rechts"]]

      movement0 = canMove(blockingRow, car.blockedBy, len(parkingRow), dir[0][0])
      movement1 = canMove(blockingRow, car.blockedBy, len(parkingRow), dir[1][0])
      #print(movement0)
      #print(movement1)
      if movement0 == True: 
        solution += toChr(car.blockedBy.name) + " 1 " + dir[0][1]
      elif movement1 == True:
        solution +=  toChr(car.blockedBy.name) + " 2 " + dir[1][1]
      elif movement0 != False and movement1 != False:
        solution1 = str(move(car.blockedBy, dir[0], blockingRow, len(parkingRow))) + toChr(car.blockedBy.name) + " 1 " + dir[0][1]
        solution2 = str(move(car.blockedBy, dir[1], blockingRow, len(parkingRow))) + toChr(car.blockedBy.name) + " 2 " + dir[1][1]
        solution += solution1 if (len(solution1) <= len(solution2) and not "Error" in solution1) or "Error" in solution2 else solution2
      elif movement0 != False:
        solution += str(move(car.blockedBy, dir[0], blockingRow, len(parkingRow))) + toChr(car.blockedBy.name) + " 1 " + dir[0][1]
      elif movement1 != False:
        solution += str(move(car.blockedBy, dir[1], blockingRow, len(parkingRow))) + toChr(car.blockedBy.name) + " 2 " + dir[1][1]
      else:
        solution += toChr(car.blockedBy.name) + " Der Wagen kann nicht so bewegt werden, dass das Auto befreit werden kann"

    solution += "\n"

  #print(*parkingRow, sep = ", ")
  #print(*blockingRow, sep = ", ")
  #print(data)
  print(solution)

if __name__ == "__main__":
  main()