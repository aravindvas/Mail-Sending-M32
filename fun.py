import smtplib


mymail = "mailme.anonymous.1@gmail.com"
mymail2 = "veeragandhamrajeevvas@gmail.com"
pasd = "mailme1997"


for i in range(1):
    with smtplib.SMTP("smtp.gmail.com:587") as conct:
        conct.ehlo()
        conct.starttls()
        conct.login(user=mymail, password=pasd)
        conct.sendmail(from_addr=mymail,
                       to_addrs=mymail2,
                       msg="Subject:Subscribed Successfully!\n\n Thank you for your subscription")






