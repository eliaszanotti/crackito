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
    driver.get(url)
    print(colors.BLUE + "[Home page reached]" + colors.RESET)
    return driver

def f_get_nb_driver(csv_file) :
    with open(csv_file, newline='') as csvfile :
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader :
            i += 1
        return (i)

def f_get_cookie(csv_file, nb) :
    with open(csv_file, newline='') as csvfile :
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader :
            if (i == nb) :
                return(row['VALUE'])
            i += 1

def main() :
    url = "https://open.spotify.com"
    driver = f_launch_driver(url, "chromedriver")
    driver.implicitly_wait(10)
    cookie = {'name' : 'sp_dc', 'value' : f_get_cookie('cookies.csv', 2)}
    f_accept_cookies(driver)
    driver.add_cookie(cookie)
    driver.get("{}/playlist/0WXMfN8PQKk9cFzkyhCUG2".format(url))
    print(colors.BLUE + "[Playlist page reached]" + colors.RESET)
    f_play_song(driver)
    f_repeat_button(driver)
    i = 1
    while (i < 500) :
        random_skip = random.randint(31, 60)
        time.sleep(random_skip)
        f_next_song(driver)
        print(colors.GREEN + "[Stream after"\
		    , random_skip, "s]", i, colors.RESET) 
        i += 1

print(f_get_nb_driver('cookies.csv'))
print(f_get_cookie('cookies.csv', 0))
print(f_get_cookie('cookies.csv', 1))
print(f_get_cookie('cookies.csv', 2))


main()

#jtRqaoDIpIR6fEATUTyY  class of advertising
#touchable class of dismiss button for premium account 
