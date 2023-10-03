import smtplib
import ssl

my_email = "attahirukamba44@gmail.com"
password = "pdstswqxccgvroqg"
smtp_server = "smtp.gmail.com"
receiver_mail = "muhammadkamba21@gmail.com"

def send_mail(message, smtp_server=smtp_server, sender_mail=my_email, receiver_mail=receiver_mail, password=password):

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host=smtp_server, port=465, context=context) as connection:
        print("Sending a secured email.")
        connection.login(user=sender_mail, password=password)
        connection.sendmail(from_addr=sender_mail, to_addrs=receiver_mail,
                                msg=message)
        print("Sent mail.")
