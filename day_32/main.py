# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import random
import smtplib
from datetime import datetime

import pandas

MY_EMAIL = "siracencoserghei@gmail.com"
MY_PASSWORD = "lhdpwzqnwtzbblox"
#
# today = datetime.now()

# for testing code:
today = "1961-12-21"
# today = "1978-02-09"
today = datetime.strptime(today, "%Y-%m-%d")
print(today)

today_tuple = (today.month, today.day)
print("++++++++++++++++++++++")
print(f"{today_tuple = }")
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}
print("++++++++++++++++++++++")
print(f"{birthdays_dict = }")
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    print("++++++++++++++++++++++")
    print(birthday_person)
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    conection = smtplib.SMTP("smtp.gmail.com", 587)  # for gmail

    # with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
    with conection as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}",
        )
