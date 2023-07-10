from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText

response = requests.get(f"https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
                        headers={
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                            "Accept-Language": "en-US,en;q=0.9,fr;q=0.8"})
# got the header params from here "https://myhttpheader.com/"
data = response.text


soup = BeautifulSoup(data, "html.parser")

price = soup.find(class_="a-offscreen").getText()
exactPrice = float(price.split('$')[1])
title = soup.find(class_="product-title-word-break").getText()

BUY_PRICE = 200

sender = "nba4everwanted@gmail.com"
password = "YOUR GMAIL APP PASSWORD"
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
recipients = ["nba4everwanted@gmail.com", "alex.nollabell@gmail.com"]
subject = "Amazon Price Alert"
message = f"{title} is now {exactPrice}"

def send_mail(sender, password, url, recipients, subject, message):
    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp_server:
        smtp_server.starttls()
        result = smtp_server.login(sender, password)
        smtp_server.sendmail(
            from_addr=sender,
            to_addrs=recipients,
            msg=f"Subject: {subject} \n\n{message}\n{url}\n\n #thankU4Ex16 ".encode("utf-8")
        )
        print("Message sent")


if exactPrice < BUY_PRICE:
    send_mail(sender, password, url, recipients, subject, message)
    # message = f"{title} is now {exactPrice}"
