from selenium.webdriver.common.by import By

class BarboraItemPage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(By.CLASS_NAME, "b-product-info--title").text
        # return self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/h1").text

    # def get_manufacturer(self):
    #     return self.driver.find_element(By.CLASS_NAME, "b-dl-align-left b-product-info--info1")
    #
    # def get_size(self):
    #     blokas = self.driver.find_element(By.CLASS_NAME, "b-dl-align-left b-product-info--info1")
    #     dydis = blokas.get_attribute('Grynasis kiekis (g/ml):')
    #     return dydis

    def get_price(self):
        return self.driver.find_element(By.XPATH, "//*[@id='fti-product-price--0']/meta[1]").get_attribute("content")




