##################### Hard Starting Project ######################
# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "testpython382@gmail.com"
MY_PASSWORD = ""

today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthdays = pandas.read_csv("./birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in birthdays.iterrows()}

if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    random_letter = random.randint(1,3)
    with open(f"./letter_templates/letter_{random_letter}.txt") as letter:
        letter_chosen = letter.read()
        letter_name = letter_chosen.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthdays_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{letter_name}")
