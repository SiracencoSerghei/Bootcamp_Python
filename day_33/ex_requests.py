import requests

url_response = requests.get("http://api.open-notify.org/iss-now.json")
url_response.raise_for_status()

# print(url_response)
# print(url_response.status_code)
# print(url_response.headers)
# print(url_response.raise_for_status())
print(url_response.json())

data = url_response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
#
# lat, lng = iss_position
# sun_response = requests.get("https://api.sunrise-sunset.org/json?lat={lat}&lng={lgn}")
# sun_response.raise_for_status()
# # print(sun_response.json())
# sun_rise = sun_response.json()["results"]["sunrise"]
# sun_set = sun_response.json()["results"]["sunset"]
# print(sun_rise, sun_set, sep=", ", end="\n")

parameters = {
    "lng": iss_position[0],
    "lat": iss_position[1],
}
print(parameters)
sun_response = requests.get("https://api.sunrise-sunset.org/json?lat={lat}&lng={lgn}")
