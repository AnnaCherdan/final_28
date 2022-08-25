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
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                     (By.CLASS_NAME, 'b-header-b-menu-e-text')))
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element(By.CLASS_NAME, 'b-header-b-menu-e-text'))
        actions.perform()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                     (By.XPATH, "//span[contains(text(), 'Билингвы и книги на иностранных языках')]")))
        actions.move_to_element(
            driver.find_element(By.XPATH, "//span[contains(text(), 'Билингвы и книги на иностранных языках')]"))
        actions.perform()
        actions.move_to_element(
                driver.find_element(By.XPATH, "//*[@id='header-genres']/div[1]/ul[1]/li[4]/ul[1]/li[4]/a[1]"))
        actions.click()
        actions.perform()
        assert driver.current_url == 'https://www.labirint.ru/genres/2827/'

    def test_books(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_bilinguas()
        assert driver.current_url == 'https://www.labirint.ru/genres/2827/'





