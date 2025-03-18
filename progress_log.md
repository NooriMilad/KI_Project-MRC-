# Progress Log for License Plate Recognition Project

## Week 1
### Day 1
- Started the project setup.
- Created the project structure and initialized Git repository.
- Installed required libraries: ultralytics, opencv-python, pytesseract, pandas, pygame.

### Day 2
- Implemented the basic structure of `main.py`.
- Set up the webcam feed using OpenCV.
- Encountered issues with webcam initialization; resolved by checking camera permissions.

### Day 3
- Began working on the YOLO object detection model in `yolo.py`.
- Loaded the YOLO model and tested it with sample images.
- Issues with model accuracy; researched and adjusted confidence thresholds.

## Week 2
### Day 4
- Implemented the OCR functionality in `ocr.py`.
- Successfully extracted text from images of license plates.
- Faced challenges with image quality affecting OCR results; improved preprocessing steps.

### Day 5
- Developed the dashboard GUI in `gui.py`.
- Integrated the display of detected license plates and access status.
- Added functionality to update statistics in real-time.

### Day 6
- Created the CSV management functions in `helpers.py`.
- Implemented adding and removing license plates from `allowed_plates.csv`.
- Encountered issues with file handling; resolved by ensuring proper file paths.

## Week 3
### Day 7
- Finalized the integration of all components in `main.py`.
- Tested the complete workflow from detection to dashboard display.
- Identified bugs in the statistics display; fixed logic errors in counting.

### Day 8
- Conducted extensive testing with various license plates.
- Logged unknown plates in `illegal_log.csv`.
- Added functionality to save images of unknown plates.

### Day 9
- Reflected on the project progress and documented improvements.
- Considered adding sound notifications for access denied events.
- Planned for a daily export of statistics for better tracking.

## Future Improvements
- Implement a feature for daily statistics export.
- Enhance the GUI for better user experience.
- Explore additional machine learning models for improved detection accuracy.