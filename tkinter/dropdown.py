import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

root = tk.Tk()
root.title("city time")
root.geometry("800x500")

label= tk.Label(root,text="Choose a city:",font=("Cascadia Mono",20))
label.pack(pady=10)

# Creates drop down menu
values = ["New York", "Stockholm", "Pune", "Tokyo"]
combo = ttk.Combobox(root, values=values,font=("Cascadia Mono",20))
combo.pack(pady=30)

label2= tk.Label(root,text="",font=("Cascadia Mono", 19))

# Timezone calculations for the cities reletive to UTC
city_timezones = {
    "New York": -5,
    "Stockholm": 1,
    "Pune": 5.5, 
    "Tokyo": 9, 
}

# Define callback function
def on_selection(event):
    selected_option = combo.get()
    utc_offset = city_timezones.get(selected_option)
    if utc_offset is not None:
        local_time = datetime.utcnow() + timedelta(hours=utc_offset)
        time_str = local_time.strftime('%d-%m-%Y, %H:%M')
        label2.config(text=f'Current time in {selected_option.title()}: {time_str}')
        label2.pack()
    else:
        label2.config(text=f"No timezone information available for {selected_option}",fg="#FF0000")
        label2.pack()
combo.bind("<<ComboboxSelected>>", on_selection)

root.mainloop()
