from datetime import datetime, timedelta
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import selenium_timetable.constants as c

class TimetableDriver(webdriver.Firefox):
    def __init__(self, settings: dict[str, str], timestamp: int, light_image_path: str, dark_image_path: str) -> None:
        self.light_image_path = light_image_path
        self.dark_image_path = dark_image_path
        self.date = datetime.fromtimestamp(timestamp)
        self.settings = settings

        options = Options()
        options.add_argument("--window-size=1280,840")

        super().__init__(options)
        self.minimize_window()

    def screenshot_bromcom(self) -> None:
        self.get(c.BROMCOM_STUDENT_LOGIN_URL)

        WebDriverWait(self, c.TIMEOUT).until(EC.visibility_of_element_located(c.BROMCOM_SCHOOL_INPUT_LOCATOR))

        self.find_element(*c.BROMCOM_SCHOOL_INPUT_LOCATOR).send_keys(self.settings["school"])
        self.find_element(*c.BROMCOM_USERNAME_INPUT_LOCATOR).send_keys(self.settings["username"])
        self.find_element(*c.BROMCOM_PASSWORD_INPUT_LOCATOR).send_keys(self.settings["password"])

        self.find_element(*c.BROMCOM_LOGIN_BUTTON_LOCATOR).click()

        WebDriverWait(self, c.TIMEOUT).until(EC.visibility_of_element_located(c.BROMCOM_LOADED_INDICATOR_LOCATOR))

        self.get(c.BROMCOM_TIMETABLE_URL)

        WebDriverWait(self, c.TIMEOUT).until(EC.visibility_of_element_located(c.BROMCOM_TIMETABLE_LOCATOR))

        # 1 day is subtracted as timetable is loaded after that day
        self.execute_script(c.BROMCOM_SET_DATE_JS(datetime.strftime(self.date - timedelta(days=1), r"%m-%d-%Y")))

        time.sleep(1) # Wait for timetable to load

        if self.light_image_path:
            self.find_element(*c.BROMCOM_TIMETABLE_LOCATOR).screenshot(self.light_image_path)

        if self.dark_image_path:
            self.execute_script(c.BROMCOM_DARK_THEME_JS)

            self.find_element(*c.BROMCOM_TIMETABLE_LOCATOR).screenshot(self.dark_image_path)

    def screenshot_satchel_one(self) -> None:
        self.get(c.SATCHEL_ONE_STUDENT_LOGIN_URL)

        WebDriverWait(self, c.TIMEOUT).until(EC.visibility_of_element_located(c.SATCHEL_ONE_SCHOOL_SEARCH_INPUT_LOCATOR))
        self.find_element(*c.SATCHEL_ONE_SCHOOL_SEARCH_INPUT_LOCATOR).send_keys(self.settings["school"])

        WebDriverWait(self, c.TIMEOUT).until(EC.visibility_of_element_located(c.SATCHEL_ONE_SUGGESTED_SCHOOL_NAME_OPTION_LOCATOR))
        self.find_element(*c.SATCHEL_ONE_SUGGESTED_SCHOOL_NAME_OPTION_LOCATOR).click()

        self.find_element(*c.SATCHEL_ONE_USERNAME_INPUT_LOCATOR).send_keys(self.settings["username"])
        self.find_element(*c.SATCHEL_ONE_PASSWORD_INPUT_LOCATOR).send_keys(self.settings["password"])

        self.find_element(*c.SATCHEL_ONE_DECLINE_COOKIES_BUTTON_LOCATOR).click()
        self.find_element(*c.SATCHEL_ONE_LOGIN_BUTTON_LOCATOR).click()

        self.get(c.SATCHEL_ONE_TIMETABLE_URL(datetime.strftime(self.date, r"%Y-%m-%d")))

        WebDriverWait(self, c.TIMEOUT).until(EC.visibility_of_element_located(c.SATCHEL_ONE_TIMETABLE_LOCATOR))

        # Removes unnecessary elements that appear in the screenshot
        self.execute_script(c.SATCHEL_ONE_REMOVE_UNNECESSARY_ELEMENTS_JS)

        if self.light_image_path:
            self.find_element(*c.SATCHEL_ONE_TIMETABLE_LOCATOR).screenshot(self.light_image_path)

        if self.dark_image_path:
            self.execute_script(c.SATCHEL_ONE_DARK_THEME_JS)

            self.find_element(*c.SATCHEL_ONE_TIMETABLE_LOCATOR).screenshot(self.dark_image_path)
