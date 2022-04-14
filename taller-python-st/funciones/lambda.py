import json
import smtplib
from email.mime.text import MIMEText


def modulo_email_notif(receiver, subject, body_message, sender='lifehack.py@gmail.com'):
    try:
        port = 587
        msg = MIMEText(body_message)

        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver

        with smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', port) as server:
            server.starttls() # Secure the connection
            server.login('AKIAQ5S7I3EPAI5YMIVH', 'BLBynm7e6HgNhKUcndu2D8elDZsKZ7tkDPu26ng+f0Eb')
            server.sendmail(sender, receiver, msg.as_string())
            print("Successfully sent email")
    except Exception as e:
        print(e)


def lambda_handler(event, context):
    email = event.get('email')
    name = event.get('name')

    body_message = f'Hola Nuevo Lead!, Email: {email} Nombre: {name}'
    modulo_email_notif('hola@dojopy.com', 'LEAD BOOTCAMP FULLSTACK', body_message)
    return {
        'statusCode': 200,
        'body': json.dumps('ok')
    }


# lambda_handler({'email': 'user@gmail.com', 'name': 'henry'}, '')