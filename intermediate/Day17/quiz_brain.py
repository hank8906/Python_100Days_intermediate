class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 1
        self.question_list = question_list
        self.point = 0

    def next_question(self):
        self.question_number += 1

    def add_point(self):
        self.point += 1

    def still_have_question(self):
        if self.question_number <= len(self.question_list)+1:
            return True
        else:
            return False

