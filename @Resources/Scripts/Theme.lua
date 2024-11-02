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
    TimetableImage = SKIN:GetVariable(string.format("TimetableImage%s", Theme))
    if not FileExists(TimetableImage) then
        TimetableImage = ""
    end
    WriteVariable("TimetableImage", TimetableImage)

    for i, variable in ipairs({"PrimaryColor", "SecondaryColor", "FontColor", "NextIcon", "SettingsIcon", "RefreshIcon", "FitIcon", "ThemeIcon", "ReturnIcon", "DropdownIcon"}) do
        WriteVariable(variable, string.format("#%s%s#", variable, Theme))
    end

    if SKIN:GetVariable("CURRENTFILE") == SKIN:GetVariable("TimetableSkin") and TimetableImage ~= "" then
        -- ImageMeasures are disabled by default to avoid errors, here they are enabled
        SKIN:Bang("!SetOption", "MeasureImageWidth", "Disabled", 0)
        SKIN:Bang("!SetOption", "MeasureImageHeight", "Disabled", 0)

        SKIN:Bang("!UpdateMeasure", "MeasureImageWidth")
        SKIN:Bang("!UpdateMeasure", "MeasureImageHeight")
    end
end

function ToggleTheme()
    Theme = Theme == "Light" and "Dark" or "Light"

    ApplyTheme()

    SKIN:Bang("!WriteKeyValue", "Variables", "Theme", Theme, "#UserSettings#")
end
