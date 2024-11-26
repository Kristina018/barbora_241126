from models.db import DB
from page_objects.barbora_item_page import BarboraItemPage
import datetime
from selenium.webdriver.common.by import By



class BarboraItem:

    def __init__(self, driver):
        self.info_dict = None
        self.title = None
        self.driver = driver

    # def fill(self):
    #     bip = BarboraItemPage(self.driver)
    #     self.title = bip.get_title()
    #     self.manufacturer = bip.get_manufacturer()
    #     # self.size = bip.get_size()
    #     # self.price = bip.get_price()

    def fill(self):
        bip = BarboraItemPage(self.driver)
        info = self.driver.find_element(By.CLASS_NAME, 'b-product-info--info1')
        titles = info.find_elements(By.TAG_NAME, 'dt')
        values = info.find_elements(By.TAG_NAME, 'dd')
        self.info_dict = {}
        for i in range(1, len(titles)):
            value = values[i].text
            if value == "":
                value = values[i].find_element(By.TAG_NAME, 'img').get_attribute("alt")
            self.info_dict[titles[i].text] = value
        print(self.info_dict)
        return self.info_dict

    def save(self):
        self.db = DB()
        query = ("INSERT INTO `prekes`(`title`, `manufacturer`, `price`, `unit`, `size`, `property`, `category`, `shop`, `last_updated`) VALUES ("
                 "%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        self.db.conn.cursor().execute(query, (self.title, "mnfctr", 0.1, "vnt", 0, "prop", "categ", "Barbora", "2024-11-24"))
        self.db.conn.commit()
        self.db.close()