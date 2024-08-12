function Initialize()
     ReadTime()
end

function ValidifyPath(path)
    local parts = {}

    -- Split the path by backslashes
    for part in string.gmatch(path, "[^\\]+") do
        -- If the part contains a space, encapsulate it with double quotes
        if string.match(part, "%s") then
            part = '"' .. part .. '"'
        end

        table.insert(parts, part)
    end

    -- Rejoin the parts with backslashes
    return table.concat(parts, "\\")
end

function FetchTimetable()
    -- Executable version
    ---[[
    return os.execute(string.format('%s "%s" -tl "%s" -td "%s" -d "%s"',
                                    ValidifyPath(SKIN:GetVariable("TimetableFetcher")),
                                    SKIN:GetVariable("UserSettings"),
                                    SKIN:GetVariable("TimetableImageLight"),
                                    SKIN:GetVariable("TimetableImageDark"),
                                    os.date("%Y-%m-%d", Time)))
    --]]

    -- Python version
    --[[
    return os.execute(string.format('python "%s" "%s" -tl "%s" -td "%s" -d "%s"',
                                    SKIN:GetVariable("TimetableFetcher"),
                                    SKIN:GetVariable("UserSettings"),
                                    SKIN:GetVariable("TimetableImageLight"),
                                    SKIN:GetVariable("TimetableImageDark"),
                                    os.date("%Y-%m-%d", Time)))
    --]]
end

function Notify(title, message)
    -- Executable version
    ---[[
    return os.execute(string.format('%s "%s" "%s"',
                                    ValidifyPath(SKIN:GetVariable("Notifier")),
                                    title,
                                    message))
    --]]

    -- Python version
    --[[
    return os.execute(string.format('python "%s" "%s" "%s"',
                                    SKIN:GetVariable("Notifier"),
                                    title,
                                    message))
    --]]
end

function ReadTime()
    Time = tonumber(SKIN:GetVariable("Time"))
end

function DisplayDate()
    if Time then
        -- Subtracting 1 converts start of week from Sun to Mon
        local currentDayOfWeek = tonumber(os.date("%w", Time)) - 1

        local startOfWeek = Time - (currentDayOfWeek * (24 * 60 * 60))
        local endOfWeek = Time + ((6 - currentDayOfWeek) * (24 * 60 * 60))

        Date = string.format("%s - %s", os.date("%d %b", startOfWeek), os.date("%d %b", endOfWeek))
    else
        Date = "N/A"
    end

    SKIN:Bang("!SetOption", "Date", "Text", Date)
end

function SetToday()
    Time = os.time()

    IncrementTime(0)
end

function IncrementTime(increment)
    if tonumber(Time) then
        Time = Time + increment

        SKIN:Bang("!SetVariable", "TimetableImage", "")
        SKIN:Bang("!SetOption", "Date", "Text", "Loading...")
        SKIN:Bang("!UpdateMeter", "TimetableImage")
        SKIN:Bang("!UpdateMeter", "Date")
        SKIN:Bang("!Redraw")

        if FetchTimetable() == 0 then
            SKIN:Bang("!WriteKeyValue", "Variables", "Time", Time, "#UserSettings#")
        else
            ReadTime()

            Notify("Error", "Please make sure you have saved the correct settings and are connected to the Internet.")
        end

        DisplayDate()
    end
end