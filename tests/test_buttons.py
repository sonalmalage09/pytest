import pytest

from pageObjects.practisePage.buttons import ButtonsPage
from utilities.BaseClass import BaseClass


class TestButtons(BaseClass):

    def test_formSubmission(self):
        buttons_page = ButtonsPage(self.driver)
        buttons_page.getRadioButton1().click()
