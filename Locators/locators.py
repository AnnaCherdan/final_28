from selenium.webdriver.common.by import By
# header objects


class Locators:
    Accept_conditions_text = '//*[@id="minwidth"]/div[4]/div[2]/p[1]'
    Accept_conditions_btn = '//*[@id="minwidth"]/div[4]/div[2]/button[1]'
    header_button_logo_lab = (By.CLASS_NAME, 'b-header-b-logo-wrapper')
    # Проверка кликабельности списка "Книги".
    header_button_books = (By.CLASS_NAME, 'b-header-b-menu-e-text')
    button_books_bilinguals = (By.XPATH, "//span[contains(text(), 'Билингвы и книги на иностранных языках')]")
    only_bilinguals = (By.XPATH, "//*[@id='header-genres']/div[1]/ul[1]/li[4]/ul[1]/li[4]/a[1]")

