from typing import List
from selenium.webdriver.remote.webdriver import WebDriver
import booking.constants as const
import time
from selenium.webdriver.common.by import By
import os


# class BookingFiltration:
#     def __int__(self, driver: WebDriver):
#         self.driver = driver
#
#
#     def apply_star_rating(self, star_value):
#         star_filtration_box = self.driver.find_element(By.CLASS_NAME, 'div[data-filters-group="class"]')
#         star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')
#         print(len(star_child_elements))



        # for star_element in star_child_elements:
        #     if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
        #         star_element.click()
