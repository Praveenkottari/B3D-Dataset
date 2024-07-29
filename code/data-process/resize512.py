import os
from PIL import Image

def resize_images_in_folder(input_folder, output_folder, size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpeg") or filename.endswith(".jpg"):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            resize_image(input_image_path, output_image_path, size)

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(size)
    resized_image.save(output_image_path)

input_folder = r"C:\Users\prave\OneDrive - Indian Institute of Science\IISc\Integrated Building Health Moniterirng\dataset\annotated\stain"
output_folder = r"C:\Users\prave\OneDrive - Indian Institute of Science\IISc\Integrated Building Health Moniterirng\dataset\annotated\512x512\stain"
size = (512, 512)

resize_images_in_folder(input_folder, output_folder, size)
