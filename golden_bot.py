#!/usr/bin/env python

import os
import sys
import json
import time
import smtplib
import timeout_decorator
from selenium import webdriver


class StackOverflowBot:
    """
    Bot to sign in to Stack Overflow, visit the personal profile and send mail with a day count report.
    """

    def __init__(self):
        self.driver = None
        self.email_content = "Subject: Your favourite Stack Overflow bot [ERROR]\n\nNo data. The driver hasn't been run yet!"
    
    @timeout_decorator.timeout(10)
    def start_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(desired_capabilities=options.to_capabilities())
        self.driver.implicitly_wait(9)

    @timeout_decorator.timeout(15)
    def visit_profile(self, login, password):
        self.driver.get('https://stackoverflow.com/users/login')
        self.driver.find_element_by_id('email').send_keys(login)
        self.driver.find_element_by_id('password').send_keys(password)
        element = self.driver.find_element_by_id('submit-button')
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element_by_class_name('my-profile').click()
        self.driver.find_element_by_xpath("//div[@id='tabs']/a[1]").click()
        day_count = self.driver.find_element_by_xpath("//div[@id='days-visited']/div[2]").text.split()[3] + '/100'
        self.email_content = "Subject: Your favourite Stack Overflow bot\n\nYour current day count: " + day_count

    def send_mail(self, gmail, password, receiver):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail, password)
        server.sendmail(
            gmail,
            receiver,
            self.email_content)
        server.quit()

    def close_driver(self):
        self.driver.close()


if __name__ == "__main__":

    with open(os.path.join(sys.path[0], 'config.json')) as f:
        creds = json.load(f)

    try:
        golden_bot = StackOverflowBot()
        golden_bot.start_driver()
        golden_bot.visit_profile(login=creds['so_login'], password=creds['so_password'])
    except Exception as e:
        golden_bot.email_content = "Subject: Your favourite Stack Overflow bot [ERROR]\n\nSomething went wrong: {}".format(e)
    finally:
        golden_bot.send_mail(gmail=creds['gmail'], password=creds['gmail_password'], receiver=creds['receiver'])
        golden_bot.close_driver() if golden_bot.driver else None

