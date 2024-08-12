from functools import partial

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import selenium_satchel_one.constants as c
import utils.settings as s

def main(settings_path: str, timetable_light_image_path: str="", timetable_dark_image_path: str="", date: str=""):
    get_setting = partial(s.get_setting, settings_path)

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)

    try:
        driver.get(c.SATCHEL_ONE_STUDENT_LOGIN_URL)

        WebDriverWait(driver, c.TIMEOUT).until(EC.visibility_of_element_located(c.SCHOOL_SEARCH_INPUT_LOCATOR))
        driver.find_element(*c.SCHOOL_SEARCH_INPUT_LOCATOR).send_keys(get_setting(*c.SCHOOL_SETTING_LOCATOR))

        WebDriverWait(driver, c.TIMEOUT).until(EC.visibility_of_element_located(c.SUGGESTED_SCHOOL_NAME_OPTION_LOCATOR))
        driver.find_element(*c.SUGGESTED_SCHOOL_NAME_OPTION_LOCATOR).click()

        driver.find_element(*c.USERNAME_INPUT_LOCATOR).send_keys(get_setting(*c.USERNAME_SETTING_LOCATOR))

        driver.find_element(*c.PASSWORD_INPUT_LOCATOR).send_keys(get_setting(*c.PASSWORD_SETTING_LOCATOR))

        driver.find_element(*c.DECLINE_COOKIES_BUTTON_LOCATOR).click()

        driver.find_element(*c.LOGIN_BUTTON_LOCATOR).click()

        driver.get(c.SATCHEL_ONE_TIMETABLE_URL(date))

        WebDriverWait(driver, c.TIMEOUT).until(EC.visibility_of_element_located(c.TIMETABLE_LOCATOR))

        # Removes unnecessary elements that appear in the screenshot
        driver.execute_script(c.REMOVE_UNNECESSARY_ELEMENTS_JS)

        if timetable_light_image_path:
            driver.find_element(*c.TIMETABLE_LOCATOR).screenshot(timetable_light_image_path)

        if timetable_dark_image_path:
            # Takes a screenshot with dark theme
            driver.execute_script(c.DARK_THEME_JS)

            driver.find_element(*c.TIMETABLE_LOCATOR).screenshot(timetable_dark_image_path)
    finally:
        driver.quit()
