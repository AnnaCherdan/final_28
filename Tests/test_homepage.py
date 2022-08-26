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
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_logo()
        assert driver.current_url == 'https://www.labirint.ru/'

    # def test_clickable_discount(self):
    #     driver = webdriver.Chrome()
    #     driver.set_window_size(1400, 700)
    #     driver.get('https://www.labirint.ru/')
    #     homepage = HomePage(driver)
    #     homepage.click_discount()
    #     assert driver.find_element(By.CLASS_NAME, 'block-link-title')

    def test_books_best(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_best()
        assert driver.current_url == 'https://www.labirint.ru/best/'

    def test_books_all(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_all_books()
        assert driver.current_url == 'https://www.labirint.ru/books/'

    def test_books_bilinguals(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_bilinguals()
        assert driver.current_url == 'https://www.labirint.ru/genres/2827/'

    def test_children_all_book(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_children_all_books()
        assert driver.current_url == 'https://www.labirint.ru/genres/1850/'

    def test_children_leisure(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_children_leisure()
        assert driver.current_url == 'https://www.labirint.ru/genres/2048/'

    def test_all_manga_comics_art(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        # homepage = HomePage(driver)
        # homepage.click_children_leisure()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'b-header-b-menu-e-text')))
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element(By.CLASS_NAME, 'b-header-b-menu-e-text'))
        actions.perform()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(), 'Комиксы, Манга, Артбуки')]")))
        actions.move_to_element(
            driver.find_element(By.XPATH, "//span[contains(text(), 'Комиксы, Манга, Артбуки')]"))
        actions.perform()
        actions.move_to_element(
            driver.find_element(By.XPATH, "//*[@id='header-genres']/div[1]/ul[1]/li[5]/ul[1]/li[3]/a[1]"))
        actions.click()
        actions.perform()
        assert driver.current_url == 'https://www.labirint.ru/genres/2993/'











