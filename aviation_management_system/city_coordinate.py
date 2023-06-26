from geopy.geocoders import Nominatim


def get_coordinates(city):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(city)

    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        print(f"Le coordinate di {city} sono: {latitude}, {longitude}")
        return latitude, longitude
    else:
        return None

get_coordinates("NAP")