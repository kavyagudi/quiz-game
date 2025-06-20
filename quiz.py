import tkinter as tk
from tkinter import messagebox

# Questions and Answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which is the largest ocean?",
        "options": ["Indian", "Pacific", "Atlantic", "Arctic"],
        "answer": "Pacific"
    },
    {
        "question": "Which language is used in web design?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    }
]

class QuizApp:
    def __init__(self, master):
        self.master = master
        master.title("Quiz App")

        self.q_no = 0
        self.score = 0

        self.question_label = tk.Label(master, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options = []

        for i in range(4):
            btn = tk.Radiobutton(master, text="", variable=self.var, value="", font=("Arial", 12))
            btn.pack(anchor="w", padx=20)
            self.options.append(btn)

        self.submit_btn = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_btn.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.q_no < len(questions):
            q = questions[self.q_no]
            self.question_label.config(text=q["question"])
            self.var.set(None)
            for i, option in enumerate(q["options"]):
                self.options[i].config(text=option, value=option)
        else:
            self.show_result()

    def check_answer(self):
        selected = self.var.get()
        if selected == "":
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        correct = questions[self.q_no]["answer"]
        if selected == correct:
            self.score += 1
        self.q_no += 1
        self.load_question()

    def show_result(self):
        messagebox.showinfo("Quiz Finished", f"Your Score: {self.score}/{len(questions)}")
        self.master.quit()

# Start the app
root = tk.Tk()
app = QuizApp(root)
root.mainloop()