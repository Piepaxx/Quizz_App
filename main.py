import html
import requests
from questions import Questions
from quizzbrain import QuizBrain
from ui import Ui


def create_question_list():
    question_list = list()
    resource = requests.get(url="https://opentdb.com/api.php?amount=50&type=boolean")
    resource.raise_for_status()

    quizz_data = resource.json()
    print(quizz_data)
    question_data = quizz_data['results']

    for _question in question_data:
        question = html.unescape(_question['question'])
        answer = html.unescape(_question['correct_answer'])

        question_list.append(Questions(question, answer))

    return question_list


def main():

    question_list  = create_question_list()
    quizzbrain = QuizBrain(question_list)
    window = Ui(quizzbrain)
















if __name__ == '__main__':
    main()