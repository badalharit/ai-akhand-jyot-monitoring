import cv2
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# 📷 DroidCam IP
CAMERA_URL = "http://192.168.1.4:4747/video"

# 📲 Your WhatsApp Number
WHATSAPP_NUMBER = "+919xxxxxxxxx"

# 🚀 Setup Selenium for WhatsApp Web
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--log-level=3")  # Reduce logs
options.add_argument("--disable-dev-shm-usage")

# Start Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open WhatsApp Web & Scan QR Code Once
driver.get("https://web.whatsapp.com")
input("Scan the QR code in WhatsApp Web, then press Enter...")

# 📢 Function to Send WhatsApp Message in Background
def send_whatsapp_alert(message):
    try:
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@title="Search input textbox"]')
        search_box.send_keys(WHATSAPP_NUMBER)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@title="Type a message"]')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

        print("[✅] WhatsApp Alert Sent!")
    except Exception as e:
        print("[❌] WhatsApp Error:", e)

# 🔥 Improved Flame & Motion Detection
def detect_jyot_issues():
    cap = cv2.VideoCapture(CAMERA_URL)

    last_flame_alert = 0
    last_motion_alert = 0
    last_ghee_alert = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("[❌] Error: Unable to fetch video feed.")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        # 🔥 Flame Size Check (Reduce Sensitivity)
        flame_area = np.sum(threshold == 255)
        if flame_area < 3000:  # Increased threshold to reduce false alerts
            if time.time() - last_flame_alert > 60:  # Avoid multiple alerts
                print("[⚠️] Alert: Flame is too low!")
                send_whatsapp_alert("⚠️ Akhand Jyot Warning: Flame is too low!")
                last_flame_alert = time.time()

        # 💨 Improved Motion Detection
        diff = cv2.absdiff(threshold, cv2.GaussianBlur(threshold, (9, 9), 0))
        motion_score = np.sum(diff)

        if motion_score > 50000:  # Increased threshold to reduce false alerts
            if time.time() - last_motion_alert > 60:
                print("[⚠️] Alert: Flame is flickering abnormally!")
                send_whatsapp_alert("⚠️ Akhand Jyot Warning: Flame is shaking abnormally!")
                last_motion_alert = time.time()

        # 🛢️ Improved Ghee Level Detection
        deepak_region = frame[-100:, :]
        avg_brightness = np.mean(cv2.cvtColor(deepak_region, cv2.COLOR_BGR2GRAY))

        if avg_brightness > 180:  # Adjusted brightness threshold
            if time.time() - last_ghee_alert > 120:  # Avoid repeated alerts
                print("[⚠️] Alert: Ghee level is low!")
                send_whatsapp_alert("⚠️ Akhand Jyot Warning: Ghee is running low!")
                last_ghee_alert = time.time()

        # 📺 Display Video
        cv2.imshow("Akhand Jyot Monitoring", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# 🔥 Start Monitoring
detect_jyot_issues()
