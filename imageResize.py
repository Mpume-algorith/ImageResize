from PIL import Image
import os
import sys


# Specify the folder containing images
image_folder = 'C:\\Users\\mtsotsha\\Downloads\\Image Resize Test Folder\\OneDrive_1_2023-09-27\\Vici\\The Roma\\Image version'

# Desired size for the resized images
new_size = (356, 348)  # Example size (width, height)

# Loop over all files in the directory
for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        # Construct the full file path
        file_path = os.path.join(image_folder, filename)
        
        # Open the image
        with Image.open(file_path) as img:
            # Resize the image
            img = img.resize(new_size, Image.Resampling.LANCZOS)

            
            # Save it back to disk
            img.save(file_path)

print('All images have been resized.')
