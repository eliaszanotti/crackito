from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome("chromedriver")
driver.get("https://open.spotify.com/")

test = driver.find_element(By.CLASS_NAME, "IPVjkkhh06nan7aZK7Bx")
test.click()



time.sleep(1000)






