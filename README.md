# AI-Powered Akhand Jyot Monitoring System

## 🔥 Purpose
The **AI-Powered Akhand Jyot Monitoring System** is designed to provide **continuous, real-time monitoring** of an Akhand Jyot, ensuring its **uninterrupted presence** during religious observances like Navratri. By utilizing **computer vision and AI-powered detection**, the system helps in:
- Detecting **low flame levels**
- Monitoring **ghee levels** in the deepak
- Identifying **shaky or flickering flames**
- Notifying the user about **any potential risks** that could extinguish the Jyot

A **spare phone** is used as a live streaming camera via **DroidCam**, while an AI model running on a **Windows 11 laptop** analyzes the feed and sends **real-time alerts** via **WhatsApp**.

---

## 🚀 Features
### ✅ **Live Streaming System** *(Completed & Optimized)*
- **Fluent, low-latency video stream** accessible by multiple users simultaneously.
- **Auto-reconnect mechanism** when DroidCam stops or loses connection.
- **Error frame display** when the stream is disconnected.
- **Professional UI** with a fullscreen mode for better visualization.
- **Multi-user access** (supports **10+ concurrent users** via Flask).

### 🛠 **AI-Powered Monitoring System** *(Under Development)*
- **Flame Detection:** Notifies when the flame is **too low**.
- **Shaky Flame Warning:** Detects **abnormal flickering** caused by wind or disturbances.
- **Ghee Level Monitoring:** Alerts when the **ghee level drops below half**.
- **Danger Prediction:** AI-based detection of objects or conditions **that may threaten the Jyot**.
- **Automated WhatsApp Notifications:** Sends alerts in **background mode** without opening the WhatsApp tab.

---

## 🛠 Enhancements for a **Fluent Live Stream**
### 🔄 **Auto-Reconnect Mechanism**
- **Detects DroidCam disconnection** and **automatically reconnects** when it comes back online.
- **Releases stale camera connections** to prevent memory leaks.
- **Waits 3 seconds before retrying** to avoid excessive reconnection attempts.

### 🎥 **Optimized Video Processing**
- **Frame locking mechanism** ensures smooth and stable streaming.
- **Flask-based MJPEG streaming** for **low latency**.
- **Custom error frames** for when the camera feed is unavailable.

### 🌐 **Multi-User Support**
- Users can access the stream via a **web browser**.
- **Threaded Flask Server** allows multiple devices to view the Jyot live stream **simultaneously**.

---

## 🔧 Installation & Setup
### **1️⃣ Install Dependencies**
Ensure **Python 3.12+** is installed, then run:
```sh
pip install opencv-python numpy flask flask_cors pywhatkit
```

### **2️⃣ Set Up DroidCam**
1. **Install DroidCam App** on your **Android phone**.
2. **Connect via WiFi** and **note the camera URL** (e.g., `http://192.168.1.4:4747/video`).
3. Keep the phone **mounted on a tripod**, facing the **Akhand Jyot**.

### **3️⃣ Run the Live Stream Server**
```sh
python live_stream.py
```
Visit `http://127.0.0.1:5000` in your browser to view the stream.

---

## 🏗 Upcoming Enhancements
🚀 **AI-Driven Monitoring System:**
- **Deep learning model** for enhanced flame and object detection.
- **More advanced danger predictions**.
- **Cloud-based storage** for event logs and alert history.

---

## 📜 Credits
Developed by **Badal Harit** to ensure the uninterrupted presence of Akhand Jyot with modern AI-powered monitoring. 🙏🔥

