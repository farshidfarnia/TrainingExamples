from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="My_city")
location = geolocator.geocode("Tehran")
print((f"latitude is: {location.latitude} and longitude is: {location.longitude}"))