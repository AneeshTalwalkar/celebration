import tkinter as tk

root = tk.Tk()
root.geometry("800x500")
root.title("GUI PYTHON")

def update_labels():
    name = oneline.get()
    label.config(text=f'Your name is: {name}')

    text = textbox.get("1.0", tk.END).strip()  # Get text from the start to the end of the textbox
    label2.config(text=f'You entered: {text}')


label= tk.Label(root,text="What is your name??",font=("Arial",18))#Prints text 
label.pack(padx=20,pady=20)

oneline = tk.Entry(root,fg="green")#Makes a textbox with one line limit
oneline.pack()

label2= tk.Label(root,text="What is your message:",font=("Arial",18))#Prints text 
label2.pack(padx=20,pady=20)

textbox= tk.Text(root,height=3,font=("Arial",15),fg="green")#creats space for writing text by the user.
textbox.pack(padx=10,pady=10)


button= tk.Button(root,text="Submit",font=("Arial",10),command=update_labels)
button.pack(padx=30, pady=10)

root.mainloop()
