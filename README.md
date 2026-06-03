# 🚗 Auto-Insure AI: Smart Vehicle Damage Detection

## Overview

Auto-Insure AI is an AI-powered vehicle inspection system that automates the identification of visible vehicle damage from images. Built using YOLOv8 and Streamlit, the application assists insurance companies and repair centers by providing rapid preliminary damage assessment and repair prioritization.

The system analyzes uploaded vehicle images, detects damage-related anomalies, calculates confidence scores, and classifies cases into repair priority levels.


## Problem Statement
Manual vehicle inspections can be time-consuming, inconsistent, and costly. Insurance providers often need a quick preliminary assessment before assigning adjusters or approving claims.
This project demonstrates how computer vision can streamline the inspection process by:
* Detecting visible vehicle damage automatically
* Providing instant diagnostic feedback
* Prioritizing cases based on damage severity
* Supporting faster insurance claim triaging


## Features
### AI-Based Damage Detection
* Utilizes YOLOv8 for real-time object detection.
* Identifies visible anomalies in uploaded vehicle images.

### Damage Analytics
* Counts detected damage regions.
* Calculates average confidence score of detections.

### Priority Assessment
* High Priority: Significant damage or highly confident detections.
* Low Priority: Minor cosmetic damage.

### Interactive Dashboard
* User-friendly Streamlit interface.
* Visualized detection results with bounding boxes.
* Detailed diagnostic report for each detection.

### Insurance-Oriented Workflow
* Designed to simulate automated insurance inspection and claim triaging systems.


## Tech Stack
* Python
* Streamlit
* YOLOv8 (Ultralytics)
* Computer Vision
* Pillow (PIL)



## System Workflow
1. User uploads a vehicle image.
2. YOLOv8 processes the image.
3. Damage regions are detected.
4. Confidence scores are calculated.
5. Damage severity is evaluated.
6. Results are displayed through an interactive dashboard.


## Sample Output
The application provides:
* Vehicle image with detected damage highlighted
* Number of anomalies detected
* Confidence score
* Damage priority assessment
* Detailed detection report


## Skills Demonstrated

* Machine Learning
* Computer Vision
* Deep Learning
* Object Detection
* Streamlit Application Development
* Model Integration
* Data Visualization
* AI Product Development


Aspiring Data Scientist / Machine Learning Engineer passionate about building AI-powered solutions for real-world business problems.
