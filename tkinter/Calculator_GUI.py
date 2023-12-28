import tkinter as tk

root = tk.Tk()
root.geometry("900x500")
root.title("Calculator")
root.configure(bg="#000000")

def evaluation():
    question = textbox.get()
    try:
        answer = eval(question)
        print(answer)
        label2.config(text=f'Answer={answer}',fg="#00FF00")
    except Exception as e:
        print(f"Error: {e}")
        label2.config(text=f'Error:{e}', fg="#FF0000")

label1 = tk.Label(root, text="Calculator", font=("Comic Sans MS", 27), fg="#00FFFF", bg="#000000")
label1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

expression_label = tk.Label(root, text="Enter your expression here:", font=("Cascadia Mono", 20), bg="#000000", fg="#808080")
expression_label.grid(row=1, column=0, padx=(10, 0), sticky='e')

textbox = tk.Entry(root, font=("Cascadia Mono", 19), bg="#000000", fg="#808080")
textbox.grid(row=1, column=1, padx=(0, 10), pady=10, sticky='w')

evaluate = tk.Button(root, text="evaluate", font=("Arial", 20), command=evaluation, bg="#000000", fg="#FFFFFF", width=7,height=1)
evaluate.grid(row=1, column=2, columnspan=3)

label2 = tk.Label(root, text="Hello there", font=("Cascadia Mono", 19), bg="#000000", fg="#00FF00")
label2.grid(row=3, column=0, columnspan=3, padx=5, pady=0, sticky='w')

print("Answers log:\n")

root.mainloop()
