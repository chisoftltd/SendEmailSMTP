import smtplib

my_email = 'python.chinwe@gmail.com'
pwd = 'pyt@#chinwe'

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=pwd)
# connection.sendmail(from_addr=my_email,
#                     to_addrs='gnexplore@gmail.com',
#                     msg="Subject:Hello\n\n"
#                     "I am testing sending email with python")
# connection.close()

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=pwd)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='gnexplore@gmail.com',
#                         msg="Subject:Hello\n\n"
#                         "I am testing sending email with python")

import datetime as dt

now = dt.datetime.now()
year = now.year
print(year)
month = now.month
print(month)
weekday = now.weekday()
print(weekday)
day = now.day()
print(day)
min = now.minute()
print(min)
