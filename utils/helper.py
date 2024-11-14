import json
import os

from locators.base_locators import TemplatesLocators


def login(self):
    # Load credentials
    config_path = os.path.join(os.path.dirname(__file__), '../config.json')
    with open(config_path) as config_file:
        config = json.load(config_file)

    # Perform login actions
    self.open(config['url'])
    self.type("#username", config['username'])
    self.click("//button[@id='continue']")
    self.type("#password", config['password'])
    self.click("button[id='submit']")


def select_first_option(self, list_locator, first_option_locator):
    self.sb.wait_for_element_visible(list_locator, timeout=20)
    options = self.sb.find_elements(list_locator)
    print("Available List of Options:")
    for option in options:
        print(option.text)
    self.sb.wait_for_element_visible(first_option_locator, timeout=20)
    self.sb.click(first_option_locator)
    print(f"Selected Option is: {options[0].text}")


def logout(self):
    self.click(TemplatesLocators.BASICS_TAB)
    self.click(TemplatesLocators.SIGN_OUT)

def navigate_to_profile(self):
    self.wait_for_element_visible(TemplatesLocators.PROFILE_ICON, timeout=30)
    self.click(TemplatesLocators.PROFILE_ICON)