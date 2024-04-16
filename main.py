import tkinter
from tkinter import ttk, PhotoImage

# Update imports with correct module names
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
mainWindow = tkinter.Tk()
mainWindow.title("ForensicXpert: Elite Computer Forensics Suite")
mainWindow.resizable(False, False)
mainWindow['background'] = '#333333'  # Dark grey background
positionWindow(mainWindow, width=1000, height=730)

# Title
titleText = tkinter.Label(
    mainWindow,
    text="ForensicXpert: Computer Forensics Suite",
    bg="#333333",  # Dark grey background
    fg="#ffffff",  # White text
    pady=20,
    font=("Roboto", 17))  # Roboto font
titleText.pack(side="top", fill="x")

# Tab Menus
tabStyle = ttk.Style()
tabStyle.theme_create("CustomStyle", parent="alt", settings={
    "TFrame": {"configure": {"background": "#333333"}},  # Dark grey background
    "TNotebook": {"configure": {"background": "#444444", "tabmargins": [70, 30, 0, 30]}},
    # Light grey background for tabs
    "TNotebook.Tab": {"configure": {"background": "#666666", "padding": [20, 20], "font": ("Roboto", 12, "bold"),
                                    "borderwidth": 2}},  # Dark grey tab background
})
tabStyle.theme_use("CustomStyle")

notebook = ttk.Notebook(mainWindow, style="TNotebook")
# Define tabs
tab_names = ["Home", "Browser Forensics", "Media Forensics", "Memory Forensics", "Registry Forensics"]
tabs = [ttk.Frame(notebook) for _ in tab_names]
# Add tabs to the notebook
for i, tab_name in enumerate(tab_names):
    notebook.add(tabs[i], text=tab_name)
notebook.pack(expand=True, fill="both")

# Home Tab
homeText = tkinter.Label(
    tabs[0],  # Home Tab
    text="Welcome to ForensicXpert: Elite Computer Forensics Suite",
    bg="#333333",  # Dark grey background
    fg="#ffffff",  # White text
    pady=10,
    font=("Roboto", 20))  # Roboto font
homeText.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

# Define features for the Home Tab
home_features = [
    "Get Browser History", "Get Browser Cookies", "Get Browser Downloads",
    "Image Forensics", "Video Forensics", "Audio Forensics",
    "Get Process List", "List Loaded DLLs", "Analyze ARP Table",
    "Check Malware Persistence", "Get USB History"
]

# Display features on the Home Tab
for i, feature in enumerate(home_features):
    featureLabel = tkinter.Label(
        tabs[0],  # Home Tab
        text=f"{i + 1}. {feature}",
        bg="#333333",  # Dark grey background
        fg="#ffffff",  # White text
        pady=5,
        font=("Roboto", 12))  # Roboto font
    featureLabel.place(relx=0.5, rely=0.25 + i * 0.05, anchor=tkinter.CENTER)


# -------------------------------- Browser Forensics Tab -------------------------------- #

# Get Browser History
def on_get_history_button_click():
    getChromeHistory(mainWindow)


get_history_icon = PhotoImage(file="images/history.png")  # Add the path to your icon image
get_history_icon = get_history_icon.subsample(5, 5)
getHistoryButton = tkinter.Button(
    tabs[1],  # Browser Forensics Tab
    command=on_get_history_button_click,
    text="Get Browser History",
    image=get_history_icon,
    compound=tkinter.TOP,  # Place the image on top of the text
    bg="#666666",  # Dark grey background
    fg="#ffffff",  # White text
    pady=10,
    padx=20,
    font=("Roboto", 12))  # Roboto font
getHistoryButton.grid(row=1, column=0, padx=(180, 10), pady=(150, 10), sticky="ew")


# Get Browser Cookies
def on_get_cookies_button_click():
    getChromeCookies(mainWindow)


