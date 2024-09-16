from PIL import Image
import numpy as np
import cv2

# Load the image with Pillow and convert it to OpenCV format
image = Image.open('your_image12.jpg')
image_cv = np.array(image)

# Get image dimensions
height, width = image_cv.shape[:2]

# Coordinates of the four corners to crop, given as percentages
# For example: top-left (5%, 10%), top-right (95%, 10%), bottom-right (95%, 80%), bottom-left (5%, 80%)
corners_percentage = [
    (7.7,7.1),    # top-left (x1%, y1%)
    (81,26.9),   # top-right (x2%, y2%)
    (82.7,81.4),     # bottom-right (x4%, y4%)
    (2,76.1)    # bottom-left (x3%, y3%)
]

# Convert percentage-based corners to pixel values
corners = [(x * width / 100, y * height / 100) for x, y in corners_percentage]
corners = np.array(corners, dtype=np.float32)

# Define the destination points for the 16:9 rectangle (for example: 1600x900)
output_size = (1600, 900)
dest_corners = np.array([
    [0, 0],                        # Top-left
    [output_size[0] - 1, 0],        # Top-right
    [output_size[0] - 1, output_size[1] - 1],  # Bottom-right
    [0, output_size[1] - 1]         # Bottom-left
], dtype=np.float32)

# Get the perspective transform matrix
matrix = cv2.getPerspectiveTransform(corners, dest_corners)

# Apply the perspective warp
warped_image_cv = cv2.warpPerspective(image_cv, matrix, output_size)

# Convert back to Pillow Image
warped_image = Image.fromarray(warped_image_cv)

# Save or display the warped image
warped_image.save('cropped_and_stretched_image.jpg')
warped_image.show()
