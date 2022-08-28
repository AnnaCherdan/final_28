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
        self.child_books = Locators.child_books
        self.children_all_books = Locators.children_all_books
        self.children_leisure = Locators.children_leisure
        self.manga_comics_art = Locators.manga_comics_art
        self.all_manga_comics_art = Locators.all_manga_comics_art
        self.only_manga_button = Locators.only_manga_button
        self.youth_literature = Locators.youth_literature
        self.non_fiction_literature = Locators.non_fiction_literature
        self.non_fiction_literature_all = Locators.non_fiction_literature_all
        self.non_fiction_natural_sciences = Locators.non_fiction_natural_sciences
        self.periodicals = Locators.periodicals
        self.religion = Locators.religion
        self.all_religion = Locators.all_religion
        self.religious_studies = Locators.religious_studies
        self.educational_methodical_literature = Locators.educational_methodical_literature
        self.all_educational_methodical_literature = Locators.all_educational_methodical_literature
        self.pedagogy_educational_methodical_literature = Locators.pedagogy_educational_methodical_literature
        self.fiction_literature = Locators.fiction_literature
        self.all_fiction_literature = Locators.all_fiction_literature
        self.fantasy_fiction_literature = Locators.fantasy_fiction_literature
        self.small_book_reviews = Locators.small_book_reviews
        self.authors_books = Locators.authors_books
        self.header_button_school = Locators.header_button_school
        self.russian_languages_button = Locators.russian_languages_button
        self.six_class = Locators.six_class
        self.unified_state_exam = Locators.unified_state_exam
        self.games_button = Locators.games_button
        self.all_games = Locators.all_games
        self.games_and_toys = Locators.games_and_toys
        self.all_games_and_toys = Locators.all_games_and_toys
        self.small_toy_manufacturers = Locators.small_toy_manufacturers
        self.office_tools = Locators.office_tools
        self.book_accessories = Locators.book_accessories
        self.bookmarks = Locators.bookmarks

    def click_logo(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.header_button_logo_lab)))
        self.driver.find_element(By.CLASS_NAME, self.header_button_logo_lab).click()

    def click_best(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.header_button_best))
        actions.click()
        actions.perform()

    def click_all_books(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.header_button_all_books))
        actions.click()
        actions.perform()

    def click_bilinguals(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.button_books_bilinguals)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.button_books_bilinguals))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.only_bilinguals))
        actions.click()
        actions.perform()

    def click_children_all_books(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.child_books)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.child_books))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.children_all_books))
        actions.click()
        actions.perform()

    def click_children_leisure(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.child_books)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.child_books))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.children_leisure))
        actions.click()
        actions.perform()

    def click_all_manga_comics_art(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.manga_comics_art)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.manga_comics_art))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.all_manga_comics_art))
        actions.click()
        actions.perform()

    def click_only_manga_button(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.manga_comics_art)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.manga_comics_art))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.only_manga_button))
        actions.click()
        actions.perform()

    def click_youth_literature(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        self.driver.find_element(By.XPATH, self.youth_literature).click()

    def click_non_fiction_literature_all(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH,  self.non_fiction_literature)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH,  self.non_fiction_literature))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.non_fiction_literature_all))
        actions.click()
        actions.perform()

    def click_non_fiction_natural_sciences(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.non_fiction_literature)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.non_fiction_literature))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.non_fiction_natural_sciences))
        actions.click()
        actions.perform()

    def click_periodicals(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        self.driver.find_element(By.XPATH, self.periodicals).click()

    def click_all_religion(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.religion)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.religion))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.all_religion))
        actions.click()
        actions.perform()

    def click_religious_studies_(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.religion)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.religion))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.religious_studies))
        actions.click()
        actions.perform()

    def click_all_educational_methodical_literature(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.educational_methodical_literature)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.educational_methodical_literature))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.all_educational_methodical_literature))
        actions.click()
        actions.perform()

    def click_pedagogy_educational_methodical_literature(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.educational_methodical_literature)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.educational_methodical_literature))
        actions.perform()
        actions.send_keys(Keys.DOWN)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.pedagogy_educational_methodical_literature)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.pedagogy_educational_methodical_literature))
        actions.click()
        actions.perform()

    def click_all_fiction_literature(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.fiction_literature)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.fiction_literature))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.all_fiction_literature))
        actions.click()
        actions.perform()

    def click_fantasy_fiction_literature(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.fiction_literature)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.fiction_literature))
        actions.perform()
        # actions.send_keys(Keys.DOWN)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.fantasy_fiction_literature)))
        # actions.send_keys(Keys.DOWN)
        # actions.scroll_to_element(self.small_book_reviews)
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.fantasy_fiction_literature))
        actions.click()
        actions.perform()

    def click_small_book_reviews(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.small_book_reviews)).click()
        actions.perform()

    def click_author_books(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_books)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_books))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.authors_books)).click()
        actions.perform()

    def click_school_russian(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_school)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_school))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.russian_languages_button)).click()
        actions.perform()

    def click_school_six_class(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_school)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_school))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.six_class)).click()
        actions.perform()

    def click_school_unified_state_exam(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.header_button_school)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.header_button_school))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.unified_state_exam)).click()
        actions.perform()

    def click_all_games(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.games_button)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.games_button))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.all_games)).click()
        actions.perform()

    def click_all_games_and_toys(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.games_button)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.games_button))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.games_and_toys))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.all_games_and_toys))
        actions.click()
        actions.perform()

    def click_small_toy_manufacturers(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.games_button)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.games_button))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.small_toy_manufacturers)).click()
        actions.perform()

    def click_all_book_accessories(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.office_tools)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.office_tools))
        actions.perform()
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.book_accessories))
        actions.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.bookmarks)))
        actions.move_to_element(
            self.driver.find_element(By.XPATH, self.bookmarks))
        actions.click()
        actions.perform()

