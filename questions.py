from questionClass import Question

question_prompts = [
    'What color are apples? \n(a) Red/Green\n(b) Purple\n(c) Orange\n\n',
    'What color are Bananas? \n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
    'What color are strawberries? \n(a) Yellow\n(b) Red\n(c) Blue\n\n'
]

#a list of prompts and answers
questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b')
]

'''
run_test will receive a list of prompts&answers.
displays the promtps and check if the user's answers are correct.
track the answers and displays how many questions were correct once finished.
'''
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct.')

run_test(questions)
