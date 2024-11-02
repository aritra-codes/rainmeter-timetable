from selenium.webdriver.common.by import By

TIMEOUT = 10

# Bromcom
BROMCOM_STUDENT_LOGIN_URL = "https://www.bromcomvle.com/auth/login"
BROMCOM_TIMETABLE_URL = "https://www.bromcomvle.com/Timetable"

BROMCOM_SCHOOL_INPUT_LOCATOR = (By.ID, "schoolid")
BROMCOM_USERNAME_INPUT_LOCATOR = (By.ID, "username")
BROMCOM_PASSWORD_INPUT_LOCATOR = (By.ID, "password")
BROMCOM_LOGIN_BUTTON_LOCATOR = (By.ID, "LoginButton")
BROMCOM_LOADED_INDICATOR_LOCATOR = (By.ID, "SchoolNameLabel")
BROMCOM_TIMETABLE_LOCATOR = (By.ID, "Timetable")

def BROMCOM_SET_DATE_JS(date: str=""):
    return f"""
var Type = $("#TimetableType").val();
var Id = $("#EntityID").val();

loadStudentTimetable('{date}', Type, Id);
"""
BROMCOM_DARK_THEME_JS = """
document.querySelectorAll('#Timetable th').forEach((th) => {
    th.style.setProperty('color', 'white', 'important')
    th.style.setProperty('background-color', 'black', 'important')
    th.style.setProperty('border-color', 'white', 'important')
});
document.querySelectorAll('#Timetable td').forEach((td) => {
    td.style.setProperty('color', 'white', 'important')
    td.style.setProperty('background-color', 'black', 'important')
});
"""

# Satchel One
SATCHEL_ONE_STUDENT_LOGIN_URL = "https://www.satchelone.com/login?userType=student"
def SATCHEL_ONE_TIMETABLE_URL(date: str="") -> str:
    return f"https://www.satchelone.com/timetable{f'?date={date}' if date else ''}"

SATCHEL_ONE_SCHOOL_SEARCH_INPUT_LOCATOR = (By.ID, "school-selector-search-box")
SATCHEL_ONE_SUGGESTED_SCHOOL_NAME_OPTION_LOCATOR = (By.CLASS_NAME, "suggested-school-name")
SATCHEL_ONE_USERNAME_INPUT_LOCATOR = (By.ID, "identification")
SATCHEL_ONE_PASSWORD_INPUT_LOCATOR = (By.ID, "password")
SATCHEL_ONE_DECLINE_COOKIES_BUTTON_LOCATOR = (By.ID, "onetrust-reject-all-handler")
SATCHEL_ONE_LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Log in']")
SATCHEL_ONE_TIMETABLE_LOCATOR = (By.CLASS_NAME, "timetable")

SATCHEL_ONE_TOP_BAR_SELECTOR = ".satchel-top-bar"
SATCHEL_ONE_TIMELINE_SELECTOR = ".time-line"
SATCHEL_ONE_TIMETABLE_HEADER_SELECTOR = ".timetable--headers--item"

SATCHEL_ONE_REMOVE_UNNECESSARY_ELEMENTS_JS = f"""
document.querySelector('{SATCHEL_ONE_TOP_BAR_SELECTOR}').remove();
document.querySelectorAll('{SATCHEL_ONE_TIMELINE_SELECTOR}').forEach((timeline) => {{
    timeline.remove();
}});
"""
SATCHEL_ONE_DARK_THEME_STYLE = "background-color: #000000; color: #ffffff;"
SATCHEL_ONE_DARK_THEME_JS = f"""
document.querySelector('.{SATCHEL_ONE_TIMETABLE_LOCATOR[1]}').style = '{SATCHEL_ONE_DARK_THEME_STYLE}';
document.querySelectorAll('{SATCHEL_ONE_TIMETABLE_HEADER_SELECTOR}').forEach((header) => {{
    header.style = '{SATCHEL_ONE_DARK_THEME_STYLE}';
}});
"""

# Settings
VARIABLES_SETTING_SECTION = "Variables"
THEME_SETTING_LOCATOR = (VARIABLES_SETTING_SECTION, "Theme")
TITLE_SETTING_LOCATOR = (VARIABLES_SETTING_SECTION, "Title")
SERVICE_SETTING_LOCATOR = (VARIABLES_SETTING_SECTION, "Service")
TIME_SETTING_LOCATOR = (VARIABLES_SETTING_SECTION, "Time")
SCHOOL_SETTING_LOCATOR = (VARIABLES_SETTING_SECTION, "School")
USERNAME_SETTING_LOCATOR = (VARIABLES_SETTING_SECTION, "Username")
PASSWORD_SETTING_LOCATOR = (VARIABLES_SETTING_SECTION, "Password")

DEFAULT_SETTINGS = {
    VARIABLES_SETTING_SECTION: {
        THEME_SETTING_LOCATOR[1]: "Dark",
        TITLE_SETTING_LOCATOR[1]: "Timetable",
        SERVICE_SETTING_LOCATOR[1]: "",
        TIME_SETTING_LOCATOR[1]: "",
        SCHOOL_SETTING_LOCATOR[1]: "",
        USERNAME_SETTING_LOCATOR[1]: "",
        PASSWORD_SETTING_LOCATOR[1]: ""
    }
}
