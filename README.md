# **Project Description**

This project uses YOLOv8 for real-time detection of cars and their number plates in video streams. It integrates object detection, tracking, and optical character recognition (OCR) to automatically identify vehicles, track their movement, and extract and display license plate information from detected number plates. The pipeline also interpolates missing detections for smoother visualization.

---

## **How to Run the Project**

1. **Run the main detection/tracking script**  
   Detects cars and number plates, tracks vehicles, and extracts license plate text.  
   _Output: Generates `test.csv` with detection and recognition results._

2. **Run `add_missing_data.py`**  
   Fills in any missing detection data by interpolating between frames.  
   _Output: Generates `test_interpolated.csv` with interpolated results._

3. **Run `visualize.py`**  
   Visualizes the results by drawing bounding boxes and displaying license plate information on the video.  
   _Output: Generates `out.mp4` as the annotated output video._

---

Make sure to follow this order for correct results!
