from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question = Question(data['text'], data['answer'])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_have_question():
    answer = input(f"Q.{quiz_brain.question_number}: {quiz_brain.question_list[quiz_brain.question_number-1].text} "
                   f"(True/False): ")

    if quiz_brain.question_list[quiz_brain.question_number-1].answer == answer:
        print("You got it right")
        print(f"The correct answer was: {quiz_brain.question_list[quiz_brain.question_number-1].answer}")
        quiz_brain.add_point()
        print(f"Your current score is: {quiz_brain.point}/{quiz_brain.question_number}")
        quiz_brain.next_question()
        print("")
    else:
        print("That's wrong")
        print(f"The correct answer was: {quiz_brain.question_list[quiz_brain.question_number-1].answer}")
        print(f"Your current score is: {quiz_brain.point}/{quiz_brain.question_number}")
        quiz_brain.next_question()
        print("")

# finish the game

print("You have complete the quiz")
print(f"Your final score was {quiz_brain.point}/{quiz_brain.question_number}")

