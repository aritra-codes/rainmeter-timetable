function Initialize()
    Theme = SKIN:GetVariable("Theme")

    ApplyTheme()
end

function FileExists(path)
    local f = io.open(path, "r")
    return f ~= nil and io.close(f)
end

function WriteVariable(key, value)
    SKIN:Bang("!SetVariable", key, value)

    SKIN:Bang("!WriteKeyValue", "Variables", key, value, "#GlobalVariables#")
end

function ApplyTheme()
    if Theme == "light" then
        TimetableImage = SKIN:GetVariable("TimetableImageLight")
        PrimaryColor = "#PrimaryColorLight#"
        SecondaryColor = "#SecondaryColorLight#"
        FontColor = "#FontColorDark#"
        NextIcon = "#NextIconDark#"
        SettingsIcon= "#SettingsIconDark#"
        RefreshIcon = "#RefreshIconDark#"
        FitIcon = "#FitIconDark#"
        ThemeIcon = "#ThemeIconLight#"
        ReturnIcon = "#ReturnIconDark#"
    else
        TimetableImage = SKIN:GetVariable("TimetableImageDark")
        PrimaryColor = "#PrimaryColorDark#"
        SecondaryColor = "#SecondaryColorDark#"
        FontColor = "#FontColorLight#"
        NextIcon = "#NextIconLight#"
        SettingsIcon= "#SettingsIconLight#"
        RefreshIcon = "#RefreshIconLight#"
        FitIcon = "#FitIconLight#"
        ThemeIcon = "#ThemeIconDark#"
        ReturnIcon = "#ReturnIconLight#"
    end

    if not FileExists(TimetableImage) then
        TimetableImage = ""
    end

    WriteVariable("TimetableImage", TimetableImage)
    WriteVariable("PrimaryColor", PrimaryColor)
    WriteVariable("SecondaryColor", SecondaryColor)
    WriteVariable("FontColor", FontColor)
    WriteVariable("NextIcon", NextIcon)
    WriteVariable("SettingsIcon", SettingsIcon)
    WriteVariable("RefreshIcon", RefreshIcon)
    WriteVariable("FitIcon", FitIcon)
    WriteVariable("ThemeIcon", ThemeIcon)
    WriteVariable("ReturnIcon", ReturnIcon)

    if SKIN:GetVariable("CURRENTFILE") == SKIN:GetVariable("TimetableSkin") and TimetableImage ~= "" then
        -- ImageMeasures are disabled by default to avoid errors, here they are enabled
        SKIN:Bang("!SetOption", "MeasureImageWidth", "Disabled", 0)
        SKIN:Bang("!SetOption", "MeasureImageHeight", "Disabled", 0)

        SKIN:Bang("!UpdateMeasure", "MeasureImageWidth")
        SKIN:Bang("!UpdateMeasure", "MeasureImageHeight")
    end
end

function ToggleTheme()
    if Theme == "dark" then
        Theme = "light"
    else
        Theme = "dark"
    end

    ApplyTheme()

    SKIN:Bang("!WriteKeyValue", "Variables", "Theme", Theme, "#UserSettings#")
end