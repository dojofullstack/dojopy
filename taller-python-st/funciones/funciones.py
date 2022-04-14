import smtplib
from email.mime.text import MIMEText



def modulo_email_notif(receiver, subject, body_message, sender='hola@dojopy.com'):
    # sender = 'hola@dojopy.com'
    # receiver = [receiver]

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




# modulo_email_notif(
#     receiver='tepiflorez@gmail.com',
#     body_message='HOLA ES UNA PRUEBA BODY',
#     sender='stefany@dojopy.com',
#     subject='HOLA ES UNA PRUEBA'
#     )


def usuarios_(*args):
    print(args)
    for arg in args:
        print(arg)

def usuarios(**args):
    print(args)
    for arg in args:
        print(arg)

# usuarios(user1='stefany', user2='erick')
# usuarios_('stefany', 'erick')


user_notificado = lambda user, gender: (user.upper(), gender.upper())

print(user_notificado('stefany', 'f'))



