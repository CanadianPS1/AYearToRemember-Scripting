import random
answers = [1775,
            1783,
            1865,
            1901,
            1939,
            1975,
            1989,
            1949,
            1945,
            1991
]
questions = ["When did the start of the Revolutionary War",
           "When was the United States Constitution signed",
           "When was President Lincoln assassinated",
           "When was Theodore Roosevelt's first day in office as President of the United States",
           "When was the beginning of World War II",
           "When was the first personal computer introduced",
           "When was the Berlin Wall taken down",
           "When did Germany Regain Hamburg",
           "When was Korea was given independence from Japan",
           "When did the Soviet Union fall"
]
usedQuestions = []
points = 0
for i in range(len(answers)):
    print("      ~QUESTION NUMBER ", i + 1, "~")
    print("Points: ", points)
    #grabs the incorrect answers and the correct one
    num1 = random.choice(answers)
    #checks to make sure the question hastn already been asked
    while(num1 in usedQuestions):
        num1 = random.choice(answers)
    usedQuestions.append(num1)
    num2 = random.choice(answers)
    #checks to make sure their arnt duplicate answers
    while(num1 == num2):
        num2 = random.choice(answers)
    num3 = random.choice(answers)
    while(num3 == num1 or num3 == num2):
        num3 = random.choice(answers)
    num4 = random.choice(answers)
    while(num4 == num1 or num4 == num2 or num4 == num3):
        num4 = random.choice(answers)
    answer1 = num1
    answer2 = num2
    answer3 = num3
    answer4 = num4
    #formating for printing the question
    ask = [answer1,
        answer2,
        answer3,
        answer4]
    random.shuffle(ask)
    #loops until you get the answer correct
    count = 10
    while(True):
        #prints questions to the user
        print(questions[answers.index(num1)], "?")
        print("(A) " , ask[0], " (B) ", ask[1])
        print("(C) " , ask[2], " (D) ", ask[3])
        #checks for correct input
        while(True):
            answer = input().lower()
            if(answer == "a" or answer == "b" or answer == "c" or answer == "d"):
                break
            else:
                print("ERROR: invalid input, try again")
        check = "g"
        #checks for which answer was correct
        for i in range(4):
            if(ask[i] == answer1):
                if(i == 0):
                    check = "a"
                    break
                elif(i == 1):
                    check = "b"
                    break
                elif(i == 2):
                    check = "c"
                    break
                elif(i == 3):
                    check = "d"
                    break
        if(check == answer):
            print("Correct!!!")
            points += count
            break
        else:
            print("FALSE!!!")
            if(count > 0):
                count = count - 2.5
print("Points: ", points)
print("   ", points / len(questions) * 10, "%")
if(points == len(questions) * 10):
    print("YOU GOT A PERFECT SCORE!!!")
exit