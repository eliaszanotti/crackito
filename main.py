# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# files
from utils import *
import csv
import time 
import random
  
def f_launch_driver(url, driver_exe) : 
    driver = webdriver.Chrome(driver_exe)
    driver.maximize_window()
    driver.get(url)
    return driver

def f_get_cookie(csv_file) :
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            return row['VALUE']

def main() :
    url = "https://open.spotify.com"
    driver = f_launch_driver(url, "chromedriver")
    driver.implicitly_wait(10)
    cookie = {'name' : 'sp_dc', 'value' : f_get_cookie('cookies.csv')}

    f_accept_cookies(driver)
    driver.add_cookie(cookie)
    driver.get("{}/playlist/0WXMfN8PQKk9cFzkyhCUG2".format(url))
    f_play_song(driver)
    f_repeat_button(driver)
    i = 1
    while (i < 500) :
        time.sleep(random.randint(31, 60))
        f_next_song(driver)
        print("OK :", i) 
        i += 1

    time.sleep(1000)

main()



#jtRqaoDIpIR6fEATUTyY
#jtRqaoDIpIR6fEATUTyY  class of advertising
