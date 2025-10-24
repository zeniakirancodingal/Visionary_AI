import cv2
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------
# Helper Function: Display image using matplotlib
# ------------------------------------------------------
def display_image(title, image):
    """Displays an image with a given title using matplotlib."""
    plt.figure(figsize=(8, 8))

    # If image has only 2 dimensions, it’s grayscale
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        # Convert BGR (OpenCV format) → RGB (matplotlib format)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.title(title)
    plt.axis('off')  # Hide the axes
    plt.show()
    

# ------------------------------------------------------
# Main Function: Interactive Edge Detection & Filtering
# ------------------------------------------------------
def interactive_edge_detection(image_path):
    """Performs different image processing techniques interactively."""
    
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("❌ Error: Image not found!")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", gray_image)

    # Display options
    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")


    # Continuous loop for user choices
    while True:
        choice = input("Enter your choice (1–6): ")

        # ------------------------------------------------------
        # 1️⃣ Sobel Edge Detection
        # ------------------------------------------------------
        if choice == "1":
            # Detect edges along X (horizontal) and Y (vertical) directions
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

            # Combine both directions into one edge image
            combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
            display_image("Sobel Edge Detection", combined_sobel)

        # ------------------------------------------------------
        # 2️⃣ Canny Edge Detection
        # ------------------------------------------------------
        elif choice == "2":
            print("Adjust thresholds for Canny (default: 100 and 200)")
            lower_thresh = int(input("Enter lower threshold: "))
            upper_thresh = int(input("Enter upper threshold: "))

            if not lower_thresh or not upper_thresh:
                continue

            # Apply Canny algorithm
            edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)
            display_image("Canny Edge Detection", edges)

        # ------------------------------------------------------
        # 3️⃣ Laplacian Edge Detection
        # ------------------------------------------------------
        elif choice == "3":
            # Detect edges using the Laplacian operator
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))

        # ------------------------------------------------------
        # 4️⃣ Gaussian Smoothing (Blurring)
        # ------------------------------------------------------
        elif choice == "4":
            print("Adjust kernel size for Gaussian blur (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size (odd number): "))

            # Apply Gaussian Blur (helps reduce noise)
            blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
            display_image("Gaussian Smoothed Image", blurred)

        # ------------------------------------------------------
        # 5️⃣ Median Filtering
        # ------------------------------------------------------
        elif choice == "5":
            print("Adjust kernel size for Median filtering (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size (odd number): "))

            # Apply Median Blur (good for salt-and-pepper noise)
            median_filtered = cv2.medianBlur(image, kernel_size)
            display_image("Median Filtered Image", median_filtered)

        # ------------------------------------------------------
        # 6️⃣ Exit
        # ------------------------------------------------------
        elif choice == "6":
            print("Exiting program...")
            break

        # ------------------------------------------------------
        # Invalid choice
        # ------------------------------------------------------
        else:
            print("⚠️ Invalid choice. Please select a number between 1 and 6.")

# ------------------------------------------------------
# Run the program with an example image
# ------------------------------------------------------
interactive_edge_detection('../images/bird.jpeg')