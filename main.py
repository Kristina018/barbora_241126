from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from models.barbora_item import BarboraItem
from scrapers.barbora_scraper import BarboraScraper
from selenium.webdriver.support import expected_conditions as EC



def init_gathering():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    return driver, wait


def execute_data_gathering():
    driver, wait = init_gathering()
    # barbora = BarboraScraper(driver, wait, 'https://barbora.lt/duonos-gaminiai-ir-konditerija/konditerijos-gaminiai/tortai')
    barbora = BarboraScraper(driver, wait,'https://barbora.lt/bakaleja/kruopos/grikiai')
    barbora.collect_data()

execute_data_gathering()