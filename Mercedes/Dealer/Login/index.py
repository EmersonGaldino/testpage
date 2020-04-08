import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from os.path import dirname, realpath, isfile
import json

with open('login.json') as file:
    data = json.load(file)

result = data
print(result)
option = Options()
option.headless = True
driver = webdriver.Firefox()
driver.get(result['base_url'])
_user = result['user']
pass_ = result['password']

login = driver.find_element_by_id(_user)
login.send_keys(pass_)
time.sleep(2)
password = driver.find_element_by_id("senha")
password.send_keys('123456')


time.sleep(1)
# driver.find_element_by_css_selector(".btn-primary").click()

time.sleep(10)
# Selecionar aceite termo
# driver.find_element_by_id("#aceiteRegulamento").click()
# time.sleep(6)
# fechar modal termo
driver.find_element_by_css_selector(".mfp-close").click()

time.sleep(2)
# abrir menu
driver.find_element_by_css_selector(".sidebar-title").click()
time.sleep(2)
# Juntos na estrada
driver.find_element_by_css_selector(".fa-chevron-down").click()
time.sleep(2)
# Como funciona
driver.find_element_by_css_selector(".fa-question-circle").click()
# time.sleep(2)
# driver.find_element_by_id("#perido").scrollIntoView()
# time.sleep(4)
# driver.find_element_by_id("#comoParticipar").scrollIntoView()
# time.sleep(4)
# driver.find_element_by_id("#premiacao").scrollIntoView()
time.sleep(4)
# Ranking
driver.find_element_by_css_selector(".fa-chart-line").click()
time.sleep(2)
# Regulamento
driver.find_element_by_css_selector(".fa-file-alt").click()
time.sleep(2)
# Ranking Concessionarios
# driver.find_element_by_css_selector(".fa-cogs").click()

# deslogar
time.sleep(5)
driver.find_element_by_css_selector(".fw600").click()  # Menu usuario
time.sleep(2)
driver.find_element_by_css_selector(".fa-power-off").click()  # LogOut


time.sleep(5)
driver.quit()  # Fechar aba firefox
