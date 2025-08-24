# Dockerfile

FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg libsm6 libxext6 libglib2.0-0 libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install opencv-python-headless

WORKDIR /app

COPY app.py .

# Create output folder
RUN mkdir -p /output

# Healthcheck based on heartbeat file
HEALTHCHECK --interval=10s --timeout=3s \
  CMD test -f /tmp/heartbeat && find /tmp/heartbeat -mmin -1 || exit 1

CMD ["python", "app.py"]
