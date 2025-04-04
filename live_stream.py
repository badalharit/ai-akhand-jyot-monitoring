import cv2
import threading
import flask
from flask import Flask, Response, render_template
from flask_cors import CORS
import time
import numpy as np

# Initialize Flask App
app = Flask(__name__)
CORS(app)

# 🔥 Replace with your DroidCam IP
CAMERA_URL = "http://192.168.1.2:4747/video"

# Global Variables
frame = None
lock = threading.Lock()
stop_thread = False
is_camera_connected = True
cap = None  # Store camera object

# Adjust FPS for smoother performance
FPS_LIMIT = 30  # Lower = Less Lag

def generate_error_frame():
    """Generate a frame with 'Camera Disconnected' message."""
    error_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    cv2.putText(error_frame, "Camera Disconnected", (100, 240),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    return error_frame

def capture_video():
    """Continuously fetch frames, auto-reconnect if camera stops."""
    global frame, stop_thread, is_camera_connected, cap

    while not stop_thread:
        try:
            if cap is None or not cap.isOpened():
                print("[⚠️] Connecting to DroidCam...")
                cap = cv2.VideoCapture(CAMERA_URL)
                time.sleep(2)  # Allow some time for connection

            ret, new_frame = cap.read()

            if not ret:
                print("[❌] No Frames Received! Retrying...")
                is_camera_connected = False
                frame = generate_error_frame()

                # **Release & Reconnect after 3 seconds**
                cap.release()
                cap = None
                time.sleep(3)
                continue

            with lock:
                frame = new_frame
                is_camera_connected = True

        except Exception as e:
            print(f"[❌] Error: {e}")
            frame = generate_error_frame()
            is_camera_connected = False
            time.sleep(3)  # Retry after 3 seconds

    if cap:
        cap.release()  # Release when stopping

def generate_frames():
    """Stream frames with low latency."""
    global frame
    while True:
        with lock:
            if frame is None:
                continue
            
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# Start Video Capture Thread
stream_thread = threading.Thread(target=capture_video, daemon=True)
stream_thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop_stream')
def stop_stream():
    """Stop the video stream properly."""
    global stop_thread
    stop_thread = True
    return "Stream Stopped"

# Run Flask App
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
    except KeyboardInterrupt:
        stop_thread = True
