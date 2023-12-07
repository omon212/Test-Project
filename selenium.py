import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




def done():

    print("Followed all the users")
    time.sleep(2)
    browser.quit()

def follow(userlist):
        for user in userlist:
            for i in range(30000):
                url = "https://www.instagram.com/" + 'rmkvlly'
                browser.get(url)
                follow_btn = browser.find_element_by_xpath('_ah57t')
                follow_btn.click()
                print("Followed " + user)
                time.sleep(2)
            done()