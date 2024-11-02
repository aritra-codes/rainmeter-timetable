from functools import partial

import selenium_timetable.constants as c
import selenium_timetable.helpers as h
import utils.settings as s

def main(settings_path: str, timestamp: int, light_image_path: str="", dark_image_path: str=""):
    get_setting = partial(s.get_setting, settings_path)
    settings = {"school": get_setting(*c.SCHOOL_SETTING_LOCATOR),
                "username": get_setting(*c.USERNAME_SETTING_LOCATOR),
                "password": get_setting(*c.PASSWORD_SETTING_LOCATOR)}

    driver = h.TimetableDriver(settings, timestamp, light_image_path, dark_image_path)

    try:
        match get_setting(*c.SERVICE_SETTING_LOCATOR):
            case "Bromcom":
                driver.screenshot_bromcom()
            case "Satchel One":
                driver.screenshot_satchel_one()
    finally:
        driver.quit()
