# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import
import time

def f_accept_cookies(driver) :
    time.sleep(1)
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

def f_play_song(driver) :
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "futnNt").click()
