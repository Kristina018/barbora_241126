from selenium.webdriver.common.by import By

class BarboraItemPage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        title = self.driver.find_element(By.CLASS_NAME, "b-product-info--title").text
        return title

    def get_price(self):
        return self.driver.find_element(By.XPATH, "//*[@id='fti-product-price--0']/meta[1]").get_attribute("content")

    # def get_size(self):


    def get_unit(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[3]/div[1]/div/div[1]/div[2]").text





