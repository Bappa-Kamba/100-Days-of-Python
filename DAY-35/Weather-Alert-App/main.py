import requests
from twilio.rest import Client
import os

MY_LAT = 11.999970
MY_LONG = 8.534860

endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get('OWM_API_KEY')
app_sid = os.environ.get('APP_SID')
auth_token = os.environ.get('AUTH_TOKEN')
print(app_sid)
print(auth_token)

client = Client(app_sid, auth_token)

parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : api_key,
    "exclude" : "current,minutely,daily"
}

response = requests.get(url=endpoint, params=parameters)
weather_data = response.json()['hourly']

weather_code = weather_data[0]['weather'][0]['id']
weather_forecast = [forecast_weather['weather'][0]['id'] for forecast_weather in weather_data[:12]]

will_rain = False
for code in weather_forecast:
    if code < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
                                body='Hello there!\nBe sure to bring an umbrella☂️. High possiblity of rainfall.',
                                from_='whatsapp:+14155238886',
                                to='whatsapp:+2348136384068'
                            )
    print(message.sid)
    