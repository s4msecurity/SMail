import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import random


konular = [
	"message1",
	"message2",
	"meesage3",
	"Input message list"
]

print("-------------------------------------------------------------------------------------")
print()

print("""

 )  ____) |        |    /  \    (_    _) \   |    
(  (___   |  |\/|  |   /    \     |  |    |  |    
 \___  \  |  |  |  |  /  ()  \    |  |    |  |    
 ____)  ) |  |  |  | |   __   |  _|  |_   |  |__  
(      (__|  |__|  |_|  (__)  |_(      )_/      )_

""")
print("SMail spam bot version 1.0\nAny illegal use belongs to the user.")
print()

say = 1
sy = 1
def start():
    global say

    account = input("["+str(sy)+"]"+"Sender's gmail address: ")
    password = input("["+str(sy)+"]"+"Sender's mail password: ")
    print()
    to = input("Recipient's e-mail address: ")
    print("---------------------------------------------------------------------------------")
    number = int(input("How many e-mails will you send?: "))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    #Başlama kısmı burası.

    print("Starting...")
    print()



    while say <= number:
        subject = random.choice(konular)
        body = random.choice(konular)
        server.login(account, password)

        mail = MIMEText(body, 'html', 'utf-8')
        mail['from'] = account
        mail['subject'] = subject
        mail['to'] = ','.join(to)
        mail = mail.as_string()
        server.sendmail(account, to, mail)

        print("["+str(say)+"]"+"sending... ")
        say = say + 1

start()