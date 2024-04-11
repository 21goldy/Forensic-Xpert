from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import tkinter as tk
from tkinter import filedialog, messagebox
from StaticGUIConfigs import *

def create_video_metadata_viewer(parent_window):
    root = tk.Toplevel(parent_window)
    root.title("Video Forensics Tool")
    root.resizable(False, False) # Disallow resizing of the mainWindow
    root['background']=bgColor # Set backgound color 

    # Select Video Heading
    label = tk.Label(
        root,
        text="Select a video file:",
        font=("Consolas", 11),
        background=bgColor,
        padx=10,
        pady=5)
    
    # Browser button to select video
    button_browse = tk.Button(
        root,
        text="Select a Video file",
        command=lambda: browse_file(root),
        padx=10,
        pady=5,
        font=("Consolas", 11),
        background="darkgray")
    
    # Result heading
    label_result = tk.Label(
        root,
        text="Metadata Results:",
        font=("Consolas", 12),
        background=bgColor)
    
    # Output window
    text_result = tk.Text(
        root,
        wrap=tk.WORD,
        height=20,
        width=50,
        background="lightblue")
    
    scrollbar = tk.Scrollbar(root, command=text_result.yview) # Initialize scrollbar

    # Export result to txt file button
    button_export = tk.Button(
        root,
        text="Export",
        command=lambda: export_to_txt(root, text_result),
        background="darkgray",
        padx=10,
        pady=5)

    # Layout settings
    label.grid(row=0, column=0, padx=10, pady=10)
    button_browse.grid(row=0, column=1, padx=10, pady=10)
    label_result.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    text_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    scrollbar.grid(row=2, column=2, sticky='ns')
    button_export.grid(row=3, column=0, columnspan=2, pady=10)
    
    text_result.config(yscrollcommand=scrollbar.set) # Configure text widget to use scrollbar

    root.mainloop()

# Browser to select files function
def browse_file(root):
    file_path = filedialog.askopenfilename(title="Select a video file", filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
    if file_path:
        # Clear previous results
        text_result = root.children['!text']
        text_result.delete(1.0, tk.END)

        metadata = get_video_metadata(file_path) # Get metadata        
        display_metadata_results(text_result, metadata) # Display results in the text widget

# Get metadata function
def get_video_metadata(video_path):
    metadata = {}

    try:
        # Create parser
        parser = createParser(video_path)
        if not parser:
            raise Exception("Unable to create parser for the given video file.")

        # Extract metadata
        metadata_info = extractMetadata(parser)
        if metadata_info:
            metadata = metadata_info.exportDictionary()

    except Exception as e:
        metadata['Error'] = str(e)

    return metadata

# Display result function
def display_metadata_results(text_result, metadata):
    text_result.delete(1.0, tk.END)  # Clear previous results
    text_result.insert(tk.END, "Metadata:\n")
    for key, value in metadata.items():
        text_result.insert(tk.END, f"{key}: {value}\n")
    text_result.insert(tk.END, "\n")

# Export function
def export_to_txt(root, text_result):
    result_text = text_result.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if file_path:
        with open(file_path, 'w') as file:
            file.write(result_text)
        messagebox.showinfo("Export Successful", "Metadata results exported to the text file.")

# if __name__ == "__main__":
#     create_video_metadata_viewer()
