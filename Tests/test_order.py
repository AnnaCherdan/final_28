from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.orderpage import OrderPage


class TestOrderPage:
    def test_search_book(self):
        driver = webdriver.Chrome(executable_path='D:\\AllDoc\\AnnCherdan\\Final\\final_28\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = OrderPage(driver)
        homepage.click_search_author()
        assert driver.find_element(By.XPATH, "//*[@class='index-top-title']").is_displayed()

    def test_search_order_book(self):
        driver = webdriver.Chrome(executable_path='D:\\AllDoc\\AnnCherdan\\Final\\final_28\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = OrderPage(driver)
        homepage.click_search_order_book()
        assert driver.current_url == 'https://www.labirint.ru/books/767041/'

    def test_hold_over_stash_book(self):
        driver = webdriver.Chrome(executable_path='D:\\AllDoc\\AnnCherdan\\Final\\final_28\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = OrderPage(driver)
        homepage.click_hold_over_stash_book()
        assert driver.find_element(By.XPATH, "//span[contains(text(), 'Аналитическая психология')]").is_displayed()
