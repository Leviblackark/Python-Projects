from question_model import Question
from data import question_data

question_bank = []

# Create a Question object from each entry in question_data
# Converting the data into an object so its easier

for new_question in question_data:
    # access text and answer
    question_text = new_question["text"]
    question_answer = new_question["answer"]
    added_question = Question(text=question_text, answer=question_answer)

    # Append each Question object to the question_bank
    question_bank.append(added_question)

print(question_bank)
# Accessing in a list position and then access object with dot notation
print(question_bank[0].answer)

