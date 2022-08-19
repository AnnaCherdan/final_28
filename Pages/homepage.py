import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from Locators.locators import Locators
from usefull_methods import check_exists_by_xpath

class HomePage:
    def __init__(self, driver):
        

