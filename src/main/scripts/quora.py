from selenium import webdriver
import os
import requests
import time

browser = webdriver.Firefox(executable_path=r'/home/ash/.local/bin/geckodriver')
browser.get('https://www.quora.com/login')
browser.maximize_window()

browser.find_elements_by_name("email")[1].clear()
browser.find_elements_by_name("email")[1].send_keys('abhay.chauhanmonu@gmail.com')
browser.find_elements_by_name("password")[1].clear()
browser.find_elements_by_name("password")[1].send_keys('abhay@9654')

time.sleep(2)
browser.find_element_by_css_selector("input[type='submit'][value='Login']").click()
time.sleep(2)

with open('input.txt') as f:
    usernames = f.readlines()
    username = [x.strip() for x in usernames]

for i in range(0,len(username)):
    browser.get(str(username[i]))
    image = browser.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/span/img')
    url = image.get_attribute('src')
    name = "img"+str(i)+".jpg"
    with open(name, "wb") as f:
        f.write(requests.get(url).content)

browser.close()
