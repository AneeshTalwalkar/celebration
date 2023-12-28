import tkinter as tk
from datetime import datetime, timedelta, timezone

class time_now:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Clock")
        self.root.geometry("800x500")
        
        self.label = tk.Label(root, text="", font=("Arial", 100))
        self.label.pack(pady=20)
        
        #button to show New York City time
        self.nyc_button = tk.Button(root, text="Show New York Time", command=self.show_nyc_time)
        self.nyc_button.pack(pady=20)
        
        self.showing_nyc_time = False
        self.update_clock() # First update to the clock
        
    def update_clock(self):
        if self.showing_nyc_time:
            # Calculate New York City time
            nyc_time = datetime.now(timezone.utc) - timedelta(hours=4)
            current_time = nyc_time.strftime('%H:%M:%S')
        else:
            # Display local time
            current_time = datetime.now().strftime('%H:%M:%S')
        
        self.label.config(text=current_time)
        self.root.after(1000, self.update_clock)
        
    def show_nyc_time(self):
        self.showing_nyc_time = True

root = tk.Tk()
app = time_now(root)
root.mainloop()
