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
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
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
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_best()
        assert driver.current_url == 'https://www.labirint.ru/best/'

    def test_books_all(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_all_books()
        assert driver.current_url == 'https://www.labirint.ru/books/'

    def test_books_bilinguals(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_bilinguals()
        assert driver.current_url == 'https://www.labirint.ru/genres/2827/'

    def test_children_all_book(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_children_all_books()
        assert driver.current_url == 'https://www.labirint.ru/genres/1850/'

    def test_children_leisure(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_children_leisure()
        assert driver.current_url == 'https://www.labirint.ru/genres/2048/'

    def test_all_manga_comics_art(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_all_manga_comics_art()
        assert driver.current_url == 'https://www.labirint.ru/genres/2993/'

    def test_only_manga_button(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru/')
        homepage = HomePage(driver)
        homepage.click_only_manga_button()
        assert driver.current_url == 'https://www.labirint.ru/genres/2684/'

    def test_youth_literature(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_youth_literature()
        assert driver.current_url == 'https://www.labirint.ru/genres/3066/'

    def test_non_fiction_all(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_non_fiction_all()
        assert driver.current_url == 'https://www.labirint.ru/genres/3000/'

    def test_non_fiction_natural_sciences(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_non_fiction_natural_sciences()
        assert driver.current_url == 'https://www.labirint.ru/genres/1854/'

    def test_periodicals(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_periodicals()
        assert driver.current_url == 'https://www.labirint.ru/genres/2137/'

    def test_all_religion(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28\\chromedriver')
        driver.set_window_size(1400, 700)
        driver.get('https://www.labirint.ru')
        homepage = HomePage(driver)
        homepage.click_all_religion()
        assert driver.current_url == 'https://www.labirint.ru/genres/2386/'
