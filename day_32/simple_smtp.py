import smtplib
my_email = "your_email@gmail.com"
password = "put from your App password (in Security) ... Go to https://myaccount.google.com/"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email ,password=password)
connection.sendmail(from_addr=my_email, to_addrs="agrobioconstruct@gmail.com", msg="Subject: Hello\n\nThis is the body of the email.")

connection.close()
