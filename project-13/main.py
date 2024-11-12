from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Create a Question object from each entry in question_data
# Converting the data into an object so its easier

for new_question in question_data:
    # access text and answer
    question_text = new_question["text"]
    question_answer = new_question["answer"]
    # turning the dictionary in to an object for each index
    added_question = Question(text=question_text, answer=question_answer)

    # Append each Question object to the question_bank
    question_bank.append(added_question)

# check that it was success in turning into an object
# print(question_bank)
# Accessing the object inside the list storing the attributes (variables)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()




