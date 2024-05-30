import os
import cv2
from flask import Flask, request, redirect, url_for, render_template
from ultralytics import YOLO
import supervision as sv

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'avi', 'mov', 'mkv'}

model = YOLO("yolov8l.pt")
names = model.model.names

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        process_video(filepath, filename)
        message = "File processing is completed! Please check the processed folder."
        return render_template('index.html', message=message)
    else:
        return "Invalid file type"

def process_video(filepath, filename):
    cap = cv2.VideoCapture(filepath)
    assert cap.isOpened(), "Error reading video file"
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

    output_path = os.path.join(app.config['PROCESSED_FOLDER'], filename)
    video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            break

        result = model(im0)[0]
        detections = sv.Detections.from_ultralytics(result)

        detections['names'] = [
            model.model.names[class_id]
            for class_id in detections.class_id
        ]

        triangle_annotator = sv.TriangleAnnotator()
        label_annotator = sv.LabelAnnotator(text_position=sv.Position.CENTER)
        annotated_frame = triangle_annotator.annotate(
            scene=im0.copy(),
            detections=detections
        )
        annotated_frame = label_annotator.annotate(
            scene=annotated_frame.copy(),
            detections=detections
        )
        video_writer.write(annotated_frame)

    cap.release()
    video_writer.release()

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    if not os.path.exists(app.config['PROCESSED_FOLDER']):
        os.makedirs(app.config['PROCESSED_FOLDER'])
    app.run(debug=True)
