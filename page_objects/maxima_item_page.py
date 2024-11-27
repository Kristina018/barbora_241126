from selenium.webdriver.common.by import By

class MaximaItemPage:
    
    def __init__(self, driver):
        self.manufacturer = None
        self.driver = driver

    def fill(self):
        mip = MaximaItemPage(self.driver)
        info = self.driver.find_element(By.CLASS_NAME, 'b-product-info--info1')
        titles = info.find_elements(By.TAG_NAME, 'dt')
        values = info.find_elements(By.TAG_NAME, 'dd')
        dict = {}
        for i in range(0, len(titles)):
            value = values[i].text
            if value == "":
                value = values[i].find_element(By.TAG_NAME, 'img').get_attribute("alt")
            dict[titles[i].text] = value
        print(dict)
        self.manufacturer = dict['Kilmės šalis:']