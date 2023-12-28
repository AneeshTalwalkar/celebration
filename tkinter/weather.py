import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.city_entry = tk.Entry(root, font=('normal', 20))
        self.city_entry.pack(pady=20)

        self.get_weather_btn = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_btn.pack()

        self.weather_label = tk.Label(root, font=('normal', 15))
        self.weather_label.pack(pady=20)

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            try:
                response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=38dfe8cc4c97796febbd37493486d608&units=metric")
                data = response.json()
                main = data['main']
                weather = data['weather'][0]
                temp = main['temp']
                description = weather['description']
                final_str = f'Weather in {city}: {temp}°C, {description}'
                self.weather_label.config(text=final_str)
            except:
                messagebox.showerror("Error", "Cannot fetch weather data for the given city.")
        else:
            messagebox.showwarning("Warning", "Please enter a city name.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
