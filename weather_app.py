import requests

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=15)
        data = response.json()

        if response.status_code == 200:
            print("\n========== WEATHER REPORT ==========")
            print("City:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Feels Like:", data["main"]["feels_like"], "°C")
            print("Weather:", data["weather"][0]["description"].title())
            print("Humidity:", data["main"]["humidity"], "%")
            print("Wind Speed:", data["wind"]["speed"], "m/s")
            print("====================================")

        else:
            print("Error:", data.get("message", "Unable to get weather information."))

    except requests.RequestException:
        print("Network error. Please check your internet connection.")

    except (KeyError, ValueError):
        print("Unable to read weather information. Please try again.")


def main():
    print("================================")
    print("       LIVE WEATHER APP")
    print("================================")

    while True:
        city = input("\nEnter city name (or type exit): ").strip()

        if city.lower() == "exit":
            print("Thank you for using the Weather App!")
            break

        if not city:
            print("Please enter a city name.")
            continue

        if API_KEY == "YOUR_API_KEY_HERE":
            print("Please add your OpenWeather API key to the code first.")
            break

        get_weather(city)


if __name__ == "__main__":
    main()