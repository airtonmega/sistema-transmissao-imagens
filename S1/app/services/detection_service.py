import cv2

class DetectionService:
    def __init__(self, model_path: str):
        self.net = cv2.dnn.readNet(model_path)
        self.model = cv2.dnn_DetectionModel(self.net)
        self.model.setInputParams(size=(416, 416), scale=1/255)
        self.trackers = {}

    def detect(self, image, client_id):
        class_ids, scores, boxes = self.model.detect(image, confThreshold=0.5, nmsThreshold=0.4)
        if client_id not in self.trackers:
            self.trackers[client_id] = []
        
        for box in boxes:
            self.trackers[client_id].append(box)
        
        return boxes, scores, class_ids

    def count_people(self, class_ids):
        return sum([1 for class_id in class_ids if class_id == 0])
