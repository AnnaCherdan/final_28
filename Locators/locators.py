from selenium.webdriver.common.by import By
# header objects


class Locators:
    Accept_conditions_text = '//*[@id="minwidth"]/div[4]/div[2]/p[1]'
    Accept_conditions_btn = '//*[@id="minwidth"]/div[4]/div[2]/button[1]'
    # Проверка кликабельности кнопки "Лабиринт".
    header_button_logo_lab = 'b-header-b-logo-wrapper'
    # Проверка кликабельности списка кнопки "Книги" в "шапке" сайта.
    header_button_books = '//a[@href="/books/"]'
    header_button_best = "//*[@id='header-genres']/div[1]/ul[1]/li[2]/a[1]"
    header_button_all_books = '//*[@id="header-genres"]/div[1]/ul[1]/li[3]/a[1]'
    button_books_bilinguals = "//span[contains(text(), 'Билингвы и книги на иностранных языках')]"
    only_bilinguals = "//*[@id='header-genres']/div[1]/ul[1]/li[4]/ul[1]/li[4]/a[1]"
    child_books = "//span[contains(text(), 'Книги для детей')]"
    children_all_books = "//*[@id='header-genres']/div[1]/ul[1]/li[5]/ul[1]/li[3]/a[1]"
    children_leisure = '//*[@id="header-genres"]/div[1]/ul[1]/li[5]/ul[1]/li[5]/a[1]'
    manga_comics_art = "//span[contains(text(), 'Комиксы, Манга, Артбуки')]"
    all_manga_comics_art = '//*[@id="header-genres"]/div[1]/ul[1]/li[6]/ul[1]/li[3]/a[1]'
    only_manga_button = '//*[@id="header-genres"]/div[1]/ul[1]/li[6]/ul[1]/li[7]/a[1]'
    youth_literature = "//*[@id='header-genres']/div[1]/ul[1]/li[7]/a[1]"
    non_fiction_literature = "//span[contains(text(), 'Нехудожественная литература')]"
    non_fiction_literature_all = '//*[@id="header-genres"]/div[1]/ul[1]/li[8]/ul[1]/li[3]/a[1]'
    non_fiction_natural_sciences = '//*[@id="header-genres"]/div[1]/ul[1]/li[8]/ul[1]/li[8]/a[1]'
    periodicals = '//*[@id="header-genres"]/div[1]/ul[1]/li[9]/a[1]'
    religion = "//span[contains(text(), 'Религия')]"
    all_religion = '//*[@id="header-genres"]/div[1]/ul[1]/li[10]/ul[1]/li[3]/a[1]'
    religious_studies = '//*[@id="header-genres"]/div[1]/ul[1]/li[10]/ul[1]/li[6]/a[1]'
    educational_methodical_literature = "//span[contains(text(), 'Учебная, методическая литература и словари')]"
    all_educational_methodical_literature = '//*[@id="header-genres"]/div[1]/ul[1]/li[11]/ul[1]/li[3]/a[1]'
    pedagogy_educational_methodical_literature = '//*[@id="header-genres"]/div[1]/ul[1]/li[11]/ul[1]/li[10]/a[1]'
    fiction_literature = "//span[contains(text(), 'Художественная литература')]"
    all_fiction_literature = '//*[@id="header-genres"]/div[1]/ul[1]/li[12]/ul[1]/li[3]/a[1]'
    fantasy_fiction_literature = '//*[@id="header-genres"]/div[1]/ul[1]/li[12]/ul[1]/li[16]/a[1]'
    small_book_reviews = '//*[@id="header-genres"]/div[1]/ul[1]/li[13]/span[1]/a[2]'
    authors_books = '//*[@id="header-genres"]/div[1]/ul[1]/li[13]/span[1]/a[7]'
    # Проверка кликабельности списка кнопки "Школа" в "шапке" сайта.
    header_button_school = '//a[@href="/school/"]'
    russian_languages_button = '//*[@id="header-school"]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]'
    six_class = '//*[@id="header-school"]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[6]/a[1]'
    unified_state_exam = '//*[@id="header-school"]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[2]/a[1]'






