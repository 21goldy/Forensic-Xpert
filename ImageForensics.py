import os
import exifread
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def create_image_metadata_viewer(parent_window):
    root = tk.Toplevel(parent_window)
    root.title("Image Forensics Tool")
    root.resizable(False, False)
    root.geometry("1200x550")
    
    bgColor = "lightgray"

    root['background'] = bgColor

    # Select image heading
    selectImageLabel = tk.Label(
        root,
        text="Select an Image file:",
        font=("Consolas", 11),
        background=bgColor)
    
    # Select image heading
    previewLabel = tk.Label(
        root,
        text="Image Preview:",
        font=("Consolas", 11),
        background=bgColor)

    # Browser button to select image
    button_browse = tk.Button(
        root,
        text="Browse",
        command=lambda: browse_file(root),
        padx=30,
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
        width=70,
        background="lightblue")

    scrollbar = tk.Scrollbar(root, command=text_result.yview)

    # Export result to txt file button
    button_export = tk.Button(
        root,
        text="Export to TXT",
        command=lambda: export_to_txt(root, text_result),
        background="darkgray",
        padx=20,
        pady=5)

    # Layout setting
    selectImageLabel.place(x=20, y=20)
    previewLabel.place(x=650, y=50)
    text_result.place(x=20, y=120)
    button_browse.place(x=465, y=15)
    label_result.place(x=20, y=90)
    scrollbar.place(x=590,y=120)
    button_export.place(x=250, y=470)
    text_result.config(yscrollcommand=scrollbar.set)

    root.mainloop()


# Browser to select files function
def browse_file(root):
    file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        # Clear previous results
        text_result = root.children['!text']
        text_result.delete(1.0, tk.END)

        metadata = get_image_metadata(file_path)  # Get metadata
        display_metadata_results(text_result, metadata)  # Display results in the text widget

        # Display image preview
        display_image_preview(root, file_path)

def display_image_preview(root, file_path):
    image = Image.open(file_path)
    image.thumbnail((400, 400))
    photo = ImageTk.PhotoImage(image)

    # Dynamically create the label for image preview
    image_preview_label = tk.Label(root, image=photo)
    image_preview_label.image = photo
    image_preview_label.place(x=700, y=100)

# Rest of the code remains unchanged...

# Get metadata function
def get_image_metadata(image_path):
    metadata = {}

    try:
        # Open image
        with open(image_path, 'rb') as file:
            tags = exifread.process_file(file)

        # Extract metadata
        metadata['File Path'] = image_path
        metadata['File Name'] = os.path.basename(image_path)

        # Basic image information
        metadata['Image Width'] = tags.get('Image ImageWidth', 'N/A')
        metadata['Image Height'] = tags.get('Image ImageLength', 'N/A')
        metadata['Camera Make'] = tags.get('Image Make', 'N/A')
        metadata['Camera Model'] = tags.get('Image Model', 'N/A')
        metadata['Software'] = tags.get('Image Software', 'N/A')

        # Time and date
        metadata['DateTime Original'] = tags.get('EXIF DateTimeOriginal', 'N/A')
        metadata['DateTime Image'] = tags.get('Image DateTime', 'N/A')

        # Camera settings
        metadata['Exposure Time'] = tags.get('EXIF ExposureTime', 'N/A')
        metadata['FNumber'] = tags.get('EXIF FNumber', 'N/A')
        metadata['ISO Speed Ratings'] = tags.get('EXIF ISOSpeedRatings', 'N/A')
        metadata['Exposure Bias'] = tags.get('EXIF ExposureBiasValue', 'N/A')
        metadata['Metering Mode'] = tags.get('EXIF MeteringMode', 'N/A')

        # GPS information
        metadata['GPS Latitude'] = tags.get('GPS GPSLatitude', 'N/A')
        metadata['GPS Longitude'] = tags.get('GPS GPSLongitude', 'N/A')
        metadata['GPS Altitude'] = tags.get('GPS GPSAltitude', 'N/A')
        metadata['GPS TimeStamp'] = tags.get('GPS GPSTimeStamp', 'N/A')

        # Thumbnail information
        metadata['Thumbnail'] = tags.get('JPEGThumbnail', 'N/A')

        # Other details
        metadata['Orientation'] = tags.get('Image Orientation', 'N/A')
        metadata['Flash'] = tags.get('EXIF Flash', 'N/A')
        metadata['White Balance'] = tags.get('EXIF WhiteBalance', 'N/A')
        metadata['Scene Capture Type'] = tags.get('EXIF SceneCaptureType', 'N/A')

        # MakerNote information
        metadata['MakerNote'] = tags.get('Image MakerNote', 'N/A')

    except Exception as e:
        metadata['Error'] = str(e)

    return metadata

# Display result function
def display_metadata_results(text_result, metadata):
    for key, value in metadata.items():
        text_result.insert(tk.END, f"{key}: {value}\n")

# Export function
def export_to_txt(root, text_result):
    result_text = text_result.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if file_path:
        with open(file_path, 'w') as file:
            file.write(result_text)
        messagebox.showinfo("Export Successful", "Metadata results exported to the text file.")

# if __name__ == "__main__":
#     create_image_metadata_viewer()