get_cookies_icon = PhotoImage(file="images/cookies.png")  # Add the path to your icon image
get_cookies_icon = get_cookies_icon.subsample(5, 5)
getCookiesButton = tkinter.Button(
    tabs[1],  # Browser Forensics Tab
    command=on_get_cookies_button_click,
    text="Get Browser Cookies",
    image=get_cookies_icon,
    compound=tkinter.TOP,  # Place the image on top of the text
    bg="#666666",  # Dark grey background
    fg="#ffffff",  # White text
    pady=10,
    padx=20,
    font=("Roboto", 12))  # Roboto font
getCookiesButton.grid(row=1, column=1, padx=10, pady=(150, 10), sticky="ew")


# Get Browser Downloads
def on_get_downloads_button_click():
    getChromeDownloads(mainWindow)


get_downloads_icon = PhotoImage(file="images/downloads.png")  # Add the path to your icon image
get_downloads_icon = get_downloads_icon.subsample(5, 5)
getDownloadsButton = tkinter.Button(
    tabs[1],  # Browser Forensics Tab
    command=on_get_downloads_button_click,
    text="Get Browser Downloads",
    image=get_downloads_icon,
    compound=tkinter.TOP,  # Place the image on top of the text
    bg="#666666",  # Dark grey background
    fg="#ffffff",  # White text
    pady=10,
    padx=20,
    font=("Roboto", 12))  # Roboto font
getDownloadsButton.grid(row=1, column=2, padx=(10, 20), pady=(150, 10), sticky="ew")


# -------------------------------- Media Forensics Tab -------------------------------- #

# Image file forensics
def on_get_image_metadata_button_click():
    create_image_metadata_viewer(mainWindow)


image_icon = PhotoImage(file="images/image.png")  # Add the path to your icon image
image_icon = image_icon.subsample(5, 5)
imageForensicsButton = tkinter.Button(
    tabs[2],  # Media Forensics Tab
    command=on_get_image_metadata_button_click,
    text="Image Forensics Tool",
    image=image_icon,
    compound=tkinter.TOP,  # Place the image on top of the text
    bg="#666666",  # Dark grey background
    fg="#ffffff",  # White text
    pady=10,
    padx=20,
    font=("Roboto", 12))  # Roboto font
imageForensicsButton.grid(row=1, column=0, padx=(180, 10), pady=(150, 10), sticky="ew")


# Video file forensics
def on_get_video_metadata_button_click():
    create_video_metadata_viewer(mainWindow)


video_icon = PhotoImage(file="images/video.png")  # Add the path to your icon image
video_icon = video_icon.subsample(5, 5)
videoForensicsButton = tkinter.Button(
    tabs[2],  # Media Forensics Tab
    command=on_get_video_metadata_button_click,
    text="Video Forensics Tool",
    image=video_icon,
    compound=tkinter.TOP,  # Place the image on top of the text
    bg="#666666",  # Dark grey background
    fg="#ffffff",  # White text
    pady=10,
    padx=20,
    font=("Roboto", 12))  # Roboto font
videoForensicsButton.grid(row=1, column=1, padx=10, pady=(150, 10), sticky="ew")


# Audio file forensics
def on_get_audio_metadata_button_click():
    run_audio_metadata_viewer(mainWindow)


audio_icon = PhotoImage(file="images/audio.png")  # Add the path to your icon image
audio_icon = audio_icon.subsample(5, 5)
audioForensicsButton = tkinter.Button(
    tabs[2],  # Media Forensics Tab
    command=on_get_audio_metadata_button_click,
    text="Audio Forensics Tool",
    image=audio_icon,
    compound=tkinter.TOP,  # Place the image on top of the text
    bg="#666666",  # Dark grey background
    fg="#ffffff",  # White text
    pady=10,
    padx=20,
    font=("Roboto", 12))  # Roboto font
audioForensicsButton.grid(row=1, column=2, padx=(10, 20), pady=(150, 10), sticky="ew")


# -------------------------------- Memory Forensics Tab -------------------------------- #

# List Process List
def on_get_pslist_button_click():
    run_pslist_tool(mainWindow)


