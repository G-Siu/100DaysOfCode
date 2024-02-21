def inputDartsMark():
    dart1 = -1
    dart2 = -1
    dart3 = -1
    while dart1 <= 0 or dart1 > 60:
        dart1 = int(input("Enter first dart score : "))
    while dart2 < 0 or dart2 > 60:
        dart2 = int(input("Enter second dart score : "))
    while dart3 < 0 or dart3 > 60:
        dart3 = int(input("Enter third dart score : "))  
    totalScore = dart1 + dart2 + dart3
    displayResult(totalScore)

def displayResult(totalScore):
    if totalScore == 180:
        print(f"Maximum Score of {totalScore}")
    elif totalScore >= 140:
        print(f"A great score of {totalScore}")
    elif totalScore >= 100:
        print(f"Average Score of {totalScore}")
    else:
        print(f"Poor score of {totalScore}")

inputDartsMark()

