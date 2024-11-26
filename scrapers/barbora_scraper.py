from driver import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from models.barbora_item import BarboraItem
import time
from selenium.webdriver.support import expected_conditions as EC


class BarboraScraper:
    def __init__(self, driver, wait, url):
        self.hrefs = []
        self.driver = driver
        self.url = url
        self.wait = wait

    def accept_cookies(self):
        self.driver.get("https://www.barbora.lt")
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll'))).click()
        #self.driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
        time.sleep(10)

    def collect_data(self):
        self.accept_cookies()
        #time.sleep(5)

        # bakaleja
        # self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div[1]/div/div/ul/li[5]/div/a').click()
        # time.sleep(5)

        # grikiai
        # self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[3]/div[2]/div/div/div/div[1]/div[2]/ul/li[3]/div/a').click()

        self.age_consent()
        self.get_urls()
        self.collect_each()

    def get_urls(self):
        hrefs = []
        for i in range(1, 20):
            self.driver.get(f"{self.url}?page={i}")
            ul = self.driver.find_element(By.XPATH, '//*[@id="category-page-results-placeholder"]/div/ul')
            lis = ul.find_elements(By.TAG_NAME, 'li')
            # print(f"Tiek pas mus grikiu {i}-ame puslapyje: {len(lis)}:")
            if len(lis) == 0:
                break
            for a in lis:
                href = a.find_element(By.TAG_NAME, 'a').get_attribute('href')
                self.hrefs.append(href)
                # print(href)

    def collect_each(self):
        for link in self.hrefs:
            self.driver.get(link)
            item = BarboraItem(self.driver)
            item.fill()
            # item.save()

    def age_consent(self):
        self.driver.get(self.url)
        is_20 = len(self.driver.find_elements(By.ID, 'fti-modal-option-1')) != 0
        if is_20:
            self.driver.find_element(By.ID, "fti-modal-option-1").click()

    def get(self, param):
        pass