# Amazon Price Tracker Project
import requests
import smtplib
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

EMAIL_PROVIDER_SMTP_ADDRESS = os.environ.get("EMAIL_PROVIDER_SMTP_ADDRESS")
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_EMAIL_PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")
print(EMAIL_PROVIDER_SMTP_ADDRESS, MY_EMAIL, MY_EMAIL_PASSWORD)

url = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_2?dib=eyJ2IjoiMSJ9.-tHZU6eErHJPLUX3N7J32IPJvfF9jMyqUv6rpC1cCZ1nnE2IG8y3oRIfhCgKAFqaGprHB-bo524cur2zGxSDzr1ATwkz1gTkwyLTvr4_y5diyZuh4-rwefxNP8W5oFVlJ-ouwsG0wXPc28w63O07fcMNyBuBcFtEbPzcGxDtnYuDZfozN_iQ0cCW5PkLDQ9eCHF-qwTRqTPLgsK9rF82HDX9_Y1c9QnFnaR6rlu6t2A.mGiDtRMRfB81lQiv96HNQSYSTyzrizSL2HIlUFUZ7pI&dib_tag=se&keywords=Pot%2BDuo%2BPlus&qid=1720822710&sr=8-2&th=1"

response = requests.get(url, headers  ={  "Accept-Language"  :  "en-US"  })

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

price_whole = soup.find(class_="a-price-whole").get_text().split()[0]
price_fraction = soup.find(class_="a-price-fraction").get_text().split()[0]
price = f"{price_whole}{price_fraction}"
price = float(price)
print(price)


title = soup.find(id="productTitle").get_text().strip()
BUY_PRICE = 200
if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"))


       