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


from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def calcola_orario_arrivo(citta1, citta2):
    """
    Calcolo l'orario di arrivo basato sulla distanza tra 2 città
    :param citta1:
    :param citta2:
    :return:
    """
    geolocatore = Nominatim(user_agent="distanza_tra_citta")

    # Ottieni le coordinate geografiche della prima città
    posizione_citta1 = geolocatore.geocode(citta1)
    latitudine_citta1 = posizione_citta1.latitude
    longitudine_citta1 = posizione_citta1.longitude

    # Ottieni le coordinate geografiche della seconda città
    posizione_citta2 = geolocatore.geocode(citta2)
    latitudine_citta2 = posizione_citta2.latitude
    longitudine_citta2 = posizione_citta2.longitude

    # Calcola la distanza geodetica tra le due città
    distanza = geodesic((latitudine_citta1, longitudine_citta1), (latitudine_citta2, longitudine_citta2)).kilometers

    tempo_totale_volo=distanza/800+0.30

    ore = int(tempo_totale_volo)
    minuti_decimali = tempo_totale_volo - ore
    minuti = int(minuti_decimali * 60)

    print(f"{ore:02d}:{minuti:02d}")
    tempo_di_volo=f"{ore:02d}:{minuti:02d}"
    return tempo_di_volo

