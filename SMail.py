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

    smtpserver = input(
        "[!] Chooise server Yandex[1] or Google[2]\n[*] Select 1 or 2 for chooise : ")

    if smtpserver == "2":
        print("[!] Warning, Google not supported 3'rd party software.")
        x = input(
            "[?] Would you like to continue anyway? [Y/y for yes, N/n for no]: ")

        if x == "N" or x == "n":
            print("Application exit.\nGoodbye :P")
            sys.exit(1)
        elif x == "Y" or x == "y":
            print(
                "---------------------------------------------------------------------------------\n[!] Continued")
        else:
            print("[!] Please enter Y,N, try again that program.")
            start()

    account = input("[*] Sender's mail address: ")
    password = input("[*] Sender's mail password: ")
    to = input("[*] Recipient's e-mail address: ")
    number = int(input("[*] How many e-mails will you send?: "))

    print("---------------------------------------------------------------------------------")

    if smtpserver == "1":
        server = smtplib.SMTP_SSL('smtp.yandex.com.tr', 465)
    elif smtpserver == "2":
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
    server.ehlo()

    # Starting in here.
    print("Starting...")
    while say <= number:
        subject = random.choice(konular)
        body = random.choice(konular)

        try:
            server.login(account, password)
        except Exception as err:
            print("Please check your mail system supported 3rd software settings. Please review: https://github.com/s4msecurity/SMail/issues/1")
            print(err)
            exit()

        mail = MIMEText(body, 'html', 'utf-8')
        mail['from'] = account
        mail['subject'] = subject
        mail['to'] = ','.join(to)
        mail = mail.as_string()
        try:
            server.sendmail(account, to, mail)
        except Exception as err:
            print(err)

        print("["+str(say)+"]"+"sending... ")
        say = say + 1


start()
