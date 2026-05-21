print("Welcome to the Computer Quiz Game")
Question = input("Want to play this Quiz Game ?\n")
if Question.lower() != "yes":
    quit()
else:
    print("Let's Play")
    score = 0

answer = input("1] What is the full form of CPU?\n")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("2] What is the full form of RAM?\n")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("3] What is the full form of GPU?\n")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("4] What is the full form of ROM?\n")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("5] What is the full form of BIOS?\n")
if answer.lower() == "basic input output system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("6] Who is Father of Computer?\n")
if answer.lower() == "Charles Babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
<<<<<<< HEAD
print("You got " + str((score/6) * 100) + "%")
=======
print("You got " + str((score/5) * 100) + "%")
>>>>>>> b464555ef063abe05d75983394e1ca2b3f1601a5
