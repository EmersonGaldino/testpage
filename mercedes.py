import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


url = "https://mercedesclubqa.azurewebsites.net/#/"

option = Options()
option.headless = True
#option.binary = 'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox()
driver.get(url)
time.sleep(2)


login = driver.find_element_by_id("userName")
login.send_keys('287.616.890-17')
time.sleep(2)
password = driver.find_element_by_id("userPwd")
password.send_keys('Yan@123456')


time.sleep(5)
driver.find_element_by_css_selector(".bt-blue").click()


time.sleep(5)
driver.find_element_by_css_selector(".bt-blue").click()
time.sleep(1)
driver.find_element_by_css_selector(".btn-primary").click()


# time.sleep(10)
# Selecionar aceite termo
# driver.find_element_by_id("#aceiteRegulamento").click()
# time.sleep(6)
# fechar modal termo
# driver.find_element_by_css_selector(".mfp-close").click()

# time.sleep(2)
# abrir menu

driver.find_element_by_css_selector(".sidebar-title").click()

# time.sleep(2)
# Juntos na estrada
# driver.find_element_by_css_selector(".fa-chevron-down").click()
# time.sleep(2)
# Como funciona

driver.find_element_by_css_selector(".ng-scope").click()

# time.sleep(2)
# driver.find_element_by_id("#perido").scrollp
# time.sleep(4)
# driver.find_element_by_id("#comoParticipar").scrollIntoView()
# time.sleep(4)
# driver.find_element_by_id("#premiacao").scrollIntoView()
# time.sleep(4)
# Ranking
# driver.find_element_by_css_selector(".fa-chart-line").click()
# time.sleep(2)
# Regulamento
# driver.find_element_by_css_selector(".fa-file-alt").click()
# time.sleep(2)
# Ranking Concessionarios
# driver.find_element_by_css_selector(".fa-cogs").click()

# deslogar
# time.sleep(5)
# driver.find_element_by_css_selector(".fw600").click()  # Menu usuario
# time.sleep(2)
# driver.find_element_by_css_selector(".fa-power-off").click()  # LogOut


# time.sleep(5)
# driver.quit()  # Fechar aba firefox
