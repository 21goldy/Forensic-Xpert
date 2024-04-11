bgColor = "#f9e6d8"
pinkColor = "#FF014E"
greenColor = "#07C123"
leftMargin = 20

def positionWindow(window, width, height): # Stick the window at the top edge of screen 
    screen_width = window.winfo_screenwidth()
    x_position = (screen_width - width) // 2
    y_position = 0
    window.geometry(f"{width}x{height}+{x_position}+{y_position}")


# Browser Forensics
browserToolsBG = "lightblue"
browserToolsPadX = 5
browserToolsFont = ("Consolas", 12, "italic")