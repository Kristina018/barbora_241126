from models.db import DB
from page_objects.barbora_item_page import BarboraItemPage

import datetime
from selenium.webdriver.common.by import By

class BarboraItem:

    def __init__(self, driver):
        self.price = None
        self.size = None
        self.manufacturer = None
        self.country = None
        # self.dict = None
        self.title = None
        self.driver = driver
        self.db = DB()


    def fill(self):
        bip = BarboraItemPage(self.driver)
        self.title = bip.get_title()
        # self.manufacturer = mip.get_manufacturer()
        # self.size = bip.get_size()
        self.price = bip.get_price()

        info = self.driver.find_element(By.CLASS_NAME, 'b-product-info--info1')
        titles = info.find_elements(By.TAG_NAME, 'dt')
        values = info.find_elements(By.TAG_NAME, 'dd')
        dctnr = {}
        for i in range(0, len(titles)):
            value = values[i].text
            if value == "":
                value = values[i].find_element(By.TAG_NAME, 'img').get_attribute("alt")
            dctnr[titles[i].text] = value
        print(dctnr)

        self.country = dctnr['Kilmės šalis:']
        self.manufacturer = dctnr['Tiekėjo kontaktai:'] if 'Tiekėjo kontaktai:' in dctnr else "na"
        self.size = dctnr['Grynasis kiekis (g/ml):'] if 'Grynasis kiekis (g/ml):' in dctnr else "na"


    # def fill(self):
    #     mip = MaximaItemPage(self.driver)
    #     info = self.driver.find_element(By.CLASS_NAME, 'b-product-info--info1')
    #     titles = info.find_elements(By.TAG_NAME, 'dt')
    #     values = info.find_elements(By.TAG_NAME, 'dd')
    #     dict = {}
    #     for i in range(0, len(titles)):
    #         value = values[i].text
    #         if value == "":
    #             value = values[i].find_element(By.TAG_NAME, 'img').get_attribute("alt")
    #         dict[titles[i].text] = value
    #     print(dict)
    #     self.manufacturer = dict['Kilmės šalis:']



    def save(self):
        # self.db = DB()
        query = ("INSERT INTO `prekes`(`country_of_origin`, `title`, `manufacturer`, `price`, `unit`, `size`, `property`, `category`, `shop`, `last_updated`) VALUES ("
                 "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        self.db.conn.cursor().execute(query, (self.country, self.title, self.manufacturer, self.price, "vnt", self.size, "prop", "categ", "Barbora", datetime.datetime.now())) # "2024-11-26 14:36:01"
        self.db.conn.commit()
        self.db.close()