import os
import sys
import tkinter
from tkinter import ttk, PhotoImage
from ARPtable import analyzeARPtable
from AudioForensics import run_audio_metadata_viewer
from GetChromeCookies import getChromeCookies
from GetChromeDownloads import getChromeDownloads
from GetChromeHistory import getChromeHistory
from ImageForensics import create_image_metadata_viewer
from LoadedDLLs import run_list_loaded_dlls_tool
from MalwarePersistance import malware_persistence_tool
from ProcessList import run_pslist_tool
from StaticGUIConfigs import positionWindow
from USBhistory import usb_history_analyzer_tool
from VideoForensics import create_video_metadata_viewer

# Determine the path to the directory containing the script
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Define the path to the images directory
images_dir = os.path.join(base_path, 'images')

# Modify the paths to the images
image_files = {
    "history": os.path.join(images_dir, "history.png"),
    "cookies": os.path.join(images_dir, "cookies.png"),
    "downloads": os.path.join(images_dir, "downloads.png"),
    "image": os.path.join(images_dir, "image.png"),
    "video": os.path.join(images_dir, "video.png"),
    "audio": os.path.join(images_dir, "audio.png"),
    "list": os.path.join(images_dir, "list.png"),
    "dll": os.path.join(images_dir, "dll.png"),
    "arp": os.path.join(images_dir, "arp.png"),
    "malware": os.path.join(images_dir, "malware.png"),
    "usb": os.path.join(images_dir, "usb.png")
}

# Main Window
mainWindow = tkinter.Tk()
mainWindow.title("Forensic-Xpert: Elite Computer Forensics Suite")
mainWindow.resizable(False, False)
mainWindow['background'] = '#333333'  # Dark grey background
positionWindow(mainWindow, width=1000, height=730)

# Title
titleText = tkinter.Label(
    mainWindow,
    text="Forensic-Xpert: Computer Forensics Suite",
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
homeText.pack(side="top")

# Define features for the Home Tab
home_features = [
    ("Get Browser History", "history", getChromeHistory),
    ("Get Browser Cookies", "cookies", getChromeCookies),
    ("Get Browser Downloads", "downloads", getChromeDownloads),
    ("Image Forensics", "image", create_image_metadata_viewer),
    ("Video Forensics", "video", create_video_metadata_viewer),
    ("Audio Forensics", "audio", run_audio_metadata_viewer),
    ("Get Process List", "list", run_pslist_tool),
    ("List Loaded DLLs", "dll", run_list_loaded_dlls_tool),
    ("Analyze ARP Table", "arp", analyzeARPtable),
    ("Check Malware Persistence", "malware", malware_persistence_tool),
    ("Get USB History", "usb", usb_history_analyzer_tool)
]

# Create a canvas to hold the buttons and scrollbar
canvas = tkinter.Canvas(tabs[0], bg="#333333", highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

# Create a frame inside the canvas to contain the buttons
frame = tkinter.Frame(canvas, bg="#333333")
canvas.create_window((0, 0), window=frame, anchor="nw")

# Create a vertical scrollbar for the canvas
scrollbar = ttk.Scrollbar(tabs[0], orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Display features on the Home Tab
buttons = []
button_images = []  # to keep references to PhotoImage objects
for i, (feature, image_icon, callback) in enumerate(home_features):
    # Load image
    image_icon = PhotoImage(file=image_files[image_icon]).subsample(5, 5)
    button_images.append(image_icon)
    # Create button
    button = tkinter.Button(
        frame,  # Home Tab frame
        text=feature,
        image=image_icon,
        compound=tkinter.TOP,  # Place the image on top of the text
        bg="#666666",  # Dark grey background
        fg="#ffffff",  # White text
        pady=10,
        padx=50,
        font=("Roboto", 12),  # Roboto font
        command=lambda cb=callback: cb(mainWindow)  # Pass callback function
    )
    buttons.append(button)
    # Position button
    button.grid(row=i // 3, column=i % 3, padx=20, pady=20)

# Update scroll region when the frame size changes
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Function to update the canvas scrolling region
def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


# Bind the frame's update function to canvas size change
frame.bind("<Configure>", update_scroll_region)


# Function to handle mouse wheel scrolling
def on_mousewheel(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")


# Bind the canvas to the mouse wheel event
canvas.bind("<MouseWheel>", on_mousewheel)


# -------------------------------- Browser Forensics Tab -------------------------------- #

# Get Browser History
def on_get_history_button_click():
    getChromeHistory(mainWindow)


get_history_icon = PhotoImage(file=image_files["history"])  # Add the path to your icon image
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


get_cookies_icon = PhotoImage(file=image_files["cookies"])  # Add the path to your icon image
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


get_downloads_icon = PhotoImage(file=image_files["downloads"])  # Add the path to your icon image
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


image_icon = PhotoImage(file=image_files["image"])  # Add the path to your icon image
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


video_icon = PhotoImage(file=image_files["video"])  # Add the path to your icon image
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


audio_icon = PhotoImage(file=image_files["audio"])  # Add the path to your icon image
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


get_pslist_icon = PhotoImage(file=image_files["list"])  # Add the path to your icon image
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


get_loaded_dlls_icon = PhotoImage(file=image_files["dll"])  # Add the path to your icon image
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


analyze_arp_table_icon = PhotoImage(file=image_files["arp"])  # Add the path to your icon image
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


malware_persistence_icon = PhotoImage(file=image_files["malware"])  # Add the path to your icon image
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


usb_history_icon = PhotoImage(file=image_files["usb"])  # Add the path to your icon image
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
