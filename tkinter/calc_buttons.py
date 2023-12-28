import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for display
entry = tk.Entry(root,text="",font=('Arial', 20),width=15,)
entry.grid(row=0, column=0, columnspan=4, padx=1, pady=10)

def add_number_to_entry(number):
    current_text = entry.get()
    entry.delete(0, tk.END)  # Clear current text
    entry.insert(0, current_text + str(number))  # Append the number pressed

def evaluate():
    question = entry.get()
    try:
        answer = eval(question)
        print(answer)
        entry.delete(0, tk.END) 
        entry.insert(0,answer)
    except Exception as e:
        print(f"Error: {e}")
        entry.delete(0,tk.END)
        entry.insert(0,f'Error')

def clear():
    entry.delete(0, tk.END)# Clear current text

# Number buttons
btn1 = tk.Button(root, text="1", width=5, height=2, command=lambda: add_number_to_entry(1)).grid(row=1, column=0)
btn1 = tk.Button(root, text="2", width=5, height=2, command=lambda: add_number_to_entry(2)).grid(row=1, column=1)
btn1 = tk.Button(root, text="3", width=5, height=2, command=lambda: add_number_to_entry(3)).grid(row=1, column=2)
btn1 = tk.Button(root, text="4", width=5, height=2, command=lambda: add_number_to_entry(4)).grid(row=2, column=0)
btn1 = tk.Button(root, text="5", width=5, height=2, command=lambda: add_number_to_entry(5)).grid(row=2, column=1)
btn1 = tk.Button(root, text="6", width=5, height=2, command=lambda: add_number_to_entry(6)).grid(row=2, column=2)
btn1 = tk.Button(root, text="7", width=5, height=2, command=lambda: add_number_to_entry(7)).grid(row=3, column=0)
btn1 = tk.Button(root, text="8", width=5, height=2, command=lambda: add_number_to_entry(8)).grid(row=3, column=1)
btn1 = tk.Button(root, text="9", width=5, height=2, command=lambda: add_number_to_entry(9)).grid(row=3, column=2)
btn1 = tk.Button(root, text="0", width=5, height=2, command=lambda: add_number_to_entry(0)).grid(row=4, column=0)
btn1 = tk.Button(root, text=".", width=5, height=2, command=lambda: add_number_to_entry('.')).grid(row=4, column=1)

# Operation buttons
btn_add = tk.Button(root, text="+", width=5, height=2, command=lambda:add_number_to_entry("+")).grid(row=1, column=3)
btn_sub = tk.Button(root, text="-", width=5, height=2, command=lambda:add_number_to_entry("-")).grid(row=2, column=3)
btn_mul = tk.Button(root, text="*", width=5, height=2, command=lambda:add_number_to_entry("*")).grid(row=3, column=3)
btn_div = tk.Button(root, text="/", width=5, height=2, command=lambda:add_number_to_entry("/")).grid(row=4, column=3)
btn_div = tk.Button(root, text="^", width=5, height=2, command=lambda:add_number_to_entry("**")).grid(row=4, column=0)
btn_equal = tk.Button(root, text="=", width=5, height=2, command=evaluate).grid(row=5, column=3)

btn_ac = tk.Button(root,text="AC",width=5,height=2,command=clear).grid(row=4,column=2)

root.mainloop()

