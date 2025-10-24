import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('../images/bird.jpeg')

# Convert BGR (OpenCV default) to RGB for Matplotlib display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ---------------------------
# Rotate the image by 45°
# ---------------------------
(height, width) = image.shape[:2]
center = (width / 2, height / 2)

# Create the rotation matrix (rotate 45 degrees, scale 1.0)
M = cv2.getRotationMatrix2D(center, 45, 1.0)

# Apply the rotation to the image
rotated = cv2.warpAffine(image, M, (w, h))

# Convert rotated image from BGR to RGB for Matplotlib
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

# Display rotated image
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

# Create a matrix filled with 50s (same shape as image)
# creating an array filled with ones, the same size as your image 
# Multiplying by 50 → every value becomes 50
#  
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50 

# performs pixel-wise addition
brighter = cv2.add(image, brightness_matrix)  # Safely add brightness

# Convert brightened image to RGB for Matplotlib display
brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)

# Display brighter image
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()
