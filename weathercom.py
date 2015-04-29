#!/usr/bin/env python3
import pywapi

#city = input("Enter city name: ")

location = pywapi.get_location_ids('astoria')

for i in location:
    location_id = i

weather = pywapi.get_weather_from_weather_com(location_id, 'imperial')

print weather
