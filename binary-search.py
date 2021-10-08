import random

def init():
  numbersList = []
  rangeLoop = 41
  for i in range(rangeLoop):
    n = random.randint(0, 100)
    numbersList.append(n);

  numbersList.sort(reverse=False)

  searchNumber = 64
  binary_search(numbersList, searchNumber)




def binary_search(list, search):
  minIndex = 0
  maxIndex = len(list)-1
  searchWasFound = False
  while maxIndex - minIndex > 1:
    meanIndex = int((minIndex + maxIndex) / 2)
    meanIndexNumber = list[meanIndex]

    if search == meanIndexNumber:
      searchWasFound = True
      break
    elif search > meanIndexNumber:
      minIndex = meanIndex + 1
    else:
      maxIndex = meanIndex - 1

    print("mean index: ",meanIndex)
    print("min index: ",minIndex)
    print("max index: ",maxIndex)

  print("Number found.") if searchWasFound == True else print("Number not found.")

init()
