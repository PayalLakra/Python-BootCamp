import smtplib
import datetime as dt
import random

MY_EMAIL = "payal07@gmail.com"
MY_PASSWORD = "xxxxxxxx@888"

now = dt.datetime.now()
weekday = now.weekday()
print(f"Today's weekday: {weekday}")

if True:  # Change to `if weekday == 1:` to match Tuesday logic
    try:
        with open("C:\\Users\\PAYAL\\Desktop\\Payal STUDY\\Python-BootCamp\\Day32\\quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes).strip()

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.set_debuglevel(1)  # Debug output
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Tuesday Motivation\n\n{quote}"
            )
        print("Email sent successfully!")
    except FileNotFoundError:
        print("Error: The file 'quotes.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")