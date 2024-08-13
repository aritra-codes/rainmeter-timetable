function Initialize()
    for i, setting in ipairs({"School", "Username", "Password"}) do
        if SKIN:GetVariable(setting) == "" then
            SKIN:Bang("!SetVariable", setting, string.format("#%sPlaceholder#", setting))
        end
    end
end

function UpdateSetting(setting, value)
    if value == "" then
        value = string.format("#%sPlaceholder#", setting)
    end

    SKIN:Bang("!SetVariable", setting, value)
    SKIN:Bang("!WriteKeyValue", "Variables", setting, value, "#UserSettings#")
end