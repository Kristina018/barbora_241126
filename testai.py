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

driver.get("https://barbora.lt/produktai/grikiai-well-done-800-g")
driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()


# pieno kainos eurai - nepavyksta tik atspausdint:
# eurai2 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[4]/div[1]/div/div[1]/div[1]/div[1]/span[1]'))).text
# eurai = driver.find_element(By.XPATH,
#                          '/html/body/div[3]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[4]/div[1]/div/div[1]/div[1]/div[1]/span[1]').text
#
# centai = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[4]/div[1]/div/div[1]/div[1]/div[1]/span[3]").text
# kaina = float(int(eurai) + int(centai)/100)
# print(kaina)
eu = driver.find_element(By.ID, "b-product-info--price-placeholder").get_attribute("price").text

# eu = driver.find_element(By.CLASS_NAME, "fti-product-price--0").text
# ct = driver.find_element(By.CLASS_NAME, "")
print(eu)
# title eilute
print(driver.title)


# centai2 = int(centai)/100



# print(f"Kaina: {eurai}{taskas}{centai}")

# # bandau kaina - printina stulpeliu
# a = driver.find_element(By.ID, "fti-product-price--0").text
# print(a)

# # VEIKIA PUSIAU
# elements = driver.find_elements(By.CLASS_NAME, "b-product-info--price-and-quantity")
# texts = [element.text for element in elements]
# print(texts, sep="\n")
# print(texts, sep="\n\n ") # spaudina paskutini dalyka (kartais)

# # VEIKIA PUSIAU
# a = driver.find_element(By.CLASS_NAME, "tw-pb-1").text
# # print(a[0])
# print(a)
# # print(type(a))
# # type(a)
###
# driver.find_element(By.CLASS_NAME, "md:tw-leading-6").text

# driver.close()