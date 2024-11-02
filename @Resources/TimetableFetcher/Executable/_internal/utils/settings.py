from configparser import RawConfigParser, NoSectionError, NoOptionError

import selenium_timetable.constants as c

DEFAULT_SETTINGS: dict[str, dict[str, str | int | float | bool]] = c.DEFAULT_SETTINGS

class InvalidSettingsError(Exception):
    pass

def init_config(settings_path: str) -> RawConfigParser:
    config = RawConfigParser()
    files = config.read(settings_path)

    if not files:
        make_default_settings_file(settings_path, DEFAULT_SETTINGS)

        print("Settings file not found. A new settings file with the default settings has been created.")
    
        config.read(settings_path)

    return config

def get_setting(settings_path: str, section: str, name: str, integer: bool=False, floatp: bool=False, boolean: bool=False) -> str | int | float | bool:
    config = init_config(settings_path)

    c_kwargs = {"section": section, "option": name}

    try:
        if integer:
            return config.getint(**c_kwargs)
        if floatp:
            return config.getfloat(**c_kwargs)
        if boolean:
            return config.getboolean(**c_kwargs)

        return config.get(**c_kwargs)
    except (NoSectionError, NoOptionError) as e:
        raise InvalidSettingsError(f"'{name}' setting not found. Please check and save your settings.") from e
    except ValueError as e:
        raise InvalidSettingsError(f"'{name}' setting is not valid. Please check and save your settings.") from e

def edit_setting(settings_path: str, section: str, name: str, value: str | int | float | bool) -> None:
    config = init_config(settings_path)

    config.set(section, name, value)

    with open(settings_path, "w", encoding="utf-8") as file:
        config.write(file)

def delete_setting(settings_path: str, section: str, name: str) -> None:
    config = init_config(settings_path)
    
    config.remove_option(section, name)

    with open(settings_path, "w", encoding="utf-8") as file:
        config.write(file)

def make_default_settings_file(settings_path:str, settings: dict[str, dict[str, str | int | float | bool]]) -> None:
    config = RawConfigParser()

    for section, section_settings in settings.items():
        config[section] = section_settings

    with open(settings_path, "w", encoding="utf-8") as file:
        config.write(file)