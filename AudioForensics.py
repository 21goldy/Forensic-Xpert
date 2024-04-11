import os
from tinytag import TinyTag
import tkinter as tk
from tkinter import filedialog, messagebox
from StaticGUIConfigs import * 

def run_audio_metadata_viewer(parent_window):

    # Browser to select files function
    def browse_file():
        file_path = filedialog.askopenfilename(title="Select an audio file", filetypes=[("Audio files", "*.mp3;*.ogg;*.flac")])
        if file_path:
            # Clear previous results
            text_result = root.children['!text']
            text_result.delete(1.0, tk.END)

            metadata = get_audio_metadata(file_path) # Get metadata
            display_metadata_results(metadata) # Display results in the text widget

    # Get metadata function
    def get_audio_metadata(audio_path):
        metadata = {}

        try:
            # Open audio file
            tag = TinyTag.get(audio_path)

            # Extract metadata
            metadata['File Path'] = audio_path
            metadata['Album'] = tag.album
            metadata['Album Artist'] = tag.albumartist
            metadata['Artist'] = tag.artist
            metadata['Audio Offset'] = tag.audio_offset
            metadata['Bitrate'] = tag.bitrate
            metadata['Channels'] = tag.channels
            metadata['Comment'] = tag.comment
            metadata['Disc'] = tag.disc
            metadata['Total Discs'] = tag.disc_total
            metadata['Duration (seconds)'] = tag.duration
            metadata['File Size (bytes)'] = tag.filesize
            metadata['Genre'] = tag.genre
            metadata['Sample Rate'] = tag.samplerate
            metadata['Title'] = tag.title
            metadata['Track'] = tag.track
            metadata['Total Tracks'] = tag.track_total
            metadata['Year'] = tag.year

        except Exception as e:
            metadata['Error'] = str(e)

        return metadata

    # Display result function
    def display_metadata_results(metadata):
        text_result.insert(tk.END, "Audio Metadata:\n")
        for key, value in metadata.items():
            text_result.insert(tk.END, f"{key}: {value}\n")
        text_result.insert(tk.END, "\n")

    # Export function
    def export_to_txt():
        result_text = text_result.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path, 'w') as file:
                file.write(result_text)
            messagebox.showinfo("Export Successful", "Metadata results exported to the text file.")

    # Create the main Tkinter window
    root = tk.Toplevel(parent_window)
    root.title("Audio Forensics Tool")
    root.resizable(False, False) # Disallow resizing of the mainWindow
    root['background']=bgColor # Set backgound color

    # Select audio heading
    label = tk.Label(
        root,
        text="Select an audio file:",
        font=("Consolas", 11),
        background=bgColor,
        padx=10,
        pady=5)
    
    # Browser button to select image
    button_browse = tk.Button(
        root,
        text="Browse",
        command=browse_file,
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
        text="Export to TXT",
        command=export_to_txt,
        background="darkgray",
        padx=10,
        pady=5)

    # Layout setting
    label.grid(row=0, column=0, padx=10, pady=10)
    button_browse.grid(row=0, column=1, padx=10, pady=10)
    label_result.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    text_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    scrollbar.grid(row=2, column=2, sticky='ns')
    button_export.grid(row=3, column=0, columnspan=2, pady=10)

    text_result.config(yscrollcommand=scrollbar.set) # Configure text widget to use scrollbar

    root.mainloop()

# if __name__ == "__main__":
#     run_audio_metadata_viewer()
