import requests
from pprint import pprint

API_key = '5df2cee2682f7d92703c43a2903986bc'

city = input("Enter the name of a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city

waether_data = requests.get(base_url).json()

pprint(waether_data)