from selenium.webdriver.common.by import By

TIMEOUT = 10

SATCHEL_ONE_STUDENT_LOGIN_URL = "https://www.satchelone.com/login?userType=student"
def SATCHEL_ONE_TIMETABLE_URL(date: str="") -> str:
    return f"https://www.satchelone.com/timetable{f'?date={date}' if date else ''}"

SCHOOL_SEARCH_INPUT_LOCATOR = (By.ID, "school-selector-search-box")
SUGGESTED_SCHOOL_NAME_OPTION_LOCATOR = (By.CLASS_NAME, "suggested-school-name")
USERNAME_INPUT_LOCATOR = (By.ID, "identification")
PASSWORD_INPUT_LOCATOR = (By.ID, "password")
DECLINE_COOKIES_BUTTON_LOCATOR = (By.ID, "onetrust-reject-all-handler")
LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Log in']")
TIMETABLE_LOCATOR = (By.CLASS_NAME, "timetable")

TOP_BAR_SELECTOR = ".satchel-top-bar"
TIMELINE_SELECTOR = ".time-line"
TIMETABLE_HEADER_SELECTOR = ".timetable--headers--item"

REMOVE_UNNECESSARY_ELEMENTS_JS = f"""
                                 document.querySelector('{TOP_BAR_SELECTOR}').remove();
                                 document.querySelectorAll('{TIMELINE_SELECTOR}').forEach((timeline) => {{
                                     timeline.remove();
                                 }});
                                 """
DARK_THEME_STYLE = "background-color: #000000; color: #ffffff;"
DARK_THEME_JS = f"""
                document.querySelector('.{TIMETABLE_LOCATOR[1]}').style = '{DARK_THEME_STYLE}';
                document.querySelectorAll('{TIMETABLE_HEADER_SELECTOR}').forEach((header) => {{
                header.style = '{DARK_THEME_STYLE}';
                }});
                """

# Settings
VARIABLES_SETTING_SECTION = "Variables"
THEME_SETTING_SECTION = (VARIABLES_SETTING_SECTION, "Theme")
TITLE_SETTING_SECTION = (VARIABLES_SETTING_SECTION, "Title")
TIME_SETTING_SECTION = (VARIABLES_SETTING_SECTION, "Time")
SCHOOL_SETTING_LOCATOR = (VARIABLES_SETTING_SECTION, "School")
USERNAME_SETTING_LOCATOR = (VARIABLES_SETTING_SECTION, "Username")
PASSWORD_SETTING_LOCATOR = (VARIABLES_SETTING_SECTION, "Password")

DEFAULT_SETTINGS = {
    VARIABLES_SETTING_SECTION: {
        THEME_SETTING_SECTION[1]: "dark",
        TITLE_SETTING_SECTION[1]: "Timetable",
        TIME_SETTING_SECTION[1]: "",
        SCHOOL_SETTING_LOCATOR[1]: "",
        USERNAME_SETTING_LOCATOR[1]: "",
        PASSWORD_SETTING_LOCATOR[1]: ""
    }
}
