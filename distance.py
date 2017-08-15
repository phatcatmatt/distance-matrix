import googlemaps
from datetime import datetime
from keys import maps_key

gmaps = googlemaps.Client(key=maps_key)

matrix_response = gmaps.distance_matrix("Provo, Utah", "Salt Lake City, Utah")

print (matrix_response)

# {'destination_addresses': ['Salt Lake City, UT, USA'], 'origin_addresses': ['Provo, UT, USA'], 'rows': [{'elements': [{'distance': {'text': '71.8 km', 'value': 71838}, 'duration': {'text': '46 mins', 'value': 2768}, 'status': 'OK'}]}], 'status': 'OK'}