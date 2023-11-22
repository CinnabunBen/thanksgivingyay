#introduction to the game
print("hello welcome to Benji's easy thanksgiving quiz!")
print("We will be putting your skills to the test with these 3 questions!")

#how many Qs the user got correct
number_questions_correct = 0
#question 1
for i in range(1):
    print("Question 1: What does a turkey say?")
    print("1: Bark")
    print("2: Meow")
    print("3: Gobble")
    print("4: Oink")

    Correct_answer1 = 3

    while True:
        user_input = int(input("which one? "))

        if user_input == Correct_answer1:
            print("Correct!")
            break
        else:
            print("Wrong! Try again!")

print("Moving on!")
number_questions_correct += 1

#question 2
for i in range(1):
    print("Question 2: what month is thanksgiving in? :")
    print("1: November")
    print("2: January")
    print("3: July")
    print("4: October")

    Correct_answer2 = 1

    while True:
        user_input = int(input("which one? "))

        if user_input == Correct_answer2:
            print("Correct!")
            break
        else:
            print("Wrong! Try again!")

print("Moving on!")
number_questions_correct += 1

#question 3
for i in range(1):
    print("Question 3: What is the best side dish at thanksgiving? :")
    print("1: Green Beans")
    print("2: Cranberry Sauce")
    print("3: Mashed Potatoes")
    print("4: Mac & Cheese")

    Correct_answer3 = 4

    while True:
        user_input = int(input("which one? "))

        if user_input == Correct_answer3:
            print("Correct!")
            break
        else:
            print("Wrong! Try again!")

print("Moving on!")
number_questions_correct += 1
    

print("You are all done with the quiz! You got " + str(number_questions_correct) + " questions right!")
    


