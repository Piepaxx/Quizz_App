class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.current_question_index = 0
        self.score = 0

    def check_answer(self, user_input):
        correct_answer = self.questions_list[self.current_question_index - 1].answer
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
            return True
        else:
            print("Wrong!")
            return False

    def still_has_questions(self):
        # Checks if we are at the end of the quiz
        return self.current_question_index < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.current_question_index]
        self.current_question_index += 1
        q_text = self.questions_list[self.current_question_index].question
        return q_text

    def get_list(self):
        return self.questions_list