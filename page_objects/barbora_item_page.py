from selenium.webdriver.common.by import By
import re

class BarboraItemPage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def get_title(self):
        title = self.driver.find_element(By.CLASS_NAME, "b-product-info--title").text
        # title_split = re.split(', ', title)
        # return title_split[0]
        # x = title.rsplit(", ", -2)
        return title

    def get_price(self):
        return self.driver.find_element(By.XPATH, "//*[@id='fti-product-price--0']/meta[1]").get_attribute("content")

    def get_unit(self):
        # units = self.driver.find_element(By.XPATH, "//*[@id='fti-product-price--0']/div[1]/div[1]").text
        # unit_split = re.split(' ', units)
        # return unit_split[-1]
        #
        # ne visada gerai:
        # unit = self.driver.find_element(By.CLASS_NAME, "b-product-info--title").text
        # unit_split = re.split(' ', unit)
        # return unit_split[-1]

        # veikia gerai:
        title = self.driver.find_element(By.CLASS_NAME, "b-product-info--title").text
        unit_split = re.split(' ', title)
        a = len(unit_split)-1
        return unit_split[a]

    def get_size(self):
        title = self.driver.find_element(By.CLASS_NAME, "b-product-info--title").text
        size = title.split(" ")
        a = len(size)-2
        return size[a]

    def get_discount(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[3]/div/div[1]/div/div/div/div[2]/div/span").text





