from selenium.webdriver.common.by import By


class ButtonsPage:

    def __init__(self, driver):
        self.driver = driver

    radiobutton1 = (By.XPATH, "input[value='radio1']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getRadioButton1(self):
        return self.driver.find_element(*ButtonsPage.radiobutton1)


