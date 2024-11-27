from selenium.webdriver.common.by import By

class BarboraItemPage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(By.CLASS_NAME, "b-product-info--title").text

    def get_price(self):
        return self.driver.find_element(By.XPATH, "//*[@id='fti-product-price--0']/meta[1]").get_attribute("content")




