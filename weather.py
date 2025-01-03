#!/usr/bin/env python3

import requests

API_KEY = "bd5e3a2932cd74617229050658d09964"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"  # Base URL without placeholders

def get_weather(city_name):
    params = {
        "q": city_name,   # Pass city name here
        "appid": API_KEY,  # Pass the API key here
        "units": "metric"  # Temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {weather.capitalize()}")
    else:
        print("Error: Unable to fetch weather data.")

if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    get_weather(city)
