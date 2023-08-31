import smtplib
import datetime as dt
import random
my_email = "huanghank8906@gmail.com"
password = "xwcczfmjyoudaave"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt") as file:
        quotes_list = file.readlines()
        friday_quotes = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="huanghank2000@myyahoo.com",
                            msg="Subject:Friday's quotes\n\n"
                                f"{friday_quotes}")






