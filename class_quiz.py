#class_quiz.py

class Quiz:
    def __init__(self, question, choice0, choice1, choice2, choice3, answer:int):
        self.question = question
        self.choices = [choice0, choice1, choice2, choice3]
        self.answer = answer
    #
    def get_question(self):
        return self.question
    def get_choices(self):
        return self.choices
    def get_answer(self):
        return self.answer
    #
    def print_quiz(self):
        print("Q : " + self.question)
        for i in range(4):
            print('[' + str(i + 1) + ']' + self.choices[i])
        print("A : [" + str(self.answer) + ']')
        print()
    def check_answer(self, answer:int):
        return answer == self.answer
