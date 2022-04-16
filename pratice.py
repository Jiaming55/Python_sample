from question import Question

test = [
    "1+4=?\n(a) 3\n(b) 4\n(c) 5\n\n",
    "1*4=?\n(a) 3\n(b) 4\n(c) 5\n\n",
    "9-4=?\n(a) 3\n(b) 4\n(c) 5\n\n"
]

questions = [
    Question(test[0], "c")
    , Question(test[1], "b")
    , Question(test[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score+=1
    print("your score is " + str(score))

run_test(questions)