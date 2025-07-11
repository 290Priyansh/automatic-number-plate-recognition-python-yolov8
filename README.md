# **Automatic Number Plate Recognition (ANPR) with YOLOv8**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-FF0000?style=for-the-badge&logo=yolo&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338D?style=for-the-badge&logo=opencv&logoColor=white)
![PyTesseract](https://img.shields.io/badge/PyTesseract-F80000?style=for-the-badge&logo=tesseract&logoColor=white)

---

## **📝 Description**

This project implements an **Automatic Number Plate Recognition (ANPR)** system using **YOLOv8** for efficient license plate detection and **Python** for image processing and optical character recognition (OCR).

ANPR is a technology that uses image processing to read vehicle registration plates. This system is designed to identify and extract text from license plates in images or video streams, providing a robust solution for various applications such as traffic monitoring, parking management, security systems, and toll collection.

By leveraging the power of YOLOv8, a state-of-the-art object detection model, the system accurately locates license plates even in challenging conditions, followed by advanced image processing techniques and OCR to extract the alphanumeric characters.

---

## **✨ Features**

* **Accurate License Plate Detection:** Utilizes YOLOv8 for precise and fast detection of number plates in diverse environments.
* **Optical Character Recognition (OCR):** Integrates with an OCR engine (e.g., Tesseract) to convert detected plate images into readable text.
* **Image Preprocessing:** Includes steps like grayscale conversion, blurring, and thresholding to enhance character readability for OCR.
* **Bounding Box Visualization:** Displays bounding boxes around detected license plates and recognized text for clear visualization.
* **Modular Codebase:** Designed with clear functions for easy understanding, modification, and extension.
* **Real-time Potential:** Optimized for performance, making it suitable for real-time video stream processing (depending on hardware).

---

## **🛠️ Technologies Used**

* **Python 3.x:** The primary programming language.
* **YOLOv8 (Ultralytics):** For object detection (specifically, detecting license plates).
* **OpenCV (`cv2`):** For image and video processing tasks.
* **NumPy:** For numerical operations, especially array manipulation.
* **PyTesseract:** Python wrapper for Google's Tesseract-OCR Engine (for character recognition).
* **Pillow (PIL Fork):** Used by PyTesseract for image handling.
* **Matplotlib:** For plotting and visualization (optional, for debugging/analysis).
* **PyTorch:** The deep learning framework that YOLOv8 is built upon.

---

---
