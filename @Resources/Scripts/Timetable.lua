function Initialize()
    ReadTime()
    DisplayDate()
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
    return os.execute(string.format('%s "%s" "%s" -lp "%s" -dp "%s"',
                                    ValidifyPath(SKIN:GetVariable("TimetableFetcherExe")),
                                    SKIN:GetVariable("UserSettings"),
                                    Time,
                                    SKIN:GetVariable("TimetableImageLight"),
                                    SKIN:GetVariable("TimetableImageDark")))
    --]]

    -- Python version
    --[[
    return os.execute(string.format('python "%s" "%s" "%s" -lp "%s" -dp "%s"',
                                    SKIN:GetVariable("TimetableFetcherPython"),
                                    SKIN:GetVariable("UserSettings"),
                                    Time,
                                    SKIN:GetVariable("TimetableImageLight"),
                                    SKIN:GetVariable("TimetableImageDark")))
    --]]
end

function Notify(title, message)
    -- Executable version
    ---[[
    return os.execute(string.format('%s "%s" "%s"',
                                    ValidifyPath(SKIN:GetVariable("NotifierExe")),
                                    title,
                                    message))
    --]]

    -- Python version
    --[[
    return os.execute(string.format('python "%s" "%s" "%s"',
                                    SKIN:GetVariable("NotifierPython"),
                                    title,
                                    message))
    --]]
end

function SetTimeAsStartOfWeek(time)
    local currentDayOfWeek = tonumber(os.date("%w", time)) - 1 -- Subtracting 1 converts start of week from Sun to Mon
    Time = time - (currentDayOfWeek * (24 * 60 * 60))
end

function ReadTime()
    local time = tonumber(SKIN:GetVariable("Time"))

    if time then
        SetTimeAsStartOfWeek(time)
    end
end

function DisplayDate()
    if Time then
        Date = string.format("%s - %s", os.date("%d %b", Time), os.date("%d %b", Time + (6 * 24 * 60 * 60)))
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
    if Time then
        SetTimeAsStartOfWeek(Time + increment)

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

