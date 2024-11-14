from seleniumbase import BaseCase
from pages.templates_page import TemplatesPage
from utils.helper import login,logout

class Task1(BaseCase):

    def test_task1(self):
        login(self)
        templates_page = TemplatesPage(self)
        templates_page.navigate_to_templates()
        template_names = templates_page.get_template_names()
        print("First 5 templates:", template_names)
        active_template = templates_page.get_active_template()
        print("Active template:", active_template)
        logout(self)
