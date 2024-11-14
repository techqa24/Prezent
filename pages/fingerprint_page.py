import time
from asyncio import timeout

from utils.helper import select_first_option
from locators.base_locators import FingerPrintLocators
import random


class FingerprintPage:
    def __init__(self, sb):
        self.sb = sb
        self.locators = FingerPrintLocators


    def navigate_to_fingerprint_tab(self):
        self.sb.wait_for_element_visible(self.locators.PROFILE_ICON, timeout=20)
        self.sb.click(self.locators.PROFILE_ICON)
        self.sb.click(self.locators.FINGERPRINT_TAB)



    def retake_fp_test(self):
        self.sb.wait_for_element_visible(self.locators.RETAKE_FP, timeout=30)
        self.sb.click(self.locators.RETAKE_FP)
        self.sb.wait_for_element_visible(self.locators.DISCOVER_FP, timeout=30)
        self.sb.click(self.locators.DISCOVER_FP)
        for i in range(0, 6):
            slide_to_click = random.choice([self.locators.FIRST_SLIDE, self.locators.SECOND_SLIDE])
            self.sb.click(slide_to_click)
            time.sleep(1) #adding as a safety net, to avoid any failures.
            self.sb.wait_for_element_not_visible(self.locators.SELECTED_SLIDE, timeout=20)
        select_first_option(self,self.locators.COMMON_PREF,self.locators.FIRST_PREF)
        self.sb.click(self.locators.NEXT_BTN)
        select_first_option(self, self.locators.INDUSTRIES, self.locators.FIRST_INDUSTRY)
        self.sb.click(self.locators.NEXT_BTN)
        select_first_option(self, self.locators.FUNCTIONS, self.locators.FIRST_FUNC)
        self.sb.click(self.locators.NEXT_BTN)
        select_first_option(self, self.locators.GROUP, self.locators.FIRST_GROUP)
        self.sb.click(self.locators.NEXT_BTN)
        self.sb.wait_for_element_visible(self.locators.REGION_HEADER,timeout=10)
        select_first_option(self, self.locators.INDUSTRIES, self.locators.FIRST_INDUSTRY)
        self.sb.click(self.locators.NEXT_BTN)
        self.sb.wait_for_element_visible(self.locators.JOB_TITLE, timeout=10)
        self.sb.type(self.locators.JOB_TITLE,"Access Analyst")
        self.sb.click(self.locators.NEXT_BTN)
        self.sb.wait_for_element_visible(self.locators.SKIP_BTN)
        self.sb.click(self.locators.SKIP_BTN)
        self.sb.wait_for_element_visible(self.locators.VIEW_FP_BTN)
        self.sb.click(self.locators.VIEW_FP_BTN)
        self.sb.wait_for_element_visible(self.locators.BACK_TO_PRSNT, timeout=20)
        self.sb.scroll_to(self.locators.BACK_TO_PRSNT)
        self.sb.click(self.locators.BACK_TO_PRSNT)






