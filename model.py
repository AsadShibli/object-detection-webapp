import cv2
from ultralytics import YOLO, solutions
import supervision as sv

model = YOLO("yolov8l.pt")
names = model.model.names

cap = cv2.VideoCapture("53125-472583428_small.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Video writer
video_writer = cv2.VideoWriter("speed_estimation.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))


while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    result = model(im0)[0]
    detections = sv.Detections.from_ultralytics(result)

    detections['names'] = [
        model.model.names[class_id]
        for class_id
        in detections.class_id
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
