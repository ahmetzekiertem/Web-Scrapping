
https://myaccount.google.com/lesssecureapps

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "ahmetzekiertem@gmail.com"

mesaj["To"] = "ahmetzekiertem@gmail.com"

mesaj["To"] = "safakiy28@gmail.com"
mesaj["Subject"] = "Smtp Mail Gönderme"


yazi = """

Smtp ile mail gönderiyorum.

Selamun Aleyk]m 

Iyi Askerlikler reis


"""


mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("ahmetzekiertem@gmail.com","A") # SMTP server'ına giriş yapıyoruz. Kendi mail adresimizi ve parolamızı yapıyoruz.

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail Başarıyla Gönderildi....")

    mail.close()  # Smtp serverımızın bağlantısını koparıyoz.



except:
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()







