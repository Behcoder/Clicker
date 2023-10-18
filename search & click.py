# This program search a keyword on google and click on result you specified.
# The keyword in this example is "لوله گالوانیزه سبک 1 اینچ"
# between any part of program is a random pause

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from selenium.webdriver.firefox.options import Options

keyWord = "لوله گالوانیزه سبک 1 اینچ"
# runTimes = int(input("Enter no. of exec. prog: "))
runTimes = 1
def waiter(a, b):
    WaitTime = randint(a, b)
    # count += 1
    print(f"waitTime is {WaitTime} seconds")
    time.sleep(WaitTime)

def moreResultClicker():
    for i in range (3):
        moreResult = driver.find_element(By.XPATH,
                                         "//div[5]/div/div[10]/div/div[4]/div/div[3]/div[4]/a[1]/h3/div/span[2]")
        moreResult.click()
        waiter(2, 5)
        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)
        waiter(1, 2)


firefox_options = Options()
firefox_options.set_preference("browser.privatebrowsing.autostart", True)
driver = webdriver.Firefox(options=firefox_options)

for i in range (runTimes):
    while True:

        driver.get('https://www.google.com')
        waiter(5, 9)

        search_input = driver.find_element("name", 'q')
        search_input.send_keys(keyWord)
        waiter(2, 4)

        search_input.send_keys(Keys.ENTER)
        waiter(4, 7)

        html = driver.find_element(By.TAG_NAME, 'html')

        for i in range(10):
            html.send_keys(Keys.END)
            waiter(2, 3)
        waiter(4, 5)

        print("trying to click on more result")

        moreResultClicker()

        myUrls = driver.find_element(By.XPATH, '//div[@class="yuRUbf"]//a[starts-with(@href,"https://www.seify.ir")]')
        myUrls.click()
        waiter(4, 7)

        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)
        waiter(45, 77)


        driver.close()
        waiter(3, 5)

