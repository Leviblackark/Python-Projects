
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz

class QuizBrain:
    # TODO: asking the questions
    # The class will do this automatically when the class is constructed
    def __init__(self, q_list):
        # keeps track of question we're on
        self.question_number = 0
        #  Pass in the question bank
        self.question_list = q_list

    def still_has_question(self):
        """Returns True if theirs another question and False if not"""
        # you could also return the whole statement 'return self.question_number < len(self.question_list)'
        #  this would also return a True or False result. example 5 > 3 True 5 > 10 False
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    # the method when the class is accessed through an object

    def next_question(self):
        # question_index is assessing where the object is stored. and becomes the object
        question_index = self.question_list[self.question_number]
        # instead of starting the count from 0 it's adjusted before display and after the index is found
        self.question_number += 1
        input(f"Q.{self.question_number}: {question_index.text} (True/False): ")
