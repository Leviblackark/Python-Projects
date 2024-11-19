
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz

class QuizBrain:
    # TODO: asking the questions
    # The class will do this automatically when the class is constructed
    def __init__(self, q_list):
        # keeps track of question we're on
        self.question_number = 0
        self.score = 0
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
        # increase the count to 1 after 0 as been run so it displays 1 when the input displays
        # this also allows the index for the next question to move up by 1 so when its next called it access the next
        #  question and not the current
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question_index.text} (True/False): ")
        # passing the user_answer in to check_answer to see if it's correct
        self.check_answer(user_answer, question_index.answer)

    def check_answer(self, user_answer, correct_answer):
        #  Make sure both the entry and the right answer are comparable with the .lower()
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            # if false so the user got it wrong
            print("That was wrong")
        # Outside the block so it displays regardless
        print(f"The correct answer was: {correct_answer}")
        # score and current question the user is on
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def final_score(self):
        """prints the last score data"""
        print(f"Your final score was: {self.score}/{self.question_number}")


