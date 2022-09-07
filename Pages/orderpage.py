import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Locators.locators import Locators


class OrderPage(object):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.search = Locators.search
        self.search_button = Locators.search_button
        self.search_author = Locators.search_author
        self.search_order_book = Locators.search_order_book
        self.hold_over_stash_book = Locators.hold_over_stash_book
        self.hold_over_stash = Locators.hold_over_stash

    def click_search_author(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.search)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys("rfhk uecnfd .yu")
        actions.perform()
        self.driver.find_element(By.XPATH, self.search_button).click()

    def click_search_order_book(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.search)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys("rfhk uecnfd .yu")
        actions.perform()
        self.driver.find_element(By.XPATH, self.search_button).click()
        self.driver.find_element(By.XPATH, self.search_order_book).click()

    def click_hold_over_stash_book(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.search)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys("rfhk uecnfd .yu")
        actions.perform()
        self.driver.find_element(By.XPATH, self.search_button).click()
        self.driver.find_element(By.XPATH, self.search_order_book).click()
        self.driver.find_element(By.XPATH, self.hold_over_stash_book).click()
        actions.move_to_element(self.driver.find_element(By.XPATH, self.hold_over_stash))
        self.driver.find_element(By.XPATH, self.hold_over_stash).click()

