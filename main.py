from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

def f_accept_cookies(driver) :
    time.sleep(1)
    cookie_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookie_button.click()

def f_play_song(driver) :
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "futnNt").click()

def main() :
    url = "https://open.spotify.com"
    driver = webdriver.Chrome("chromedriver")
    driver.get(url)
    cookie = {'name' : 'sp_dc', 'value' : 'AQDtiTt2-EjQDbHNrOh0NsLbZ_tSbmGPCqFc_5c2ORruTC1od0E9hMfmAEAJpX-w7o0aac4Hk-DDUIgFik7E3dujW10RkQtHJmG8hwOm_9OqZbPPMchjHWULbl8oAMVf9H-lWEgdVJLQ5I40n8MLM3Zc6mt9LOlz'}
    driver.add_cookie(cookie)
    f_accept_cookies(driver)
    driver.get("{}/playlist/0WXMfN8PQKk9cFzkyhCUG2".format(url))
    f_play_song(driver)
    time.sleep(1000)

if __name__ == "__main__":
   main()