get_pslist_icon = PhotoImage(file="images/list.png")  # Add the path to your icon image
get_pslist_icon = get_pslist_icon.subsample(5, 5)
getPSlistButton = tkinter.Button(
    tabs[3],  # Memory Forensics Tab
    command=on_get_pslist_button_click,
    text="Get Process List",
    image=get_pslist_icon,
    compound=tkinter.TOP,  # Place the image on top of the text
    bg="#666666",  # Dark grey background
    fg="#ffffff",  # White text
    pady=10,
    padx=20,
    font=("Roboto", 12))  # Roboto font
getPSlistButton.grid(row=1, column=0, padx=(180, 10), pady=(150, 10), sticky="ew")


# List Loaded DLLs
def on_get_loaded_dlls_button_click():
    run_list_loaded_dlls_tool(mainWindow)


get_loaded_dlls_icon = PhotoImage(file="images/dll.png")  # Add the path to your icon image
get_loaded_dlls_icon = get_loaded_dlls_icon.subsample(5, 5)
listLoadedDLLsButton = tkinter.Button(
    tabs[3],  # Memory Forensics Tab
    command=on_get_loaded_dlls_button_click,
    text="List Loaded DLLs",
    image=get_loaded_dlls_icon,
    compound=tkinter.TOP,  # Place the image on top of the text
    bg="#666666",  # Dark grey background
    fg="#ffffff",  # White text
    pady=10,
    padx=20,
    font=("Roboto", 12))  # Roboto font
listLoadedDLLsButton.grid(row=1, column=1, padx=10, pady=(150, 10), sticky="ew")


# Analyze ARP Table
def on_analyze_arp_table_button_click():
    analyzeARPtable(mainWindow)


analyze_arp_table_icon = PhotoImage(file="images/arp.png")  # Add the path to your icon image
analyze_arp_table_icon = analyze_arp_table_icon.subsample(5, 5)
analyzeARPtableButton = tkinter.Button(
    tabs[3],  # Memory Forensics Tab
    command=on_analyze_arp_table_button_click,
    text="Analyze ARP Table",
    image=analyze_arp_table_icon,
    compound=tkinter.TOP,  # Place the image on top of the text
    bg="#666666",  # Dark grey background
    fg="#ffffff",  # White text
    pady=10,
    padx=20,
    font=("Roboto", 12))  # Roboto font
analyzeARPtableButton.grid(row=1, column=2, padx=(10, 20), pady=(150, 10), sticky="ew")


# -------------------------------- Registry Forensics Tab -------------------------------- #

# Malware Persistence
def on_get_malware_persistence_button_click():
    malware_persistence_tool(mainWindow)


malware_persistence_icon = PhotoImage(file="images/malware.png")  # Add the path to your icon image
malware_persistence_icon = malware_persistence_icon.subsample(5, 5)
malwarePersistenceButton = tkinter.Button(
    tabs[4],  # Registry Forensics Tab
    command=on_get_malware_persistence_button_click,
    text="Check Malware Persistence",
    image=malware_persistence_icon,
    compound=tkinter.TOP,  # Place the image on top of the text
    bg="#666666",  # Dark grey background
    fg="#ffffff",  # White text
    pady=10,
    padx=20,
    font=("Roboto", 12))  # Roboto font
malwarePersistenceButton.grid(row=1, column=0, padx=(280, 10), pady=150, sticky="ew")


# USB History
def on_get_usb_history_button_click():
    usb_history_analyzer_tool(mainWindow)


usb_history_icon = PhotoImage(file="images/usb.png")  # Add the path to your icon image
usb_history_icon = usb_history_icon.subsample(5, 5)
usbHistoryButton = tkinter.Button(
    tabs[4],  # Registry Forensics Tab
    command=on_get_usb_history_button_click,
    text="USB History",
    image=usb_history_icon,
    compound=tkinter.TOP,  # Place the image on top of the text
    bg="#666666",  # Dark grey background
    fg="#ffffff",  # White text
    pady=10,
    padx=20,
    font=("Roboto", 12))  # Roboto font
usbHistoryButton.grid(row=1, column=2, padx=(10, 20), pady=150, sticky="ew")

# Run the application
mainWindow.mainloop()
