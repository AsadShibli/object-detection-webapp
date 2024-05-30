# Flask Video Object Detection

This repository contains a Flask web application that processes video files for object detection using YOLOv8 and displays a message upon successful processing.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [APP Demo](#app-demo)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Project Overview
This project demonstrates how to use a Flask web application to upload video files, process them using YOLOv8 for object detection, and provide feedback to the user once the processing is complete. The processed videos are saved to a specified folder, and the user is informed to check the folder after the processing is done.

## Features
- Upload video files (supports `.mp4`, `.avi`, `.mov`, `.mkv` formats)
- Process videos using YOLOv8 for object detection
- Save processed videos to a specified folder
- Inform the user once processing is complete

## APP Demo

![demo1](https://github.com/AsadShibli/object-detection-webapp/assets/119102237/3ac6f5d3-315c-46a7-aab0-16f7f793bee2)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AsadShibli/object-detection-webapp.git
    cd object-detection-webapp
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the YOLOv8 model:**
    When you run the app, the `yolov8l.pt` model file will be downloaded in your project directory.

## Usage

1. **Run the Flask application:**
    ```bash
    python app.py
    ```

2. **Open your web browser and go to:**
    ```
    http://127.0.0.1:5000/
    ```

3. **Upload a video file:**
    - Click on "Choose File" and select a video file.
    - Click on the "Upload" button.
    - Wait for the processing to complete.
    - You will see a message indicating that the file processing is completed and to check the `processed` folder.

## Folder Structure

```
object-detection-webapp/
├── uploads/
│ └── (uploaded videos)
├── processed/
│ └── (processed videos)
├── templates/
│ └── index.html
├── app.py
├── requirements.txt
├── README.md
```

## Dependencies

- Flask==3.0.3
- ultralytics==8.2.24
- supervision==1.0.0
- opencv-python==4.9.0.80
- numpy==1.26.4

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bugs, feature requests, or improvements.

1. **Fork the repository.**
2. **Create a new branch:**
    ```bash
    git checkout -b feature-branch-name
    ```
3. **Make your changes and commit them:**
    ```bash
    git commit -m 'Add new feature'
    ```
4. **Push to the branch:**
    ```bash
    git push origin feature-branch-name
    ```
5. **Submit a pull request.**
