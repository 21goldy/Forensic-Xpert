import tkinter
from tkinter import ttk
from StaticGUIConfigs import *
from GetChromeHistory import getChromeHistory
from GetChromeCookies import getChromeCookies
from GetChromeDownloads import getChromeDownloads
from ImageForensics import create_image_metadata_viewer
from VideoForensics import create_video_metadata_viewer
from AudioForensics import run_audio_metadata_viewer
from ProcessList import run_pslist_tool
from LoadedDLLs import run_list_loaded_dlls_tool
from ARPtable import analyzeARPtable
from MalwarePersistance import malware_persistence_tool
from USBhistory import usb_history_analyzer_tool

# Main Window

mainWindow = tkinter.Tk() # Initialize mainWindow object
mainWindow.title("ForensicXpert: Elite Computer Forensics Suite") # Give a title to the mainWindow
mainWindow.resizable(False, False) # Disallow resizing of the mainWindow
mainWindow['background']=bgColor # Set backgound color
positionWindow(mainWindow, width=1000, height=730) # Stick the window at the top edge of screen

titleText = tkinter.Label(
    mainWindow,
    text="ForensicXpert: Computer Forensics Suite",
    bg="#fdf2d2",
    fg="black",
    pady=20,
    font=("Arial Rounded MT Bold", 17))
titleText.pack(side="top", fill="x")


# TAB MENUs
tabStyle = ttk.Style()
tabStyle.theme_create("CustomStyle", parent="alt", settings={
    "TFrame": {"configure": {"background": bgColor}},
    "TNotebook": {"configure": {"background": "#d5e6f6", "tabmargins": [70, 30, 0, 30]}}, # Tab Background
    "TNotebook.Tab": {"configure": {"background": "#ffffff", "padding": [20, 20], "font": ("Consolas", 12, "bold"), "borderwidth": 2}}, # Tab menu config
    })
tabStyle.theme_use("CustomStyle")

notebook = ttk.Notebook(mainWindow, style="TNotebook")
homeTab = ttk.Frame(notebook)
notebook.add(homeTab, text="Home")
browserTab = ttk.Frame(notebook)
notebook.add(browserTab, text="Browser Forensics")
mediaForensicsTab = ttk.Frame(notebook)
notebook.add(mediaForensicsTab, text="Media Forensics")
memoryForensicsTab = ttk.Frame(notebook)
notebook.add(memoryForensicsTab, text="Memory Forensics")
registryForensicsTab = ttk.Frame(notebook)
notebook.add(registryForensicsTab, text="Registry Forensics")
notebook.pack(expand=True, fill="both")



# Home Tab
homeText = tkinter.Label(
    homeTab,
    text="Welcome to ForensicXpert: Elite Computer Forensics Suite",
    bg=bgColor,
    pady=10,
    font=("Arial Rounded MT Bold", 20))
homeText.place(x=leftMargin+85, y=0)

featureText = tkinter.Label(
    homeTab,
    text="Features:",
    bg=bgColor,
    pady=10,
    font=("Arial Rounded MT Bold", 20))
featureText.place(x=leftMargin+85, y=50)

featureListText = tkinter.Label(
    homeTab,
    text=
    '''
1. Browser Forensics:
    Get Browser History
    Get Browser Cookies
    Get Browser Downloads''',
    bg=bgColor,
    pady=10,
    font=("Consolas", 12))
featureListText.place(x=leftMargin+95, y=90)

featureListText2 = tkinter.Label(
    homeTab,
    text=
    '''
2. Multimedia Forensics:
    Image Forensics
    Video Forensics
    Audio Forensics''',
    bg=bgColor,
    pady=10,
    font=("Consolas", 12))
featureListText2.place(x=leftMargin+500, y=90)

featureListText3 = tkinter.Label(
    homeTab,
    text=
    '''
3. Memory Forensics:
    Get Process List
    List Loaded DLLs
    Analyze ARP Table''',
    bg=bgColor,
    pady=10,
    font=("Consolas", 12))
featureListText3.place(x=leftMargin+110, y=225)

featureListText4 = tkinter.Label(
    homeTab,
    text=
    '''
4. Registry Forensics:
    Check Malware Persistance
    Get USB History''',
    bg=bgColor,
    pady=10,
    font=("Consolas", 12))
featureListText4.place(x=leftMargin+500, y=225)


# Browser Forensics Tab
WebForensicsText = tkinter.Label(
    browserTab,
    text="Welcome to the Web Browser Forensics Toolkit",
    bg=bgColor,
    pady=10,
    font=("Consolas", 14, "italic"))
WebForensicsText.place(x=leftMargin, y=0)

def on_get_history_button_click():
    getChromeHistory(mainWindow)
getHistoryButton = tkinter.Button(
    browserTab,
    command=on_get_history_button_click,
    text="Get Browser History",
    bg=browserToolsBG,
    pady=70,
    padx=browserToolsPadX,
    font=browserToolsFont)
getHistoryButton.place(x=leftMargin, y=100)

def on_get_cookies_button_click():
    getChromeCookies(mainWindow)
