import time
import pytest
import os, pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Locators.locators import Locators
from Pages.homepage import HomePage


# @pytest.mark.usefixtures('welcome')
class TestHomePage:

    def test_welcome_homepage(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        driver.implicitly_wait(10)
        driver.find_element(By.CLASS_NAME, 'b-header-b-logo-wrapper').click()

    def test_discount_school(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        driver.find_element(By.CLASS_NAME, 'b-header-b-logo-e-discount').click()

    def test_books(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        ActionChains.move_to_element(driver.find_element(By.CLASS_NAME, 'b-header-b-menu-e-text'))



