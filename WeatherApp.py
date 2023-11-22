import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image,ImageTk
import ttkbootstrap


# function to get weather
def get_weather(city):
    API_key = "45969ccc50bafbdf982089d87612d14f"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error","The city not found")
        return None
    # Parse the response to get weather information
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description =weather['weather'][0]['description']
    city = weather['name']
    country =weather['sys']['country']

    # Get the icon URL and return all weather information
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)



#Search the desired city
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # In case the city has been found unpack weather information:
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{country}, {city}")

    # Get the icon image from the URL
    image = Image.open(requests.get(icon_url,stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # Update the temprature and description labels
    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")
root = ttkbootstrap.Window(themename="morph")
root.title("My first weather app")
root.geometry("400x400")

# Enter city name
city_entry = ttkbootstrap.Entry(root,font="Helvetica, 18")
city_entry.pack(pady=10)

# Button -> to search for weather information
search_button = ttkbootstrap.Button(root,text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

#Label -> to show the city/country name
location_label = tk.Label(root,font="Helvetica, 25")
location_label.pack(pady=20)

#Label -> show weather icon
icon_label = tk.Label(root)
icon_label.pack()

#Label -> to show the temperature
temperature_label = tk.Label(root,font="Helvetica, 20")
temperature_label.pack()

#Label -> to show the weather description
description_label = tk.Label(root,font="Helvetica, 20")
description_label.pack()

root.mainloop()
