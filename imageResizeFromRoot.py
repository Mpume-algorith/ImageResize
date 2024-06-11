import os
from PIL import Image

def resize_image(file_path, new_size):
    with Image.open(file_path) as img:
        img = img.resize(new_size, Image.Resampling.LANCZOS)
        img.save(file_path)

def is_image(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))

def process_directory(directory, new_size):
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            if is_image(file_path):
                resize_image(file_path, new_size)

# Specify the root directory and the new size
root_directory = 'C:\\Users\\mtsotsha\\Downloads\\ATX'
new_size = (356, 348)  # Example size (width, height)

process_directory(root_directory, new_size)
print('Image resizing process is complete.')
