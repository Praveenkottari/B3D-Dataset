import os
import random

# Set the directory where the images are located
directory = r'C:\Users\prave\OneDrive - Indian Institute of Science\IISc\Integrated Building Health Moniterirng\dataset\curated-dataset\stain'

# Get a list of all files in the directory
files = os.listdir(directory)

# Filter the list to include only JPEG files
image_files = [f for f in files if f.endswith('.jpg') or f.endswith('.jpeg')]

# Shuffle the image files
random.shuffle(image_files)

# Rename the files
for i, image_file in enumerate(image_files, start=1):
    old_path = os.path.join(directory, image_file)
    new_filename = f'cls06_{str(i).zfill(3)}.jpg'
    new_path = os.path.join(directory, new_filename)
    os.rename(old_path, new_path)
    print(f'Renamed {image_file} to {new_filename}')