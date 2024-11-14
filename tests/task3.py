from seleniumbase import BaseCase
from pages.home_page import HomePage
from utils.helper import login, logout, navigate_to_profile


class Task2(BaseCase):

    def test_task3(self):
        login(self)
        home_page = HomePage(self)
        home_page.generate_prompt()