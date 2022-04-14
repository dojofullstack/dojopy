import funciones


data_emails = open('./lista_correos.txt')
data_emails = data_emails.readlines()
print(data_emails)

for email in data_emails:
    email = email.strip('\n')
    funciones.modulo_email_notif(
        receiver=email,
        body_message=f'HOLA ES UNA PRUEBA BODY {email}',
        sender='stefany@dojopy.com',
        subject='HOLA ES UNA PRUEBA2'
    )