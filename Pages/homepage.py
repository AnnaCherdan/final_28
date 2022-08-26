import time
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Pages.base import WebPage
from Pages.elements import WebElement
from Pages.elements import ManyWebElements

from selenium.webdriver.common.by import By
from Locators.locators import Locators
from usefull_methods import check_exists_by_xpath


class HomePage (object):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.header_button_logo_lab = Locators.header_button_logo_lab
        self.header_button_books = Locators.header_button_books
        self.header_button_best = Locators.header_button_best
        self.header_button_all_books = Locators.header_button_all_books
        self.button_books_bilinguals = Locators.button_books_bilinguals
        self.only_bilinguals = Locators.only_bilinguals
        self.header_discount_logo = Locators.header_discount_logo
        self.fin_discount_logo = Locators.fin_discount_logo
        self.children_all_books = Locators.children_all_books
        self.children_leisure = Locators.children_leisure
        self.manga_comics_art = Locators.manga_comics_art
        self.all_manga_comics_art = Locators.all_manga_comics_art
        self.only_manga_button = Locators.only_manga_button
        self.youth_literature = Locators.youth_literature

    def click_logo(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.header_button_logo_lab)))
        self.driver.find_element(By.CLASS_NAME, 'b-header-b-logo-wrapper').click()

    def click_discount(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.header_discount_logo)))
        self.driver.find_element(By.CLASS_NAME, 'b-header-b-logo-e-discount').click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.CLASS_NAME, 'block-link-title')))

    def click_best(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.CLASS_NAME, 'b-header-b-menu-e-text')))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CLASS_NAME, 'b-header-b-menu-e-text'))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, "//*[@id='header-genres']/div[1]/ul[1]/li[2]/a[1]"))
        actions.click()
        actions.perform()

    def click_all_books(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                      (By.CLASS_NAME, 'b-header-b-menu-e-text')))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CLASS_NAME, 'b-header-b-menu-e-text'))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, "//*[@id='header-genres']/div[1]/ul[1]/li[3]/a[1]"))
        actions.click()
        actions.perform()

    def click_bilinguals(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.CLASS_NAME, 'b-header-b-menu-e-text')))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CLASS_NAME, 'b-header-b-menu-e-text'))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.XPATH, "//span[contains(text(), 'Билингвы и книги на иностранных языках')]")))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, "//span[contains(text(), 'Билингвы и книги на иностранных языках')]"))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, "//*[@id='header-genres']/div[1]/ul[1]/li[4]/ul[1]/li[4]/a[1]"))
        actions.click()
        actions.perform()

    def click_children_all_books(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.CLASS_NAME, 'b-header-b-menu-e-text')))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CLASS_NAME, 'b-header-b-menu-e-text'))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.XPATH, "//span[contains(text(), 'Книги для детей')]")))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, "//span[contains(text(), 'Книги для детей')]"))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, "//*[@id='header-genres']/div[1]/ul[1]/li[5]/ul[1]/li[3]/a[1]"))
        actions.click()
        actions.perform()

    def click_children_leisure(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.CLASS_NAME, 'b-header-b-menu-e-text')))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CLASS_NAME, 'b-header-b-menu-e-text'))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.XPATH, "//span[contains(text(), 'Книги для детей')]")))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, "//span[contains(text(), 'Книги для детей')]"))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, "//*[@id='header-genres']/div[1]/ul[1]/li[5]/ul[1]/li[5]/a[1]"))
        actions.click()
        actions.perform()

    def click_all_manga_comics_art(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.CLASS_NAME, 'b-header-b-menu-e-text')))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CLASS_NAME, 'b-header-b-menu-e-text'))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.XPATH, "//span[contains(text(), 'Комиксы, Манга, Артбуки')]")))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, "//span[contains(text(), 'Комиксы, Манга, Артбуки')]"))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, '//*[@id="header-genres"]/div[1]/ul[1]/li[6]/ul[1]/li[3]/a[1]'))
        actions.click()
        actions.perform()

    def click_only_manga_button(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.CLASS_NAME, 'b-header-b-menu-e-text')))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CLASS_NAME, 'b-header-b-menu-e-text'))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.XPATH, "//span[contains(text(), 'Комиксы, Манга, Артбуки')]")))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, "//span[contains(text(), 'Комиксы, Манга, Артбуки')]"))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, '//*[@id="header-genres"]/div[1]/ul[1]/li[6]/ul[1]/li[7]/a[1]'))
        actions.click()
        actions.perform()

    def click_youth_literature(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                     (By.CLASS_NAME, 'b-header-b-menu-e-text')))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.CLASS_NAME, 'b-header-b-menu-e-text'))
        actions.perform()
        self.driver.find_element(By.XPATH, "//*[@id='header-genres']/div[1]/ul[1]/li[7]/a[1]").click()








