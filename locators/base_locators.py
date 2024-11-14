class BaseLocators:
    """Base class containing common locators across pages"""
    PROFILE_ICON = "//div[@name='profile-icon']"
    SIGN_OUT = "//span[text()=' Sign Out ']"

class TemplatesLocators(BaseLocators):
    TEMPLATES_TAB = "#templates-tab"  # Using CSS if possible for better performance
    TEMPLATE_TITLES = "div.v-card__title.cardTitleForViewer"  # CSS selector
    CURRENT_SELECTION = "//span[@class='v-btn__content'][contains(text(), 'Current selection')]"
    BASICS_TAB = "#basics-tab"
class HomePageLocators(BaseLocators):
    AUTO_GENERATOR = "//div[text()='Auto Generator ']"
    THIRD_SUGGESTION = "//p[@id='generate-suggested-2']"
    GENERATE_BTN = "//span[text()=' Generate ']"
    INPUT_PROMPT = "//textarea[@placeholder='Enter your prompt here…']"
class FingerPrintLocators(BaseLocators):
    FINGERPRINT_TAB = "#fingerprint-tab"
    RETAKE_FP = "//div[@class='btn-retake']"
    DISCOVER_FP = "#discover"
    FIRST_SLIDE="//div[@class='card-item'][1]"
    SECOND_SLIDE = "//div[@class='card-item'][2]"
    BACK_BTN = "//div[@class='back-button']"
    COMMON_PREF = "//span[@class='selection-title']"
    FIRST_PREF="//span[@class='selection-title'][1]"
    SELECTED_PREF = "//div[@class='selection highlight']//span[@class='selection-title']"
    SELECTED_SLIDE = "//div[@class='v-card v-card--link v-sheet theme--light selected   ']"
    NEXT_BTN = "#show-fingerprint-for-btn--auto"
    INDUSTRIES = "//div[@class='cards-wrapper']//div[@class='item-name']"
    FIRST_INDUSTRY = "//div[@class='cards-wrapper']//div[@class='item-name'][1]"
    FUNCTIONS = "//div[@class='cards-wrapper industry']//div[@class='item-name']"
    FIRST_FUNC = "//div[@class='cards-wrapper industry']//div[@class='item-name'][1]"
    GROUP = "//div[@class='selection group-items']//span[@class='selection-title']"
    FIRST_GROUP = "//div[@class='selection group-items']//span[@class='selection-title'][1]"
    REGION_HEADER = "//div[@class='header' and text()='Which region do you focus on?']"
    JOB_TITLE = "//input[@placeholder='Job Title']"
    JOB_LIST = "//div[@class='v-list-item__title']"
    SKIP_BTN = "//div[@class='skip-button']"
    VIEW_FP_BTN = "//button/span[text()=' View my fingerprint ']"
    BACK_TO_PRSNT = "//button//span[contains(text(), 'Back to Prezent')]"