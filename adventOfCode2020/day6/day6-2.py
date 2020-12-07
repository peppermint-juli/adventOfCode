answers = open("./input.txt", "r")

numGroups = 0
answersPerGroup = []
totalAnswers = 0 
firstPerson = True

for index, line in enumerate(answers):
  if line in ['\n', '\r\n']:
    numGroups += 1
    totalAnswers += len(answersPerGroup)
    firstPerson = True
    answersPerGroup = []
  else:
    if firstPerson:
      answersPerGroup = list(line)
      answersPerGroup.pop()
    else:
      answersPerGroup = list(set(line) & set(answersPerGroup))

    firstPerson = False

  if not line.endswith('\n'):
    numGroups += 1
    totalAnswers += len(answersPerGroup)
    print('---------')

print("Total answers: ", totalAnswers)
