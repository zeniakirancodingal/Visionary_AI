import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image."""

    # Create a copy of the image to avoid modifying the original
    result = image.copy()
    if filter_type == "red_tint":

        # Keep only red channel
        result[:, :, 1] = 0  # Green channel to 0
        result[:, :, 0] = 0  # Blue channel to 0

    elif filter_type == "blue_tint":
        # Keep only blue channel
        result[:, :, 1] = 0  # Green channel to 0
        result[:, :, 2] = 0  # Red channel to 0

    elif filter_type == "green_tint":
        # Keep only green channel
        result[:, :, 0] = 0  # Blue channel to 0
        result[:, :, 2] = 0  # Red channel to 0

    elif filter_type == "increase_red_green":
        # Increase the intensity of the red channel
        result[:, :, 1] = cv2.add(result[:, :, 1], 50)  
        result[:, :, 2] = cv2.add(result[:, :, 2], 50)  

    elif filter_type == "decrease_blue_red":
        # Decrease the intensity of the blue channel

        result[:, :, 0] = cv2.subtract(result[:, :, 0], 50)
    return result

# Load the image
image_path = '../images/bird.jpeg'  # Provide your image path
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    filter_type = "original"  # Default filter type

    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red & Green Intensity")
    print("d - Decrease Blue & Red Intensity")
    print("q - Quit")

    while True:

        cv2.imshow("original Image", image)

        # Wait for key press
        key = cv2.waitKey(0) & 0xFF

        filtered_image = []
        # Map key presses to filters
        if key == ord('r'):
            filtered_image = apply_color_filter(image, "red_tint")
        elif key == ord('b'):
            filtered_image = apply_color_filter(image, "blue_tint")
        elif key == ord('g'):
            filtered_image = apply_color_filter(image, "green_tint")
        elif key == ord('i'):
            filtered_image = apply_color_filter(image, "increase_red_green")
        elif key == ord('d'):
            filtered_image = apply_color_filter(image, "decrease_blue_red")
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', or 'q'.")
                # Apply the selected filter

        # Display the filtered image
        cv2.imshow("Filtered Image", filtered_image)

cv2.destroyAllWindows()
