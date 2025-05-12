from ultralytics import YOLO
import torch

def main():
    # Clear unused GPU memory
    torch.cuda.empty_cache()

    # Load YOLOv8 nano model (smallest, fastest option)
    model = YOLO("yolov8n.pt")

    # Train the model with reduced settings
    model.train(
        data="D:/python/openCV/ocr/model/data.yaml",
        epochs=10,          # reduced from 50 to 10
        imgsz=416,          # smaller image size to reduce memory usage
        batch=8,            # smaller batch size to fit GPU
        device="cuda",      # use GPU
        amp=True,           # enable mixed precision
        workers=2,          # lower dataloader workers for stability
        name="train_test"
    )

if __name__ == "__main__":
    main()
