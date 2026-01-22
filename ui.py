from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            anchor=CENTER,
            font=FONT,
            fill=THEME_COLOR,
            text="Welcome to Quizler",
            width=280
        )

        self.text = Label(text="Score: 0", font=FONT, bg=THEME_COLOR)
        self.text.grid(row=0,column=1)

        true_icon = PhotoImage(file="images/true.png")
        false_icon = PhotoImage(file="images/false.png")

        self.true = Button(image=true_icon, command=self.answered_true)
        self.true.grid(row=2, column=0)

        self.false = Button(image=false_icon, command=self.answered_false)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true.config(state=DISABLED)
            self.false.config(state=DISABLED)
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have reached the end of the quiz!"
                                        f"\n\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")

    def answered_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answered_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.text.configure(text=f"Score: {self.quiz.score}")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.text.configure(text=f"Score: {self.quiz.score}")
            self.window.after(1000, self.get_next_question)