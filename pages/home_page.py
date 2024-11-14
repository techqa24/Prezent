from locators.base_locators import HomePageLocators


class HomePage:
    def __init__(self, sb):
        self.sb = sb
        self.locators = HomePageLocators

    def generate_prompt(self):
        self.sb.wait_for_element_visible(self.locators.AUTO_GENERATOR, timeout=20)
        self.sb.click(self.locators.AUTO_GENERATOR)
        self.sb.wait_for_element_visible(self.locators.INPUT_PROMPT, timeout=20)
        self.sb.click(self.locators.INPUT_PROMPT)
        self.sb.click(self.locators.THIRD_SUGGESTION)
        self.sb.click(self.locators.GENERATE_BTN)