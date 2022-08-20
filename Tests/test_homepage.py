from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures('welcome')
class TestHomePage:

    def test_homepage(self):
        pass