function Initialize()
    if SKIN:GetVariable("School") == "" then
        SKIN:Bang("!SetOption", "SchoolLabel", "Text", "#SchoolPlaceholder#")
    end
    if SKIN:GetVariable("Username") == "" then
        SKIN:Bang("!SetOption", "UsernameLabel", "Text", "#UsernamePlaceholder#")
    end
    if SKIN:GetVariable("Password") == "" then
        SKIN:Bang("!SetOption", "PasswordLabel", "Text", "#PasswordPlaceholder#")
    end
end