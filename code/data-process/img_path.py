import os
import pandas as pd

# Set the folder path where the images are located
folder_path = r'C:\Users\prave\OneDrive - Indian Institute of Science\IISc\Integrated Building Health Moniterirng\dataset\building-dataset\stain'

# Create a list to store the image names and paths
image_names = []
#image_paths = []

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        # Get the full path of the image
        #image_path = os.path.join(folder_path, filename)
        # Append the image name and path to the lists
        image_names.append(filename)
        #image_paths.append(image_path)

# Create a pandas DataFrame with the image names and paths
# data = {'Image Name': image_names, 'Image Path': image_paths}
data = {'Image Name': image_names}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel sheet
df.to_excel(r'C:\Users\prave\OneDrive - Indian Institute of Science\IISc\Integrated Building Health Moniterirng\image_info.xlsx', index=False)

print('Image information saved to "image_info.xlsx".')