# 26/05/2025
# Building a multiple-choice quiz  using Python

# Steps
# 1. Define an array of questions with options.
# 2. Create a questions class to store the questions prompts and answer

from question import Question
question_prompts = [
    "What is the capital of France?\n(a) London\n(b) Paris\n(c) Berlin\n\n",
    "Who wrote 'To Kill a Mockingbird'?\n(a) Harper Lee\n(b) Mark Twain\n(c) F. Scott Fitzgerald\n\n",
    "What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Saturn\n\n"
]

# Array of questions
questions = [ # creating question object
    Question(question_prompts[0],"b"),
    Question(question_prompts[1],"a"),
    Question(question_prompts[2],"b")
]

def run_test(questions): #A list of question objecst that we want to ask the user
    score = 0
    for question in questions:
        answer = input(question.prompt) # asking user for input
        if answer == question.answer: # checking if the answer is correct
            score += 1 # incrementing score if answer is correct
    print("You got " + str(score) + "/" + str(len(questions)) + " correct") # printing the score

run_test(questions) # calling the function to run the test