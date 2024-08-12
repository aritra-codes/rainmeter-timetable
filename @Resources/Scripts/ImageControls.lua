function Initialize()
    IsDragging = false
    StartX, StartY = 0, 0
    OffsetX = tonumber(SKIN:GetVariable("OffsetX"))
    OffsetY = tonumber(SKIN:GetVariable("OffsetY"))

    ZoomFactor = tonumber(SKIN:GetVariable("ZoomFactor"))
end

function Update()
    if IsDragging then
        local currentX = SKIN:GetMeasure("MeasureMouseX"):GetValue()
        local currentY = SKIN:GetMeasure("MeasureMouseY"):GetValue()

        local newOffsetX = OffsetX - (currentX - StartX)
        local newOffsetY = OffsetY - (currentY - StartY)

        Drag(newOffsetX, newOffsetY)

        StartX, StartY = currentX, currentY
    end
end

function StartDrag()
    IsDragging = true

    StartX = SKIN:GetMeasure("MeasureMouseX"):GetValue()
    StartY = SKIN:GetMeasure("MeasureMouseY"):GetValue()
end

function StopDrag()
    IsDragging = false
end

function Drag(newOffsetX, newOffsetY)
    local imageWidth =  SKIN:GetMeasure("MeasureImageWidth"):GetValue()
    local imageHeight =  SKIN:GetMeasure("MeasureImageHeight"):GetValue()

    -- Prevents over-cropping to the right
    if newOffsetX > 0 then
        -- Prevents over-cropping to the left
        if newOffsetX + ZoomFactor > imageWidth then
            OffsetX = imageWidth - ZoomFactor
        else
            OffsetX = newOffsetX
        end

        SKIN:Bang("!SetVariable", "OffsetX", OffsetX)
    end

    -- Prevents over-cropping to the bottom
    if newOffsetY > 0 then
        -- Prevents over-cropping to the top
        if newOffsetY + ZoomFactor > imageHeight then
            OffsetY = imageHeight - ZoomFactor
        else
            OffsetY = newOffsetY
        end

        SKIN:Bang("!SetVariable", "OffsetY", OffsetY)
    end
end

function Zoom(zoomIncrement)
    local newZoomFactor = ZoomFactor + zoomIncrement

    -- Prevents image from disappearing due to over-zooming
    if newZoomFactor > 0 then
        local imageWidth =  SKIN:GetMeasure("MeasureImageWidth"):GetValue()
        local imageHeight =  SKIN:GetMeasure("MeasureImageHeight"):GetValue()

        -- Prevents image from becoming smaller than the meter
        if newZoomFactor > imageWidth or newZoomFactor > imageHeight then
            MinZoom()
        else
            ZoomFactor = newZoomFactor

            SKIN:Bang("!SetVariable", "ZoomFactor", ZoomFactor)

            Drag(OffsetX, OffsetY) -- Prevents over-cropping to the left and top
        end
    end
end

function MinZoom()
    local imageWidth =  SKIN:GetMeasure("MeasureImageWidth"):GetValue()
    local imageHeight =  SKIN:GetMeasure("MeasureImageHeight"):GetValue()

    if imageWidth < imageHeight then
        ZoomFactor = imageWidth
    else
        ZoomFactor = imageHeight
    end

    SKIN:Bang("!SetVariable", "ZoomFactor", ZoomFactor)

    Drag(OffsetX, OffsetY) -- Prevents over-cropping to the left and top
end
