##################### Extra Hard Starting Project ######################
import random
import smtplib
import pandas as pd
import datetime as dt

my_email = "huanghank8906@gmail.com"
password = "xwcczfmjyoudaave"

# Check if today matches a birthday in the birthdays.csv
df_birth = pd.read_csv("birthdays.csv")

birth_month = df_birth.month.astype(int)
result_month = birth_month.values[0]

birth_day = df_birth.day.astype(int)
result_day = birth_day.values[0]

now = dt.datetime.now()

now_month = now.month
now_day = now.day

if now_month == result_month and now_day == result_day:
    # 3. If step 2 is true, pick a random letter from letter templates and
    # replace the [NAME] with the person's actual name from birthdays.csv

    letter_id = random.randint(1, 3)
    with open(f"./letter_templates/letter_{letter_id}.txt") as letter_file:
        content = letter_file.read()

        new_name = df_birth.name.values[0]
        new_content = content.replace('[NAME]', new_name)
        # print(new_content)

    # 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="whatspooh@gmail.com",
                            msg="Subject:Happy Birthday Baby!!!\n\n"
                                f"{new_content}")


