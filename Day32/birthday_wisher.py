import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# Function to send email
def send_birthday_email(to_email, subject, body):
    from_email = "your_email@gmail.com"  # Replace with your email
    password = "your_email_password"  # Replace with your email password

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"Birthday wish sent to {to_email}!")
    except Exception as e:
        print(f"Error: {e}")

# List of birthdays (name, email, birthdate)
birthdays = [
    {"name": "John", "email": "john@example.com", "birthdate": "2000-12-23"},
    {"name": "Alice", "email": "alice@example.com", "birthdate": "1995-12-23"}
]

# Get the current date
today = datetime.date.today()

# Check if today is anyone's birthday and send them a message
for person in birthdays:
    birthdate = datetime.datetime.strptime(person["birthdate"], "%Y-%m-%d").date()
    if today.month == birthdate.month and today.day == birthdate.day:
        subject = f"Happy Birthday, {person['name']}!"
        body = f"Dear {person['name']},\n\nWishing you a very happy birthday! Have a fantastic day!\n\nBest regards,\nYour Automated System"
        send_birthday_email(person['email'], subject, body)