import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread

url = "http://ec2-3-83-69-108.compute-1.amazonaws.com:8080/"

try:
    driver = webdriver.Chrome('./chromedriver')
except:
    driver = webdriver.Chrome()

driver.get(url)

time.sleep(2)

for i in range(12):
    btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-bar"]/form/button')))
    btn.click()
    time.sleep(0.2)


