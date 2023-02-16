print("Hey there! Welcome to my new game.")

playing = input("Do you want to play? ")

if playing != "yes".lower():
    quit()

print("Lets get started then!")
score = 0

answer = input("What is the name of the NBA team in Memphis? ").lower()
if answer == "grizzlies":
    print("You a Grizz fan ain't it?")
    score += 25
else:
    print("C'mon mane.")

answer = input("What major river runs along Memphis? ").lower()
if answer == "mississippi river":
    print("Correct!")
    score += 25
else:
    print("C'mon mane..")

answer = input("Where can you find bison in Memphis? ").lower()
if answer == "shelby farms":
    print("Correct!")
    score += 25
else:
    print("C'mon mane.")

answer = input("What global logistics company has a headquarters in Memphis? ").lower()
if answer == "fedex":
    print("Correct!")
    score += 25
else:
    print("C'mon mane.")

print("You got " + str(score) + " out of 100 points!")
