import math 

seats = open("./input.txt", "r")

row = -1
column = -1

seatIDs = []

for seat in seats:

  lowerRow = 0
  upperRow = 127
  lowerColumn = 0
  upperColumn = 7
  
  for index, t in enumerate(seat):
    if index <= 6:
      if t == "F":
        upperRow = upperRow - math.ceil((upperRow - lowerRow)/2)

      elif t == "B":
        lowerRow = lowerRow + math.ceil((upperRow - lowerRow)/2)
      
      if upperRow == lowerRow:
        row = lowerRow
    else:
      if t == "L":
        upperColumn = upperColumn - math.ceil((upperColumn - lowerColumn)/2)

      elif t == "R":
        lowerColumn = lowerColumn + math.ceil((upperColumn - lowerColumn)/2)
      
      if upperColumn == lowerColumn:
        column = lowerColumn
    
    if index == len(seat) - 1:
      seatIDs.append(row * 8 + column)

print("Max seat id: ", max(seatIDs)) # Answer to Part One

sortedIds = sorted(seatIDs)
for index, seatID in enumerate(sortedIds):
  if index == 0:
    continue

  if sortedIds[index-1] != seatID - 1: 
    print("Your seat id: ", seatID - 1) # Answer to Part Two


