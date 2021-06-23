import requests
from datetime import datetime

api_key = '1c87cfda226dc2aadd1d18edaa4e6cb9'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

list = [temp_city, weather_desc, hmdt, wind_spd, date_time]
with open("weather.txt",'w') as f:
    f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    f.write("\nCurrent temperature is : {:.2f}°C ".format(list[0]))
    f.write("\nCurrent weather desc   : {:s}".format(list[1]))
    f.write("\nCurrent Humidity       : {:d}%".format(list[2]))
    f.write("\nCurrent wind speed is  : {:.2f}kmph " .format(list[3]))
    f.close()