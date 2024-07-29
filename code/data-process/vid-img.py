import cv2
import os

# Set the input video file path
video_file = r'C:\Users\prave\OneDrive - Indian Institute of Science\IISc\Integrated Building Health Moniterirng\Backup\collected-data\capture\set10\vid3.mp4'

# Set the output directory for the extracted images
output_dir = r'C:\Users\prave\OneDrive - Indian Institute of Science\IISc\Integrated Building Health Moniterirng\Backup\collected-data\capture\set10'

# Open the video file
cap = cv2.VideoCapture(video_file)

# Get the video frame rate
fps = cap.get(cv2.CAP_PROP_FPS)

# Set the frame interval to extract 5 images per second
frame_interval = int(fps / 5)

# Initialize the frame count
frame_count = 0

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through the video frames and extract the images
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If there are no more frames, break the loop
    if not ret:
        break

    # Check if it's time to extract an image
    if frame_count % frame_interval == 0:
        # Generate the output file name
        output_file = os.path.join(output_dir, f'image_vid3{frame_count}.jpg')

        # Save the frame as a JPEG image
        cv2.imwrite(output_file, frame)

    # Increment the frame count
    frame_count += 1

# Release the video capture object
cap.release()

print(f'Extracted {frame_count} images from the video.')