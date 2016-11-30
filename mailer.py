import smtplib

def send_emails(emails, message, forecast):
    # Connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    # password = input("What's your password?")
    password = 'yourpassword'
    from_email = 'youremail'
    server.login(from_email, password)

    # Send to entire email list
    for to_email, name in emails.items():
        text = 'Subject: Remember our meeting!\n'
        text += 'Hi ' + name + '!\n\n'
        text += message + '\n\n'
        text += forecast + '\n\n'
        text += 'See you there!'
        server.sendmail(from_email, to_email, text)

    server.quit()
