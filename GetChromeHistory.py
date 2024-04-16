import sqlite3
import os
import platform
import shutil
import pandas as pd
import CutPaste
import tkinter
from tkinter import ttk
from StaticGUIConfigs import *

def getChromeHistory(parent_window):

    # Detect the operating system to find the Chrome history file location
    if platform.system() == 'Windows':
        history_file_path = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'Default', 'History')
    elif platform.system() == 'Darwin':  # macOS
        history_file_path = os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'Google', 'Chrome', 'Default', 'History')
    elif platform.system() == 'Linux':
        history_file_path = os.path.join(os.path.expanduser('~'), '.config', 'google-chrome', 'Default', 'History')
    else:
        print("Unsupported operating system")
        return

    # Create a temporary copy of the history file
    temp_copy_path = 'temp_history_copy'
    shutil.copy(history_file_path, temp_copy_path)

    # Connect to the Chrome history SQLite database
    try:
        connection = sqlite3.connect(temp_copy_path)
        cursor = connection.cursor()

        # Execute a query to get the complete history
        cursor.execute("SELECT title, url, last_visit_time/1000000 as last_visit_time FROM urls ORDER BY last_visit_time DESC")
        rows = cursor.fetchall() # Fetch all the rows

        # Create a Pandas DataFrame for better tabular formatting
        columns = ["Title", "URL", "Last Visit Time"]
        df = pd.DataFrame(rows, columns=columns)
        df.to_csv('chrome_history.csv', index=False) # Save the DataFrame to a CSV file

    except sqlite3.Error as e:
        print(f"Error reading Chrome history: {e}")

    finally:
        if connection:
            connection.close()

        os.remove(temp_copy_path) # Remove the temporary copy 
    
    df = pd.read_csv('chrome_history.csv') # Read the CSV file into a Pandas DataFrame


    # GUI
    historyWindow = tkinter.Toplevel(parent_window) # Main window
    historyWindow.title("Google Chrome History")
    historyWindow.configure(background=bgColor)
    positionWindow(historyWindow, width=1000, height=730) # Stick the window at the top edge of screen

    # Create a Treeview widget to display the CSV contents as a table
    style = ttk.Style()
    style.configure("Treeview",
                    background=bgColor,
                    fieldbackground=bgColor,
                    foreground="white",
                    font=("Consolas", 11))

    tree = ttk.Treeview(historyWindow, style="Treeview")
    tree["columns"] = ('Sr. No.',) + tuple(df.columns)

    # Configure columns
    for col in tree["columns"]:
        tree.column(col, anchor=tkinter.W)
        tree.heading(col, text=col)

    # Insert data into the Treeview with serial numbers
        for i, (index, row) in enumerate(df.iterrows(), start=0):
            tree.insert("", i, values=(str(i),) + tuple(row))

    # Set up vertical scrollbar
    yscrollbar = ttk.Scrollbar(historyWindow, orient="vertical", command=tree.yview)
    yscrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=yscrollbar.set)

    # Set up horizontal scrollbar
    xscrollbar = ttk.Scrollbar(historyWindow, orient="horizontal", command=tree.xview)
    xscrollbar.pack(side="bottom", fill="x")
    tree.configure(xscrollcommand=xscrollbar.set)

    tree.pack(expand=True, fill=tkinter.BOTH) # Pack the Treeview
    historyWindow.mainloop()

    CutPaste.cut_and_paste_file("chrome_history.csv", "Evidence_Collection/chrome_history.csv") # Save history file to evidence

# getChromeHistory()