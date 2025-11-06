from question_model import Question
from data import question_data
from quiz_brain import QuizBrian

question_bank=[]
for question in question_data:
    questions_text=question['text']
    questions_answer = question['answer']
    new_question = Question(questions_text,questions_answer)
    question_bank.append(new_question)

# print(question_bank[])
quiz = QuizBrian(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

quiz.final_score()
