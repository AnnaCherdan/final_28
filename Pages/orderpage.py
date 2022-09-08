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
        self.really_hold_over_stash_book = Locators.really_hold_over_stash_book
        self.my_lab = Locators.my_lab
        self.discount_code_field = Locators.discount_code_field
        self.button_auth = Locators.button_auth
        self.compare_book = Locators.compare_book
        self.hold_over = Locators.hold_over
        self.cart_buy_book = Locators.cart_buy_book
        self.hold_over_cart = Locators.hold_over_cart
        self.html = Locators.html
        self.direct_book = Locators.direct_book
        self.clear_cart = Locators.clear_cart

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

    def click_compare_book(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.search)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys("rfhk uecnfd .yu")
        actions.perform()
        self.driver.find_element(By.XPATH, self.search_button).click()
        self.driver.find_element(By.XPATH, self.search_order_book).click()
        self.driver.find_element(By.XPATH, self.compare_book).click()

    def cod_for_good_time(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_lab)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.my_lab)).click()
        actions.perform()
        self.driver.find_element(By.XPATH, self.discount_code_field).clear()
        actions.move_to_element(self.driver.find_element(By.XPATH, self.discount_code_field))
        self.driver.find_element(By.XPATH, self.discount_code_field).send_keys('FB16-4A69-9F0F')
        actions.move_to_element(self.driver.find_element(By.XPATH, self.button_auth))
        self.driver.find_element(By.XPATH, self.button_auth).click()
        time.sleep(10)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_lab)))
        actions.move_to_element(self.driver.find_element(By.XPATH, self.my_lab))
        self.driver.find_element(By.XPATH, self.my_lab).click()
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
        html = self.driver.find_element(By.TAG_NAME, self.html)
        html.send_keys(Keys.PAGE_DOWN)
        html.send_keys(Keys.PAGE_DOWN)
        self.driver.find_element(By.XPATH, self.hold_over_cart).click()
        time.sleep(10)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.cart_buy_book)))
        self.driver.find_element(By.XPATH, self.cart_buy_book).click()

    def click_add_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_lab)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.my_lab)).click()
        actions.perform()
        self.driver.find_element(By.XPATH, self.discount_code_field).clear()
        actions.move_to_element(self.driver.find_element(By.XPATH, self.discount_code_field))
        self.driver.find_element(By.XPATH, self.discount_code_field).send_keys('FB16-4A69-9F0F')
        actions.move_to_element(self.driver.find_element(By.XPATH, self.button_auth))
        self.driver.find_element(By.XPATH, self.button_auth).click()
        time.sleep(20)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_lab)))
        actions.move_to_element(self.driver.find_element(By.XPATH, self.my_lab))
        self.driver.find_element(By.XPATH, self.my_lab).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.search)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys("rfhk uecnfd .yu")
        actions.perform()
        self.driver.find_element(By.XPATH, self.search_button).click()
        self.driver.find_element(By.XPATH, self.cart_buy_book).click()

    def book_in_cart(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_lab)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.my_lab)).click()
        actions.perform()
        self.driver.find_element(By.XPATH, self.discount_code_field).clear()
        actions.move_to_element(self.driver.find_element(By.XPATH, self.discount_code_field))
        self.driver.find_element(By.XPATH, self.discount_code_field).send_keys('FB16-4A69-9F0F')
        actions.move_to_element(self.driver.find_element(By.XPATH, self.button_auth))
        self.driver.find_element(By.XPATH, self.button_auth).click()
        time.sleep(10)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_lab)))
        actions.move_to_element(self.driver.find_element(By.XPATH, self.my_lab))
        self.driver.find_element(By.XPATH, self.my_lab).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.search)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys("rfhk uecnfd .yu")
        actions.perform()
        self.driver.find_element(By.XPATH, self.search_button).click()
        self.driver.find_element(By.XPATH, self.search_order_book).click()
        self.driver.find_element(By.XPATH, self.direct_book).click()

    def click_clear_cart(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_lab)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.my_lab)).click()
        actions.perform()
        self.driver.find_element(By.XPATH, self.discount_code_field).clear()
        actions.move_to_element(self.driver.find_element(By.XPATH, self.discount_code_field))
        self.driver.find_element(By.XPATH, self.discount_code_field).send_keys('FB16-4A69-9F0F')
        actions.move_to_element(self.driver.find_element(By.XPATH, self.button_auth))
        self.driver.find_element(By.XPATH, self.button_auth).click()
        time.sleep(10)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_lab)))
        actions.move_to_element(self.driver.find_element(By.XPATH, self.my_lab))
        self.driver.find_element(By.XPATH, self.my_lab).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.search)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys("rfhk uecnfd .yu")
        actions.perform()
        self.driver.find_element(By.XPATH, self.search_button).click()
        self.driver.find_element(By.XPATH, self.cart_buy_book).click()
        self.driver.find_element(By.XPATH, self.clear_cart).click()

