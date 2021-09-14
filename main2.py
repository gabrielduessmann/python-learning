import requests

city = input("Type a city name: ")

response = requests.get("https://goweather.herokuapp.com/weather/"+city)

if response is None:
    print("No response")
elif response is not None:
    print(response.json())