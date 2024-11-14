from seleniumbase import BaseCase
from pages.fingerprint_page import FingerprintPage
from utils.helper import login, logout, navigate_to_profile


class Task2(BaseCase):

    def test_task2(self):
        login(self)
        fingerprintpage = FingerprintPage(self)
        fingerprintpage.navigate_to_fingerprint_tab()
        fingerprintpage.retake_fp_test()
        navigate_to_profile(self)
        logout(self)