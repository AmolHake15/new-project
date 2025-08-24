# AI RTSP Simple (Face Detection Demo)

- Connects to RTSP (falls back to webcam if RTSP fails)
- Detects faces with OpenCV’s Haar cascade
- Saves annotated frames to `./output`
- Logs connection status, dropped frames, and inference time

## Run
```bash
# Linux/macOS:
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
RTSP_URL="rtsp://…" python app.py

# Windows (PowerShell):
py -m venv .venv; .\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
$env:RTSP_URL="rtsp://…"; py app.py
