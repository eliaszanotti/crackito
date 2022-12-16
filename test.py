 # selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.firefox.options import Options

#options.add_argument("binary")
#options.add_argument("/usr/bin/firefox-developer-edition")

#binary = FirefoxBinary('/usr/bin/firefox-developer-edition');
#options.setBinary('/usr/bin/firefox-developer-edition');
#print(fp)

#driver = webdriver.Chrome('/usr/bin/chromium')

options=Options()

options.set_preference("media.eme.enabled",True);
options.set_preference("media.gmp-manager.updateEnabled", True);
#fp = webdriver.FirefoxProfile()


driver = webdriver.Firefox(options=options)
driver.get('https://spotify.com')
cookie = {'name' : 'sp_dc', 'value' : 'AQB8HBUT67hKDPPwZrnOD_52CDquJssARaokfSrz0PIQBD9klwWvMHjpbaNChbfx4e3LuEadIfXLhAp-H74hYVFeXdmrpCwOgvRhICaTbsEQBNxq3dYPDY5Qi-tZvpWBD5wHZbBrfZQR9s3E-Ljql-YPAdZxhv-D'}

driver.add_cookie(cookie)
driver.get('https://spotify.com')

