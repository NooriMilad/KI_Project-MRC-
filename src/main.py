import cv2
import pandas as pd
from detection.yolo import YOLODetector
from detection.ocr import extract_text
from dashboard.gui import Dashboard
from dashboard.webcam import start_webcam
from utils.helpers import save_image, log_illegal_plate
import time

def main():
    # Load allowed plates from CSV
    allowed_plates = pd.read_csv("src/data/allowed_plates.csv")["plate"].tolist()
    
    # Initialize YOLO detector
    yolo_detector = YOLODetector()
    yolo_detector.load_model()

    # Initialize dashboard
    dashboard = Dashboard()

    # Start webcam
    webcam = start_webcam()

    # Statistics
    total_cars = 0
    access_granted = 0
    access_denied = 0

    while True:
        ret, frame = webcam.read()
        if not ret:
            break

        # Detect objects in the frame
        boxes, labels = yolo_detector.detect_objects(frame)

        # Process detected objects
        for box, label in zip(boxes, labels):
            if label == 'license_plate':
                total_cars += 1
                x, y, w, h = box
                roi = frame[y:y+h, x:x+w]
                plate_text = extract_text(roi)

                if plate_text in allowed_plates:
                    access_granted += 1
                    dashboard.update_display(plate_text, "Access Granted")
                else:
                    access_denied += 1
                    dashboard.update_display(plate_text, "Access Denied")
                    log_illegal_plate(plate_text)
                    save_image(frame, f"src/data/illegal_{plate_text}.jpg")

        # Update dashboard statistics
        stats = {
            'total_cars': total_cars,
            'access_granted': access_granted,
            'access_denied': access_denied,
            'current_time': time.strftime("%Y-%m-%d %H:%M:%S")
        }
        dashboard.show_statistics(stats)

        # Display the frame
        cv2.imshow('Webcam Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()