# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# files
from color import *
import time

def f_accept_cookies(driver) :
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()
    print(colors.BLUE + "[Cookies accepted]" + colors.RESET)

def f_play_song(driver) :
    driver.find_element(By.CLASS_NAME, "futnNt").click()
    print(colors.BLUE + "[Play song]" + colors.RESET)

def f_next_song(driver) :
    driver.find_element(By.CLASS_NAME, "mnipjT4SLDMgwiDCEnRC").click()

def f_repeat_button(driver) :
    driver.find_element(By.CLASS_NAME, "Vz6yjzttS0YlLcwrkoUR").click()
    print(colors.BLUE + "[Repeat button]" + colors.RESET)
