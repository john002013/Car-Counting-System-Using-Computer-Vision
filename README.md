# Computer Vision Based Car counting System For Road Construction and Maintenance Evaluation.
Real-time vehicle counting system for traffic analysis and road planning.

# Overview 📌

This project implements a computer vision–based vehicle counting system designed to detect and count cars, trucks, buses and lorries passing through a particular road segment.

Using object detection and lane-based region tracking, the system processes live or recorded video footage and keeps track of vehicle types and their total count over time.

This project demonstrates how AI can assist transportation engineers, civil engineers and smart-city developers in analyzing road usage and improving infrastructure planning.

# Purpose of the Project 🎯 

The main goal of this system is to determine the number of vehicles passing through a specific road within a given time period. This information is extremely valuable in real-world applications such as:

1. Road Construction Planning

Before repairing, expanding, or reconstructing a road, engineers must understand traffic density. This system gives accurate data on how many vehicles use the road daily.

2. Road Maintenance Evaluation

Heavily used roads wear out faster. Counting vehicle categories (cars vs heavy trucks) helps estimate load stress and determine maintenance frequency.

3. Traffic Analysis & Monitoring

Useful for detecting congestion patterns, peak hours, and traffic flow behavior.

4. Smart Transportation Systems

Forms the base for future real-time monitoring systems in smart cities.

# Features 🚀 

1. Counts multiple vehicle types: Cars, Trucks, Lorries and Buses
2. Works with live camera feed or pre-recorded video
3. Tracks vehicle movement across defined regions
4. Logs total count per category
5. Lightweight and works in real-time with a Fine-Tuned Yolo Model Trained to meet this need
6. Customizable for different lanes, camera angles, or locations
7. Option to save processed video with detection boxes

# Tech Stack 🛠️ 

1. Python
2. OpenCV
3. YOLOv8n and YOLOv8m
4. NumPy
5. Video Processing Pipeline
6. Sort for trackingHow It Works
   
# How It Works
1. The system loads the detection model (YOLOv8n or YOLOv8m).
2. Each frame from the video feed is analyzed.
3. Vehicles are detected and classified into categories.
4. A “counting line” or zone is defined in the frame.
5. When a vehicle crosses the line, it is counted.
6. Counts are stored and displayed on the screen.

# Author 👨🏾‍💻 

John Babalola
Computer Vision | Robotics | Embedded Systems | Embodied AI
   

