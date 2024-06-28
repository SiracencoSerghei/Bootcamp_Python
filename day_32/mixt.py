
import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "my_email@gmail.com"
MY_PASSWORD = "my_passwd"

def conn_msg():
	conection = smtplib.SMTP("smtp.gmail.com", 587)
	with conection as conection:
		conection.starttls()
		conection.login(user=MY_EMAIL, password=MY_PASSWORD)
		conection.sendmail(
			from_addr=MY_EMAIL,
			to_addrs="receiver@gmail.com",
			msg=f"Subject:Monday Motivation\n\n {quote}")

#
# today = dt.datetime.now()

# for testing code:
today = "1961-12-21"
today = dt.datetime.strptime(today, "%Y-%m-%d")
# print(today)

weekday = dt.datetime.now()
# weekday = 1
if weekday == 1:
	with open("quotes.txt") as quote_file:
		all_quotes = quote_file.readlines()
		quote = random.choice(all_quotes)
		conn_msg()
	print(quote)
	# print(all_quotes)

