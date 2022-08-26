from selenium.webdriver.common.by import By
# header objects


class Locators:
    Accept_conditions_text = '//*[@id="minwidth"]/div[4]/div[2]/p[1]'
    Accept_conditions_btn = '//*[@id="minwidth"]/div[4]/div[2]/button[1]'
    # Проверка кликабельности кнопки "Лабиринт".
    header_button_logo_lab = 'b-header-b-logo-wrapper'
    # Проверка кликабельности кнопки "Книжные скидки".
    header_discount_logo = 'b-header-b-logo-e-discount'
    fin_discount_logo = 'block-link-title'
    # Проверка кликабельности списка кнопки "Книги".
    header_button_books = 'b-header-b-menu-e-text'
    header_button_best = "//*[@id='header-genres']/div[1]/ul[1]/li[2]/a[1]"
    header_button_all_books = '//*[@id="header-genres"]/div[1]/ul[1]/li[3]/a[1]'
    button_books_bilinguals = "//span[contains(text(), 'Билингвы и книги на иностранных языках')]"
    only_bilinguals = "//*[@id='header-genres']/div[1]/ul[1]/li[4]/ul[1]/li[4]/a[1]"
    child_books = "//span[contains(text(), 'Книги для детей')]"
    children_all_books = "//*[@id='header-genres']/div[1]/ul[1]/li[4]/ul[1]/li[3]/a[1]"
    children_leisure = '//*[@id="header-genres"]/div[1]/ul[1]/li[5]/ul[1]/li[5]/a[1]'
    manga_comics_art = "//span[contains(text(), 'Комиксы, Манга, Артбуки')]"
    all_manga_comics_art = '//*[@id="header-genres"]/div[1]/ul[1]/li[6]/ul[1]/li[3]/a[1]'
    only_manga_button = '//*[@id="header-genres"]/div[1]/ul[1]/li[6]/ul[1]/li[7]/a[1]'
    youth_literature = "//*[@id='header-genres']/div[1]/ul[1]/li[7]/a[1]"
    non_fiction_literature = "//span[contains(text(), 'Нехудожественная литература')]"
    non_fiction_all = '//*[@id="header-genres"]/div[1]/ul[1]/li[8]/ul[1]/li[3]/a[1]'
    non_fiction_natural_sciences = '//*[@id="header-genres"]/div[1]/ul[1]/li[8]/ul[1]/li[8]/a[1]'
    periodicals = '//*[@id="header-genres"]/div[1]/ul[1]/li[9]/a[1]'
    religion = "//span[contains(text(), 'Религия')]"
    all_religion = '//*[@id="header-genres"]/div[1]/ul[1]/li[10]/ul[1]/li[3]/a[1]'




