from locators.base_locators import TemplatesLocators


class TemplatesPage:
    def __init__(self, sb):
        self.sb = sb
        self.locators = TemplatesLocators

    def get_template_names(self):
        self.sb.wait_for_element_visible(self.locators.TEMPLATE_TITLES, timeout=30)
        templates = self.sb.find_elements(self.locators.TEMPLATE_TITLES)
        return [template.text for template in templates][:5]

    def get_active_template(self):
        return self.sb.get_text(self.locators.CURRENT_SELECTION)

    def navigate_to_templates(self):
        self.sb.wait_for_element_visible(self.locators.PROFILE_ICON, timeout=20)
        self.sb.click(self.locators.PROFILE_ICON)
        self.sb.click(self.locators.TEMPLATES_TAB)