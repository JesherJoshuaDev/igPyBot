#!/usr/bin/env python3
from selenium import webdriver as wd
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from time import sleep



browser=wd.Chrome('/Users/jesherjoshua/Library/chromedriver')
wait=WebDriverWait(browser,10)
usr_name=str(input('enter acc username'))
password=str(input('enter acc password'))


#sleep(5)
def login(u,p):
    
    browser.get('https://www.instagram.com/')
    sleep(3)
    #username and password objects
    username_element=browser.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
    password_element=browser.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
    login_button=browser.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
    
    #sending uname and password
    username_element.send_keys(u)
    password_element.send_keys(p)
    login_button.click()
    sleep(3)
    try:
        opt_button=browser.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
        opt_button.click()
        sleep(2)
    except:
        pass
    try:
        not_now_button=browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
        not_now_button.click()
        sleep(2)
    except:
        pass 

def search(s):
    search_bar_element=browser.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
    search_bar_element.send_keys(s)
    sleep(1)
    search_bar_element.send_keys(Keys.ENTER)
    search_bar_element.send_keys(Keys.ENTER)
    sleep(2)
    name_on_page = browser.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > h2')
    return name_on_page.text
    

def follow(sname,fname):
    if sname!=fname:
        raise Exception('The given username and resultant username do not match')
    else:
        try:
            follow_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Follow')]")))       
            sleep(2)
            follow_button.click()
        except:
            print('you already follow this person (or) something went wrong:(')


