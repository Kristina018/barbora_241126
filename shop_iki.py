import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 100)
driver.get("https://iki.lt")

# atemsti slapukus
time.sleep(10)
driver.find_element(By.ID, "onetrust-reject-all-handler").click()

# isjungti reklama
time.sleep(5)
driver.find_element(By.ID, "js_modal_frontpage_close").click()
# driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()

# nueiti i eshopa
driver.find_element()

# driver.find_element(By.CLASS_NAME, "tw-pr-[2px]").text

# pieno kainos eurai - nepavyksta tik atspausdint:
# a = driver.find_elements(By.XPATH,
#                          '/html/body/div[3]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[4]/div[1]/div/div[1]/div[1]/div[1]/span[1]')
# print(a[0])
# print(type(a))
# type(a) # nespausdina
#
# # title eilute
# print(driver.title)
# # print(a)

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