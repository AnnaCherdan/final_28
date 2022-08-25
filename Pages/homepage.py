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
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)
        self.header_button_logo_lab = Locators.header_button_logo_lab
        self.header_button_books = Locators.header_button_books
        self.button_books_bilinguals = Locators.button_books_bilinguals
        self.only_bilinguals = Locators.only_bilinguals



    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path




