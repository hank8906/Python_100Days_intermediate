import requests
from datetime import datetime
import smtplib

my_email = "huanghank8906@gmail.com"
password = "xwcczfmjyoudaave"

MY_LAT = 25.032969
MY_LONG = 121.565414

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


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

sunrise_utc_plus_8 = sunrise + 8
sunset_utc_plus_8 = sunset + 8
print(sunset_utc_plus_8)

hour_now = datetime.now().hour
print(hour_now)


def is_dark():
    if sunrise_utc_plus_8 >= hour_now >= sunset_utc_plus_8:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


lat_dif = abs(iss_latitude - MY_LAT)
long_dif = abs(iss_longitude - MY_LONG)
if lat_dif < 5 and long_dif < 5 and is_dark():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="huanghank2000@myyahoo.com",
                            msg="Subject:ISS overhead alert!!!\n\n"
                                "Look up the sky, ISS is flying through your head!")

