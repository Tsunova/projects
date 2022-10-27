#   you can run this in python!
#   https://www.programiz.com/python-programming/online-compiler/

true = True
false = False

import random

GeneratedNames = [
    "Billy",
    "Joe",
    "Superman",
    "Aegis",
    "Solis",
    "Bard",
    "Macintosh",
    "Nevae",
    "Juno",
    "Eanor",
]


Students = {}

#   check grade value
def checkGrade(grade):
    if not isinstance(grade, int):
        print(str(grade), " needs to be an integer")
    if grade < 60:
        return "F"
    elif int(grade) >= 60 and grade < 70:
        return "D"
    elif int(grade) >= 70 and grade < 80:
        return "C"
    elif int(grade) >= 80 and grade < 90:
        return "B"
    elif int(grade) >= 90:
        return "A"

#   randomize student values
for i in range(1, 11):
    thisName = random.choice(GeneratedNames)
    GeneratedNames.remove(thisName)
    #
    Students[thisName] = {}
    Students[thisName]["Math"] = checkGrade(random.randint(0, 100))
    Students[thisName]["English"] = checkGrade(random.randint(0, 100))
    Students[thisName]["Science"] = checkGrade(random.randint(0, 100))
    print(thisName, Students[str(thisName)])
    
#   you can run this in python!
#   https://www.programiz.com/python-programming/online-compiler/

#   ask for user input
x = int(input("[SYSTEM]: Enter your grade:"))
print("[SYSTEM]: you have a " + checkGrade(x), "!")
