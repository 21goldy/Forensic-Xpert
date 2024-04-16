import sqlite3
import os
import platform
import shutil
import pandas as pd
import tkinter
from tkinter import ttk
from StaticGUIConfigs import *
from Components import CutPaste


def getChromeCookies(parent_window):  # Accept the parent window as an argument

    # Detect the operating system to find the Chrome cookies file location
    if platform.system() == 'Windows':
        cookies_file_path = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'Default', 'Network', 'Cookies')
    elif platform.system() == 'Darwin':  # macOS
        cookies_file_path = os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'Google', 'Chrome', 'Default', 'Cookies')
    elif platform.system() == 'Linux':
        cookies_file_path = os.path.join(os.path.expanduser('~'), '.config', 'google-chrome', 'Default', 'Cookies')
    else:
        print("Unsupported operating system")
        return

    # Create a temporary copy of the cookies file
    temp_copy_path = 'temp_cookies_copy' 
    try:
        shutil.copy(cookies_file_path, temp_copy_path)
    except FileNotFoundError:
        print(f"Error: File not found - {cookies_file_path}")
        return

    # Connect to the Chrome cookies SQLite database
    try:
        connection = sqlite3.connect(temp_copy_path)
        cursor = connection.cursor()

        # Execute a query to get the complete cookies
        cursor.execute("SELECT name, value, host_key, path, expires_utc, is_secure, is_httponly FROM cookies")
        rows = cursor.fetchall()  # Fetch all the rows

        # Create a Pandas DataFrame for better tabular formatting
        columns = ["Name", "Value", "Host Key", "Path", "Expires UTC", "Is Secure", "Is HttpOnly"]
        df = pd.DataFrame(rows, columns=columns)
        df.to_csv('chrome_cookies.csv', index=False)  # Save the DataFrame to a CSV file

    except sqlite3.Error as e:
        print(f"Error reading Chrome cookies: {e}")

    finally:
        if connection:
            connection.close()

        os.remove(temp_copy_path)  # Remove the temporary copy

    df = pd.read_csv('chrome_cookies.csv')  # Read the CSV file into a Pandas DataFrame

    # GUI
    cookiesWindow = tkinter.Toplevel(parent_window)  # Use Toplevel instead of Tk
    cookiesWindow.title("Google Chrome Cookies")
    cookiesWindow.configure(background=bgColor)
    positionWindow(cookiesWindow, width=1000, height=730)

    titleText = tkinter.Label(cookiesWindow, text="ForensicXpert: Web Browser Forensics - Cookies", bg="black", fg=pinkColor, pady=10, font=("Consolas", 15, "italic"))
    titleText.pack(side="top", fill="x")

    # Create a Treeview widget to display the CSV contents as a table
    style = ttk.Style()
    style.configure("Treeview",
                    background=bgColor,
                    fieldbackground=bgColor,
                    foreground="white",
                    font=("Consolas", 11))

    tree = ttk.Treeview(cookiesWindow, style="Treeview")
    tree["columns"] = ('Sr. No.',) + tuple(df.columns)

    # Configure columns
    for col in tree["columns"]:
        tree.column(col, anchor=tkinter.W)
        tree.heading(col, text=col)

    # Insert data into the Treeview with serial numbers
    for i, (index, row) in enumerate(df.iterrows(), start=0):
        tree.insert("", i, values=(str(i),) + tuple(row))

    # Set up vertical scrollbar
    yscrollbar = ttk.Scrollbar(cookiesWindow, orient="vertical", command=tree.yview)
    yscrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=yscrollbar.set)

    # Set up horizontal scrollbar
    xscrollbar = ttk.Scrollbar(cookiesWindow, orient="horizontal", command=tree.xview)
    xscrollbar.pack(side="bottom", fill="x")
    tree.configure(xscrollcommand=xscrollbar.set)

    tree.pack(expand=True, fill=tkinter.BOTH)  # Pack the Treeview
    cookiesWindow.mainloop()
    CutPaste.cut_and_paste_file("chrome_cookies.csv", "Evidence_Collection/chrome_cookies.csv") # Save history file to evidence
