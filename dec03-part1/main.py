# Read Input
inputFile = open('input.txt', 'r')
wireStepsA = inputFile.readline().rstrip('\r\n').split(',')
wireStepsB = inputFile.readline().rstrip('\r\n').split(',')
inputFile.close()
# wireStepsA = ['R8','U5','L5','D3']
# wireStepsB = ['U7','R6','D4','L4']

# Text Helpers
def coordToString(coord):
  return '[x:' + str(coord[0]) + ' y:' + str(coord[1]) + ']'

def printWire(wireSteps, wireCoords):
  numberToPrint = 7
  print('wireSteps:\n  ' + '\n  '.join(wireSteps[:numberToPrint]))
  print('wireCoords:\n  ' + '\n  '.join(map(coordToString, wireCoords[:numberToPrint])))
  print('\n')

# From input wire steps to subsequent wire coordinates
wireStepDirections = {
  'U': (0, -1),
  'D': (0, 1),
  'L': (-1, 0),
  'R': (1, 0),
}
def wireStepToCoordStep(wireStepDirection, wireStepSize):
  base = wireStepDirections.get(wireStepDirection)
  return (base[0] * wireStepSize, base[1] * wireStepSize)

def wireStepsToCoords(wireSteps):
  curr = (0, 0)
  coords = []
  coords.append(curr)
  for wireStep in wireSteps:
    coordStep = wireStepToCoordStep(wireStep[0], int(wireStep[1:]))
    curr = (curr[0] + coordStep[0], curr[1] + coordStep[1])
    coords.append(curr)
  printWire(wireSteps, coords)
  return coords

# Find the intersections of the lists of coordinates
def findIntersection(coordStartA, coordEndA, coordStartB, coordEndB):
  verticalStartY = None
  verticalEndY = None
  verticalX = None
  horizontalStartX = None
  horizontalEndX = None
  horizontalY = None
  if ((coordStartA[0] - coordEndA[0]) == 0):
    if ((coordStartB[0] - coordEndB[0]) == 0):
      return None

    verticalStartY = min([coordStartA[1], coordEndA[1]])
    verticalEndY = max([coordStartA[1], coordEndA[1]])
    verticalX = coordStartA[0]
    horizontalStartX = min([coordStartB[0], coordEndB[0]])
    horizontalEndX = max([coordStartB[0], coordEndB[0]])
    horizontalY = coordStartB[1]
  else:
    if ((coordStartB[1] - coordEndB[1]) == 0):
      return None
    return findIntersection(coordStartB, coordEndB, coordStartA, coordEndA);

  if (verticalX <= horizontalStartX or verticalX >= horizontalEndX):
    return None
  if (horizontalY <= verticalStartY or horizontalY >= verticalEndY):
    return None

  return (verticalX, horizontalY)

def findIntersections(wireCoordsA, wireCoordsB):
  intersections = []
  previousCoordA = None
  previousCoordB = None
  for currentCoordA in wireCoordsA:
    for currentCoordB in wireCoordsB:
      if (previousCoordA is not None):
        intersection = findIntersection(previousCoordA, currentCoordA, previousCoordB, currentCoordB)
        if (intersection is not None):
          intersections.append(intersection)
      previousCoordB = currentCoordB
    previousCoordA = currentCoordA
  return intersections

intersections = findIntersections(
  wireStepsToCoords(wireStepsA),
  wireStepsToCoords(wireStepsB)
)

# Find the intersection closest to home
print('intersections:', intersections)
def coordToManhattanDistance(coord):
  return abs(coord[0]) + abs(coord[1])
print('closest:', min(map(coordToManhattanDistance, intersections), default='no intersections found'))
