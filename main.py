import weather
import mailer

def get_emails():
    # Reading emails from a file
    emails = {}

    try:
        email_file = open('emails.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()

    except FileNotFoundError as err:
        print(err)

    return emails

def get_message():
    # Reading our message from a file
    try:
        message_file = open('message.txt', 'r')
        message = message_file.read()
    except FileNotFoundError as err:
        print(err)

    return message

def main():
    emails = get_emails()
    message = get_message()
    forecast = weather.get_weather_forecast()

    mailer.send_emails(emails, message, forecast)

main()