getCookiesButton = tkinter.Button(
    browserTab,
    command=on_get_cookies_button_click,
    text="Get Browser Cookies",
    bg=browserToolsBG,
    pady=70,
    padx=browserToolsPadX,
    font=browserToolsFont)
getCookiesButton.place(x=leftMargin+370, y=100)

def on_get_downloads_button_click():
    getChromeDownloads(mainWindow)
getDownloadsButton = tkinter.Button(
    browserTab,
    command=on_get_downloads_button_click,
    text="Get Browser Downloads",
    bg=browserToolsBG,
    pady=70,
    padx=browserToolsPadX,
    font=browserToolsFont)
getDownloadsButton.place(x=leftMargin+740, y=100)


# Media Forensics Tab

mediaForensicsText = tkinter.Label(
    mediaForensicsTab,
    text="Welcome to the Media Forensics Toolkit",
    bg=bgColor,
    pady=10,
    font=("Consolas", 14, "italic"))
mediaForensicsText.place(x=leftMargin, y=0)

# Image file forensics
def on_get_image_metadata_button_click():
    create_image_metadata_viewer(mainWindow)
imageForensicsButton = tkinter.Button(
    mediaForensicsTab,
    command=on_get_image_metadata_button_click,
    text="Image Forensics Tool",
    bg=browserToolsBG,
    pady=70,
    padx=browserToolsPadX,
    font=browserToolsFont)
imageForensicsButton.place(x=leftMargin, y=100)

# Video file forensics
def on_get_video_metadata_button_click():
    create_video_metadata_viewer(mainWindow)
videoForensicsButton = tkinter.Button(
    mediaForensicsTab,
    command=on_get_video_metadata_button_click,
    text="Video Forensics Tool",
    bg=browserToolsBG,
    pady=70,
    padx=browserToolsPadX,
    font=browserToolsFont)
videoForensicsButton.place(x=leftMargin+380, y=100)

# Audio file forensics
def on_get_audio_metadata_button_click():
    run_audio_metadata_viewer(mainWindow)
audioForensicsButton = tkinter.Button(
    mediaForensicsTab,
    command=on_get_audio_metadata_button_click,
    text="Audio Forensics Tool",
    bg=browserToolsBG,
    pady=70,
    padx=browserToolsPadX,
    font=browserToolsFont)
audioForensicsButton.place(x=leftMargin+750, y=100)


# Memory Forensics Tab

MemoryForensicsText = tkinter.Label(
    memoryForensicsTab,
    text="Welcome to the Memory Forensics Toolkit",
    bg=bgColor,
    pady=10,
    font=("Consolas", 14, "italic"))
MemoryForensicsText.place(x=leftMargin, y=0)

# List Process List
def on_get_pslist_button_click():
    run_pslist_tool(mainWindow)
getPSlistButton = tkinter.Button(
    memoryForensicsTab,
    command=on_get_pslist_button_click,
    text="Get Process List",
    bg=browserToolsBG,
    pady=70,
    padx=browserToolsPadX,
    font=browserToolsFont)
getPSlistButton.place(x=leftMargin, y=100)

# List Loaded DLLs
def on_get_loaded_dlls_button_click():
    run_list_loaded_dlls_tool(mainWindow)
listLoadedDLLsButton = tkinter.Button(
    memoryForensicsTab,
    command=on_get_loaded_dlls_button_click,
    text="List Loaded DLLs",
    bg=browserToolsBG,
    pady=70,
    padx=browserToolsPadX+10,
    font=browserToolsFont)
listLoadedDLLsButton.place(x=leftMargin+380, y=100)

# Analyze ARP Table
def on_analyze_arp_table_button_click():
    analyzeARPtable(mainWindow)
analyzeARPtableButton = tkinter.Button(
    memoryForensicsTab,
    command=on_analyze_arp_table_button_click,
    text="Analyze ARP Table",
    bg=browserToolsBG,
    pady=70,
    padx=browserToolsPadX,
    font=browserToolsFont)
analyzeARPtableButton.place(x=leftMargin+750, y=100)


# Registry Forensics Tab

RegistryForensicsText = tkinter.Label(
    registryForensicsTab,
    text="Welcome to the Registry Forensics Toolkit",
    bg=bgColor,
    pady=10,
    font=("Consolas", 14, "italic"))
RegistryForensicsText.place(x=leftMargin, y=0)

# Malware Persistance
def on_get_malware_presistance_button_click():
    malware_persistence_tool(mainWindow)
checkMalwarePersistanceButton = tkinter.Button(
    registryForensicsTab,
    command=on_get_malware_presistance_button_click,
    text="Check Malware Persistance",
    bg=browserToolsBG,
    pady=70,
    padx=browserToolsPadX,
    font=browserToolsFont)
checkMalwarePersistanceButton.place(x=leftMargin, y=100)

# Get USB History
def on_get_usb_history_button_click():
    usb_history_analyzer_tool(mainWindow)
getUSBhistoryButton = tkinter.Button(
    registryForensicsTab,
    command=on_get_usb_history_button_click,
    text="USB History",
    bg=browserToolsBG,
    pady=70,
    padx=browserToolsPadX+10,
    font=browserToolsFont)
getUSBhistoryButton.place(x=leftMargin+380, y=100)

mainWindow.mainloop()