answers = open("./input.txt", "r")

numGroups = 0
answersPerGroup = []
totalAnswers = 0 


for index, line in enumerate(answers):
  if line in ['\n', '\r\n']:
    numGroups += 1
    totalAnswers += len(answersPerGroup)
    print(len(answersPerGroup))
    answersPerGroup = []
    print('---------')
  else:
    for answer in line:
      if answer not in answersPerGroup and answer != '\n':
        answersPerGroup.append(answer)

  if not line.endswith('\n'):
    numGroups += 1
    totalAnswers += len(answersPerGroup)
    print(len(answersPerGroup))
    print('---------')

print("Total answers: ", totalAnswers)
