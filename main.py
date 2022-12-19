# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

# files
from utils import *
from color import *
import csv
import time 
import random
  
def f_launch_driver(url, driver_exe) : 
    options=Options()
    options.set_preference("media.eme.enabled",True);
    options.set_preference("media.gmp-manager.updateEnabled", True);
    driver = webdriver.Firefox(options=options)
    #driver = webdriver.Chrome(driver_exe)
    driver.maximize_window()
    driver.get(url)
    print(colors.BLUE + "[Home page reached]" + colors.RESET)
    return driver

def f_get_cookie(csv_file) :
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            return row['VALUE'][0]

def main() :
    url = "https://open.spotify.com"
    driver = f_launch_driver(url, "chromedriver")
    driver.implicitly_wait(10)
    #cookie = {'name' : 'sp_dc', 'value' : f_get_cookie('cookies.csv')}
    cookie = {'name' : 'sp_dc', 'value' : 'AQB8HBUT67hKDPPwZrnOD_52CDquJssARaokfSrz0PIQBD9klwWvMHjpbaNChbfx4e3LuEadIfXLhAp-H74hYVFeXdmrpCwOgvRhICaTbsEQBNxq3dYPDY5Qi-tZvpWBD5wHZbBrfZQR9s3E-Ljql-YPAdZxhv-D'}
    f_accept_cookies(driver)
    driver.add_cookie(cookie)
    driver.get("{}/playlist/0WXMfN8PQKk9cFzkyhCUG2".format(url))
    print(colors.BLUE + "[Playlist page reached]" + colors.RESET)
    f_play_song(driver)
    f_repeat_button(driver)
    i = 1
    while (i < 500) :
        time.sleep(random.randint(31, 60))
        f_next_song(driver)
        print(colors.GREEN + "[Stream]", i, colors.RESET) 
        i += 1

main()

#jtRqaoDIpIR6fEATUTyY  class of advertising
