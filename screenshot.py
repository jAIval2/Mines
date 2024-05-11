import os
from PIL import Image


# Function to crop images
def crop_images(input_folder, output_folder, crop_coords):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of files in input folder
    files = os.listdir(input_folder)

    # Iterate over each file
    for file in files:
        # Check if the file is an image
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            # Open the image
            image_path = os.path.join(input_folder, file)
            image = Image.open(image_path)

            # Crop the image
            cropped_image = image.crop(crop_coords)

            # Save the cropped image
            output_path = os.path.join(output_folder, file)
            cropped_image.save(output_path)
            print(f"Image '{file}' cropped and saved successfully.")


# Define input and output folders
input_folder = "input"
output_folder = "cropped_images"

# Define crop coordinates (left, upper, right, lower)
crop_coords = (575, 186, 1066, 690)

# Crop images
crop_images(input_folder, output_folder, crop_coords)
