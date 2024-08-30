# Object Defect Detection using YOLO
This project is designed to detect six types of defects in images using the YOLO model.

## How to Run

1. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Train the model:
   ```
   python scripts/train.py
   ```

3. Detect defects in an image:
   ```
   python scripts/detect.py
   ```

## Project Structure

- `data/`: Contains the training and testing images along with their labels.
- `models/`: Contains the trained model.
- `scripts/`: Contains the training and detection scripts.
- `config.yaml`: Configuration file for the YOLO model.
- `requirements.txt`: List of required dependencies.
    