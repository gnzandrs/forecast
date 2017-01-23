import smtplib

def send_emails(emails, message, forecast):
    # Connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    try:
        from_email = input("What's your email?\n")
        password = input("What's your password?\n")
        server.login(from_email, password)
    except smtplib.SMTPAuthenticationError as err:
        print('Wrong Authentication!')
        exit()

    # Send to entire email list
    for to_email, name in emails.items():
        text = 'Subject: Remember our meeting!\n'
        text += 'Hi ' + name + '!\n\n'
        text += message + '\n\n'
        text += forecast + '\n\n'
        text += 'See you there!'
        server.sendmail(from_email, to_email, text)

    print('The email message was successfully sent to: \n')
    for to_email, name in emails.items():
        print(to_email + '\n\n')
    server.quit()
