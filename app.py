import cv2
import os
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Output directory
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# RTSP / webcam stream
# Replace with your RTSP URL if you have one
RTSP_URL = 0  # 0 = default webcam

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def main():
    logging.info("Starting video stream...")
    cap = cv2.VideoCapture(RTSP_URL)

    if not cap.isOpened():
        logging.error("Failed to open video stream.")
        return

    frame_count = 0
    saved_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            logging.warning("Failed to grab frame.")
            break

        start_time = time.time()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                frame,
                "face",
                (x, max(0, y - 5)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                1,
                cv2.LINE_AA
            )

        inference_time = time.time() - start_time
        logging.info(f"Frame {frame_count}: {len(faces)} face(s) detected - inference {inference_time:.3f}s")

        # Save only a few frames
        if saved_frames < 5:
            frame_path = os.path.join(OUTPUT_DIR, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_path, frame)
            saved_frames += 1
            logging.info(f"Saved {frame_path}")

        frame_count += 1

        # Break after some frames for testing
        if frame_count > 50:
            break

    cap.release()
    logging.info("Stream ended.")

if __name__ == "__main__":
    main()

