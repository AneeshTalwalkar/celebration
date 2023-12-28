import tkinter as tk
from tkinter import messagebox

def check_answer():
    selected_option = var.get()
    if selected_option == correct_answer:
        result_label.config(text="Correct!",fg="#00FF00")
    else:
        result_label.config(text="Incorrect!",fg="#FF0000")


root = tk.Tk()
root.title("MCQ Quiz")
root.geometry("800x500")
# Creates a StringVar() to hold the value of the selected radio button
var = tk.StringVar()

#QnA
question = "Q: What is the capital of India?"
answers = ["Pune", "Antarctica", "Moscow", "New Delhi"]
correct_answer = "New Delhi"

question_label = tk.Label(root, text=question,font=("Cascadia Mono",20))
question_label.pack(anchor='w')

#radio buttons for each answer
for answer in answers:
    rb = tk.Radiobutton(root, text=answer, variable=var, value=answer)
    rb.pack(anchor='w')

submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(anchor='w')

result_label = tk.Label(root, text="",font=("Cascadia Mono",19))
result_label.pack()


root.mainloop()
