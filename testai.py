import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import numpy as np



driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

driver.get("https://barbora.lt/produktai/gazuotas-gerimas-coca-cola-330-ml-83841")
driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

# print(driver.title)

# akcija = driver.find_element(By.CLASS_NAME, 'b-page-container b-info-page-container')

akcija = driver.find_element(By.CLASS_NAME, "b-page-specific-content").text
# akcija2 = akcija.split("\n")
# print(akcija2[0])
print(akcija.split("\n")[0])
driver.close()
# /html/body/div[2]/div/div[3]/div/div[3]
