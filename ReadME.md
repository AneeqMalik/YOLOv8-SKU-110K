
## SKU-111K Dataset with YOLOv8 Object Detection

#### This repository contains the implementation of the YOLOv8 object detection model on the SKU-110K dataset. The SKU-110K dataset is a large-scale dataset for stock keeping unit (SKU) detection. The dataset contains 111,634 images with 1,128,246 annotated objects. The dataset is divided into 85,134 images for training, 11,510 images for validation, and 15,990 images for testing. The dataset contains 110 classes of products. The dataset is available at [SKU-110K]

### This repository contains the notebook along with the training and validation data files for the SKU-110K dataset.

### The repository contains the following files and folders:

1. `SKU-110K_YOLOv8.ipynb`: This is the main notebook that contains the implementation of the YOLOv8 object detection model on the SKU-110K dataset. The notebook contains the code for loading the dataset, training the model, and evaluating the model on the test data.

2. `runs\detect\weights\best_saved_model\best_float32.pt`: This is the best model weights file that is saved during the conversion process from pytorch to tflite. The model weights file is saved in the `runs\detect\weights\best_saved_model` folder:

3. `YOLOv8-TfLite-Object-Detector`: This folder contains a sample application that runs the customs trained tflite model on the SKU-110K dataset. The application is built using the TensorFlow Lite library and is used to detect objects in images.

### Developer: [Aneeq Malik]

