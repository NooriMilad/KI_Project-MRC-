from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows
from utils.helpers import save_image
import time

def start_webcam(dashboard):
    cap = VideoCapture(0)  # Initialize the webcam
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            print("Error: Could not read frame.")
            break

        # Here you would call the detection functions and update the dashboard
        # For example:
        # detected_plate, status = detect_license_plate(frame)
        # dashboard.update_display(detected_plate, status)

        imshow("Webcam Feed", frame)  # Display the resulting frame

        # Exit on 'q' key
        if waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # When everything done, release the capture
    destroyAllWindows()  # Close all OpenCV windows