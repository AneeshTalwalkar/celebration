import tkinter as tk

root = tk.Tk()
root.title("Simple Canvas Example")
root.geometry("500x500")

#Canvas
canvas = tk.Canvas(root,width=400, height=400, bd=2, highlightthickness=2, highlightbackground="green")
canvas.pack(anchor='s')

def rect():
    canvas.create_rectangle(50, 50, 150, 150, fill="blue")

def circ():
    canvas.create_oval(200, 200, 300, 300, fill="red")


label = tk.Label(root,text="What do you want to be drawn?",font=("Cascadia Mono",20))
label.pack(pady=5,padx=5)


button1 = tk.Button(root,text="Rectangle",font=("Cascadia Mono",19),command=rect)
button1.pack(pady=2,padx=2)
button2 = tk.Button(root,text="Circle",font=("Cascadia Mono",19),command=circ)
button2.pack(pady=2,padx=2)


root.mainloop()
