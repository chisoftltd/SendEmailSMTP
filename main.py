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

with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as connection:
    connection.starttls()
    connection.login(user=my_email, password=pwd)
    connection.sendmail(from_addr=my_email,
                        to_addrs='gnexplore@gmail.com',
                        msg="Subject:Hello\n\n"
                        "I am testing sending email with python")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)
# month = now.month
# print(month)
# weekday = now.weekday()
# print(weekday)
#
# # User datetime object
# date_of_brith = dt.datetime(year=1972, month=11, day=30, hour=19)
# print(date_of_brith)