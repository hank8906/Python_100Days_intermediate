import requests
from twilio.rest import Client

account_sid = 'ACb11594d29dcb561abc33f736a3debb9b'
auth_token = '86a1ecd3e18e3ba60e41771ce691a25a'

response = requests.get(url="http://api.weatherapi.com/v1/forecast.json?"
                            "key=44137c0d82254005af0152650230109&q=Kaohsiung&days=1&aqi=no&alerts=no")
response.raise_for_status()

hour_data = response.json()["forecast"]["forecastday"][0]["hour"]

# print(response.json()["forecast"]["forecastday"][0]["hour"])

will_rain = False
for hour in hour_data:
    if hour["condition"]["code"] == 1240 or hour["condition"]["code"] == 1063 or hour["condition"]["code"] == 1183:
        print(hour["time"])
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain this hour.Please remember to bring the umbrella.",
        from_='+12563051618',
        to='+886960063863'
    )

    print(message.status)


