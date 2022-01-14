import smtplib
import datetime as dt
import random
import pandas

mymail = ""
mymail2 = ""
pasd = ""

tdy = dt.datetime.now()
tdyt = (tdy.month, tdy.day)
dat = pandas.read_csv("birthdays.csv")
bdic = {(dr["month"], dr["day"]): dr for (i,dr) in dat.iterrows()}
if tdyt in bdic:
    bper = bdic[tdyt]
    fl = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(fl) as lf:
        con = lf.read()
        xy = con.replace("[NAME]", bper["name"])

    with smtplib.SMTP("smtp.gmail.com:587") as conct:
        conct.ehlo()
        conct.starttls()
        conct.login(user=mymail, password=pasd)
        conct.sendmail(from_addr=mymail,
                       to_addrs=bper["email"],
                       msg=f"Subject:Happy Birthday!!!\n\n{xy}")


# if wkd == 6:
#     with open("quotes.txt") as qu:
#         all = qu.readlines()
#         qt = random.choice(all)
#     print(qt)
