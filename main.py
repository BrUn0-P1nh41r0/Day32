import random
import smtplib
import datetime as dt

my_email="testpython382@gmail.com"
password="esze crrh jcgx vvdt"

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt", mode= "r") as file:
    quotes = file.readlines()
    quote = random.choice(quotes)

if day_of_week == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="bpinheiro44@yahoo.com",
                            msg=f"Subject:Quote of the week\n\n{quote}")
