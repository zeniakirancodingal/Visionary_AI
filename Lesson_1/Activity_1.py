import cv2
import matplotlib.pyplot as plt

image = cv2.imread('./../images/bird.jpeg')

# Convert BGR to RGB
# Matplot lib expects image in RGB format to display it correctly.

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)
plt.title("RGB Image")
plt.show()

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.show()

# Cropping the image

cropped_image = image[200:400, 300:500]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()
