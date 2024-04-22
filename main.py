from ultralytics import YOLO
import os

os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

# Load the YOLOv8 model
model = YOLO('./runs/detect/train/weights/best.pt')

# Export the model to TFLite format
model.export(format='tflite', int8=True)

# # Load the exported TFLite model
# tflite_model = YOLO('runs/detect/train/weights/best_saved_model/best_float32.tflite')

# # Run inference
# results = tflite_model('datasets/SKU-110K/images/test_1004.jpg')