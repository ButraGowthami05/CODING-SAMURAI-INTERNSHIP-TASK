import requests

city = "kurnool"
api_key = "b3f1cdab5e4c487f20b3b2e747d334fe"  

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

data = requests.get(url).json() #To get whether report in json format

if data["cod"] == 200: 
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("City not found!")
