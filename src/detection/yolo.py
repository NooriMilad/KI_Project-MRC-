class YOLODetector:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        from ultralytics import YOLO
        self.model = YOLO(self.model_path)

    def detect_objects(self, image):
        results = self.model(image)
        detections = results.pandas().xyxy[0]  # Get detections in pandas DataFrame format
        return detections