import cv2

# Initialize webcam feed
camera = cv2.VideoCapture(0)

# Check if the camera is working
if not camera.isOpened():
    print("Camera not accessible.")
    exit(1)

# Load the Haar Cascade for frontal face detection
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

print("Press 'q' to exit the program...")

while True:
    # Read a single frame from the webcam
    success, frame = camera.read()
    if not success:
        print("Failed to grab frame.")
        break

    # Convert the captured frame to grayscale for better detection accuracy
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect multiple faces in the grayscale image
    detected_faces = detector.detectMultiScale(
        grayscale,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Highlight each detected face with a rectangle
    for (x, y, w, h) in detected_faces:
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 2)

    # Display the live video with rectangles drawn
    cv2.imshow("Live Face Detection", frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup resources
camera.release()
cv2.destroyAllWindows()
