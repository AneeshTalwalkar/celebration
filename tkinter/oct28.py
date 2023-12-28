import tkinter as tk
from tkinter import ttk

i=0
x1,y1=0,0
x2,y2 = 0,0

#Draws line
def on_canvas_click(event):
    global i,x1,y1,x2,y2
    if i==0:
        x1, y1 = event.x, event.y
        print(f"Clicked at coordinates: ({x1}, {y1})")
        i=i+1
    else:
        x2, y2 = event.x, event.y
        print(f"Clicked at coordinates: ({x2}, {y2})")
        canvas.create_line(x1, y1, x2, y2, fill=current_colour, width=2)
        i=0


#main window
root = tk.Tk()
root.title("Line drawer")
root.geometry("500x550")
values = ["Red", "Blue", "Green", "Black","Orange","Purple","Grey"]
color_choice = ttk.Combobox(root, values=values,font=("Cascadia Mono",20))
color_choice.pack(pady=30)
current_colour = "Red"

canvas = tk.Canvas(root, width=400, height=400,bd=2,highlightbackground="green")
canvas.pack()


#edits the current_colour
def on_selection(event):
    global current_colour
    current_colour = color_choice.get()
    print(current_colour)

color_choice.bind("<<ComboboxSelected>>", on_selection)    
canvas.bind("<Button-1>", on_canvas_click)

root.mainloop()
