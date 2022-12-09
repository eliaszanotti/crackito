# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def f_accept_cookies(driver) :
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

def f_play_song(driver) :
    driver.find_element(By.CLASS_NAME, "futnNt").click()

def f_next_song(driver) :
    driver.find_element(By.CLASS_NAME, "mnipjT4SLDMgwiDCEnRC").click()

def f_repeat_button(driver) :
    driver.find_element(By.CLASS_NAME, "Vz6yjzttS0YlLcwrkoUR").click()
