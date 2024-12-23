'''
Topics to be Covered:
- Google SMTP Port
- How to send Emails with Python using SMTP
- Working with datetime module
- Project- Automated Birthday Wisher Project
- Run your Python code in the Cloud
'''

# SMTP: Simple Mail Transfer Protocol
import smtplib

my_email = "lakrapayal307@gmail.com"
password = "PayalLakra@307"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="payallakra307@gmail.com",
        msg="Subject:Hello\n\nThis is the SMTP."
    )

import datetime

now = datetime.datetime.now()
year = now.year

# To Host our code in the Cloud and run it on every single day we can use service called -- Python anywhere.
# Sign In < Upload files < On consoles create a new Bash Console < type python filename.py < set time also.