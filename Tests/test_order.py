from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.orderpage import OrderPage


class TestOrderPage:
    def test_search_book(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28_7\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = OrderPage(driver)
        homepage.click_search_author()
        assert driver.find_element(By.XPATH, "//*[@class='index-top-title']").is_displayed()

    def test_search_order_book(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28_7\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = OrderPage(driver)
        homepage.click_search_order_book()
        assert driver.current_url == 'https://www.labirint.ru/books/767041/'

    def test_hold_over_stash_book(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28_7\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = OrderPage(driver)
        homepage.click_hold_over_stash_book()
        assert driver.find_element(By.XPATH, "//span[contains(text(), 'Книга в отложенных')]").is_displayed()

    def test_click_compare_book(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28_7\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = OrderPage(driver)
        homepage.click_compare_book()
        assert driver.find_element(By.XPATH, "//span[contains(text(), 'Сравнить')]").is_displayed()

    def test_cod_for_good_time(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28_7\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = OrderPage(driver)
        homepage.cod_for_good_time()

    def test_add_to_cart(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28_7\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = OrderPage(driver)
        homepage.click_add_to_cart()
        assert driver.find_element(By.XPATH, '//*[@id="ui-id-4"]').is_displayed()

    def test_book_in_cart(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28_7\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = OrderPage(driver)
        homepage.click_add_to_cart()
        assert driver.find_element(By.XPATH, '//*[@id="ui-id-4"]').is_displayed()

    def test_clear_cart(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Python\\final_28_7\\chromedriver.exe')
        driver.set_window_size(1900, 1200)
        driver.get('https://www.labirint.ru')
        homepage = OrderPage(driver)
        homepage.click_clear_cart()
        assert driver.find_element(By.XPATH, "//span[contains(text(), 'Ваша корзина пуста. Почему?')]").is_displayed()
