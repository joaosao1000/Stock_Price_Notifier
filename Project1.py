from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import yagmail
import os

sender = 'joaosao1000@gmail.com'
password = os.getenv('senha')
receiver = 'joasao1001@gmail.com'

subject = 'ALERT'

contet = """

PERCENTAGE IS LOWER THAN -0.10%

"""


def get_driver():
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    option.add_argument('start-maximized')
    option.add_argument('disable-dev-shm-usage')  # linux
    option.add_argument('no-sandbox')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument('disable-blink-features = AutomationControlled')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get('https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6')
    return driver


def clean(text):
    output = (text.split('+',))
    out2 = output[1].split(' %')
    return out2[0]


def main():
    driver = get_driver()
    while True:
        time.sleep(10)
        element = driver.find_element(by='xpath', value='/html/body/div[2]/div/section[1]/div/div/div[2]/span[2]')
        if float(clean(element.text)) < -0.10:
            yag = yagmail.SMTP(user=sender, password=password)
            yag.send(to=receiver, subject=subject, contents=contet)
            print('email sent')


print(main())
