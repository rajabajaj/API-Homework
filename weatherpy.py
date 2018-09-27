# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import datetime
from pprint import pprint
# Import API key

from api_keys import api_keys
# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy


# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)



# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0],lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


  print("Beginning Data Retrieval")
    print("------------------------------")

for x in range(len(cities)):
    
      print(f"Processing Record {x} of City | {cities[x]}")
        


latitude = []
temp = []
humid = []
cloud = []
wind_sp = []
city_name =[]
country = []
max_temp = []
date = []
longitude = []

url =  "http://api.openweathermap.org/data/2.5/weather?"
units = "metric"
# Build partial query URL
query_url = f"{url}appid={api_keys}&units={units}&q="

for city in cities:
    
    try:
        response = requests.get(query_url + city).json()
        latitude.append(response["coord"]["lat"])
        longitude.append(response["coord"]["lon"])
        temp.append(response['main']['temp'])   
        humid.append(response['main']['humidity'])
        cloud.append(response['clouds']['all'])
        wind_sp.append(response['wind']['speed'])
        city_name.append(response['name'])
        country.append(response['sys']['country'])
        max_temp.append(response['main']['temp_max'])
        date.append(response['dt'])
    except:
        
        pass


weatherpy_dict = {
    "City":city_name,
    "Country": country,
    "Date":date,
    "Latitude": latitude,
    "Longitude": longitude,
    "Temperature": temp,
    "Humidity":humid,
    "Cloudiness": cloud,
    "Wind Speed" : wind_sp, 
    "Max Temp": max_temp
}
weatherpy_data = pd.DataFrame(weatherpy_dict)
weatherpy_data.head()

weatherpy_data.to_csv("weatherpy.csv", encoding="utf-8", index=False)
weatherpy_data.count()


#Latitude vs. Temperature Plot

currentDT = datetime.datetime.now()
time = currentDT.strftime("%m/%d%/%Y")
plt.scatter(weatherpy_data["Latitude"],weatherpy_data["Max Temp"],marker ="o",
            color ="lightblue", edgecolors = "black")
plt.xlabel("Latitude")
plt.ylabel("Max Temperature (C)")
plt.title(f"City Latitudes V/s Max Temperatures {time}")
plt.grid()


# Latitude vs. Humidity Plot

currentDT = datetime.datetime.now()
time = currentDT.strftime("%m/%d%/%Y")
plt.scatter(weatherpy_data["Latitude"],weatherpy_data["Humidity"],marker ="o",
            color ="lightblue", edgecolors = "black")
plt.xlabel("Latitude")
plt.ylabel("Max Temperature (C)")
plt.title(f"City Latitudes V/s Max Temperatures {time}")
plt.grid()

#Latitude vs. Cloudiness Plot

currentDT = datetime.datetime.now()
time = currentDT.strftime("%m/%d%/%Y")
plt.scatter(weatherpy_data["Latitude"],weatherpy_data["Cloudiness"],marker ="o",
            color ="lightblue", edgecolors = "black")
plt.xlabel("Latitude")
plt.ylabel("Max Temperature (C)")
plt.title(f"City Latitudes V/s Max Temperatures {time}")
plt.grid()

#Latitude vs. Wind Speed Plot

currentDT = datetime.datetime.now()
time = currentDT.strftime("%m/%d%/%Y")
plt.scatter(weatherpy_data["Latitude"],weatherpy_data["Wind Speed"],marker ="o",
            color ="lightblue", edgecolors = "black")
plt.xlabel("Latitude")
plt.ylabel("Max Temperature (C)")
plt.title(f"City Latitudes V/s Max Temperatures {time}")
plt.grid()


