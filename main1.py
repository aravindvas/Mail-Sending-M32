import smtplib
import datetime as dt
import random

mymail = ""
mymail2 = ""

pasd = ""

nw = dt.datetime.now()
wkd = nw.weekday()

with open("quotes.txt") as qu:
    all = qu.readlines()
    qt = random.choice(all)
print(qt)
with smtplib.SMTP("smtp.gmail.com:535") as conct:
    conct.ehlo()
    conct.starttls()
    conct.login(user=mymail, password=pasd)
    if wkd == 6:
        conct.sendmail(from_addr=mymail,
                       to_addrs=mymail2,
                       msg=f"Subject:Sunday Motivation!\n\n{qt}")
    elif wkd == 5:
        conct.sendmail(from_addr=mymail,
                       to_addrs=mymail2,
                       msg=f"Subject:Saturday Motivation!\n\n{qt}")
    elif wkd == 4:
        conct.sendmail(from_addr=mymail,
                       to_addrs=mymail2,
                       msg=f"Subject:Friday Motivation!\n\n{qt}")
    elif wkd == 3:
        conct.sendmail(from_addr=mymail,
                       to_addrs=mymail2,
                       msg=f"Subject:Thursday Motivation!\n\n{qt}")
    elif wkd == 2:
        conct.sendmail(from_addr=mymail,
                       to_addrs=mymail2,
                       msg=f"Subject:Wednesday Motivation!\n\n{qt}")
    elif wkd == 1:
        conct.sendmail(from_addr=mymail,
                       to_addrs=mymail2,
                       msg=f"Subject:Tuesday Motivation!\n\n{qt}")
    elif wkd == 0:
        conct.sendmail(from_addr=mymail,
                       to_addrs=mymail2,
                       msg=f"Subject:Monday Motivation!\n\n{qt}")






