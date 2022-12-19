 # selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

options=Options()
options.set_preference("media.eme.enabled",True);
options.set_preference("media.gmp-manager.updateEnabled", True);
driver = webdriver.Firefox(options=options)

driver.get('https://spotify.com')
cookie = {'name' : 'sp_dc', 'value' : 'AQB8HBUT67hKDPPwZrnOD_52CDquJssARaokfSrz0PIQBD9klwWvMHjpbaNChbfx4e3LuEadIfXLhAp-H74hYVFeXdmrpCwOgvRhICaTbsEQBNxq3dYPDY5Qi-tZvpWBD5wHZbBrfZQR9s3E-Ljql-YPAdZxhv-D'}

driver.add_cookie(cookie)

url = "https://open.spotify.com"

driver.get("{}/playlist/0WXMfN8PQKk9cFzkyhCUG2".format(url))
