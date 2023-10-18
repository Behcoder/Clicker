from selenium import webdriver
import time
from urls import urlMaker1
from urls import urlMaker2
from random import randint

while True:
    
    driver = webdriver.Firefox()
    driver.maximize_window()

    for i in range(10):
        url1 = urlMaker1()
        print(url1)
        driver.get(url1)
        waitTime = randint(4, 14)
        print(f"waitTime1 is {waitTime} seconds")
        time.sleep(waitTime)

        url2 = urlMaker2()
        print(url2)
        driver.get(url2)
        waitTime = randint(4, 14)
        print(f"waitTime2 is {waitTime} seconds")
        time.sleep(waitTime)

    time.sleep(10)
    driver.close()
