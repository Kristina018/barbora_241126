from selenium.webdriver.common.by import By
import re

class BarboraItemPage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        title = self.driver.find_element(By.CLASS_NAME, "b-product-info--title").text
        title_split = re.split(', ', title)
        return title_split[0]

    def get_price(self):
        return self.driver.find_element(By.XPATH, "//*[@id='fti-product-price--0']/meta[1]").get_attribute("content")

    def get_unit(self):
        units = self.driver.find_element(By.XPATH, "//*[@id='fti-product-price--0']/div[1]/div[2]").text
        units_split = re.split('/', units)
        return units_split[-1]

    def get_size(self):
        title = self.driver.find_element(By.CLASS_NAME, "b-product-info--title").text
        size = title.split(" ")
        a = len(size)-2
        return size[a]

    # element_text = driver.find_element_by_tag_name('h3').text
    # # split element_text into ['Confirmation', '#:', 'S1234567890']
    # split_text = element_text.split(' ')
    # confirmation_num = split_text[2]





