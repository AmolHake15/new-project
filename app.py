import cv2
import logging
import time
import os

logging.basicConfig(level=logging.INFO)


def detect_faces(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return frame, faces


def main():
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    # Use RTSP or 0 for webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        logging.error("Failed to connect to camera or stream.")
        return

    logging.info("Successfully connected to video stream.")

    frame_count = 0

    while frame_count < 10:
        ret, frame = cap.read()
        if not ret:
            logging.warning("Dropped frame")
            continue

        start_time = time.time()
        annotated_frame, faces = detect_faces(frame, face_cascade)
        inference_time = time.time() - start_time

        logging.info(
            f"Saved frame {frame_count} with {len(faces)} faces detected "
            f"in {inference_time:.3f} seconds"
        )

        output_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")
        cv2.imwrite(output_path, annotated_frame)

        frame_count += 1

    cap.release()


if __name__ == "__main__":
    main()
