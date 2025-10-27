import tkinter
from tkinter import *

import questions
from questions import Questions
from quizzbrain import QuizBrain

class Ui:
    def __init__(self, quizbrain:QuizBrain):
        self.quizbrain = quizbrain
        self.window = Tk()
        self.window.title("QUIZZ GAME")
        self.window.config(padx=20, pady=20)

        #Create the True button
        self.true_button = Button(text="True", width=15, height=2, fg="black", highlightbackground="green", command=self.true_question)
        self.true_button.grid(row = 1, column = 0, pady=20)

        #Create the False button
        self.false_button = Button(text="False", width=15, height=2, fg="black", highlightbackground="red", command=self.false_question)
        self.false_button.grid(row = 1, column = 1, pady=20)

        #Create the question Window
        self.canvas = Canvas(self.window, width=400, height=400, bg="white")
        self.question_text = self.canvas.create_text(200,200,width=200, text="RANDOM TEXT", font=("Arial", 25, "bold"), fill="black")
        self.canvas.grid(row= 0, column = 0, columnspan=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def true_question(self):
        right_question = self.quizbrain.check_answer("True")
        self.give_feedback(right_question)

    def false_question(self):
        false_question = self.quizbrain.check_answer("False")
        self.give_feedback(false_question)

    def give_feedback(self, question_answer):
        if question_answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quizbrain.still_has_questions():
            q_text = self.quizbrain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            # Disable buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

