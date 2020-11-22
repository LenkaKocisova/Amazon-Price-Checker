import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.co.uk/Sony-ILCE7KB-CE-Autofocus-Tiltable-Tru-Finder/dp/B00FWUDEEC/ref=sr_1_1?dchild=1&keywords=sony+a7&qid=1605098391&quartzVehicle=5-109&replacementKeywords=sony&sr=8-1"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "lxml")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5])

    if(converted_price > 700):
        send_mail()


    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("kocisova.lenka25@gmail.com", "fiugnqpxxaijyoof")
    subject = "Price fell down!"
    body = "Check the Amazon link https://www.amazon.co.uk/Sony-ILCE7KB-CE-Autofocus-Tiltable-Tru-Finder/dp/B00FWUDEEC/ref=sr_1_1?dchild=1&keywords=sony+a7&qid=1605098391&quartzVehicle=5-109&replacementKeywords=sony&sr=8-1"
    
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "kocisova.lenka25@gmail.com",
        "25lenka25@gmail.com",
        msg
    )
    print("Hey, email has been sent!")

    server.quit()

check_price()






