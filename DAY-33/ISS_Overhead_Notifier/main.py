import requests
from datetime import datetime
from send_mail import send_mail

MY_LAT = 11.999970
MY_LONG = 8.534860

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def position(lat, long, iss_lat, iss_long):
    if abs(lat - iss_lat) <= 5 and abs(long - iss_long) <= 5:
        return True
    return False

def is_dark(current_hour, sunrise_hour, sunset_hour):
    if current_hour >= sunrise_hour and current_hour < sunset_hour:
        return False
    return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
if position(MY_LAT, MY_LONG, iss_latitude, iss_longitude) and is_dark(
    current_hour=time_now, sunrise_hour=sunrise, sunset_hour=sunset
):
    message = "Look up! The ISS will be over you shortly."
    send_mail(message=f"Subject:ISS Overhead Notification\n\n{message}")
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



