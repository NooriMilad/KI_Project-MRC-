# License Plate Recognition with AI

This project implements a license plate recognition system using artificial intelligence. The system detects license plates from vehicle images captured via a webcam and checks them against a list of allowed plates stored in a CSV file. 

## Project Structure

- **src/**: Contains the main application code.
  - **main.py**: Entry point of the application that initializes the webcam and manages the dashboard.
  - **detection/**: Contains the detection algorithms.
    - **yolo.py**: Implements the YOLO object detection model.
    - **ocr.py**: Implements Optical Character Recognition (OCR) using pytesseract.
  - **dashboard/**: Manages the graphical user interface (GUI).
    - **gui.py**: Handles the dashboard display and updates.
    - **webcam.py**: Manages the webcam feed and captures frames.
  - **data/**: Contains data files.
    - **allowed_plates.csv**: List of allowed license plates.
    - **illegal_log.csv**: Logs unknown license plates.
  - **utils/**: Contains utility functions.
    - **helpers.py**: Provides helper functions for saving images and logging.

## Requirements

To run this project, you need to install the following Python libraries:

- ultralytics
- opencv-python
- pytesseract
- pandas
- pygame

You can install the required libraries using the following command:

```
pip install -r requirements.txt
```

## Usage

1. Run the application by executing `main.py`.
2. The webcam will start, and the system will begin detecting vehicles and their license plates.
3. Detected license plates will be checked against the allowed plates list.
4. The dashboard will display the access status ("Access Granted" or "Access Denied") along with the recognized license plate.
5. Unknown license plates will be logged in `illegal_log.csv`, and the corresponding images will be saved.

## Future Improvements

- Implement a feature to export daily statistics.
- Add sound notifications for access denied events.
- Enhance the GUI for better user experience.

## License

This project is licensed under the MIT License.