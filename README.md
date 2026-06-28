# ML-BASED-HOME-AUTOMATION-SYSTEM


An IoT-based Smart Home Automation System that allows users to control home appliances using **Voice Commands**, **Hand Gestures**, and **Manual Switches** through a Flutter mobile application. The project integrates ESP8266, MQTT, Machine Learning, and Computer Vision to provide a seamless smart home experience.

---

##  Features

-  Control lights and fans remotely
-  Voice-based appliance control
-  Hand Gesture Recognition using Machine Learning
-  Flutter Mobile Application
-  MQTT-based real-time communication
-  ESP8266 NodeMCU as IoT Controller
-  Manual switch control from the app
-  Works over the Internet using MQTT Broker

---

##  Technologies Used

- Flutter (Mobile App)
- Python
- Flask
- OpenCV
- MediaPipe
- Scikit-learn (Random Forest Classifier)
- ESP8266 NodeMCU
- MQTT Protocol
- HiveMQ Public Broker
- Arduino IDE

---

##  Project Structure

```
Smart-Home-Automation/
│
├── Flutter_App/
│   ├── lib/
│   └── pubspec.yaml
│
├── ESP8266_Code/
│   └── esp8266_code.ino
│
├── Python_Server/
│   ├── server.py
│   ├── gesture_control.py
│   ├── train_model.py
│   ├── collect_data.py
│   ├── gesture_model.pkl
│   └── dataset.csv
|   └── predict_gesture.py
│
├── README.md
```

---

##  Working

1. The Flutter application allows users to control appliances through Voice, Gesture, or Manual Switches.
2. For gesture control, the app captures an image and sends it to the Flask server.
3. The Flask server processes the image using MediaPipe to extract hand landmarks.
4. A Random Forest Machine Learning model predicts the gesture.
5. The server publishes MQTT commands to the ESP8266.
6. ESP8266 receives the commands and controls the relay module connected to the appliances.

---

##  Hardware Components

- ESP8266 NodeMCU
- 4-Channel Relay Module
- LEDs / Bulbs
- DC Fan
- Power Supply
- Breadboard
- Jumper Wires

---

##  Machine Learning

- Hand landmark extraction using MediaPipe
- Dataset collection using OpenCV
- Random Forest Classifier for gesture recognition
- Supports gestures such as:
  - Light ON
  - Light OFF
  - Fan ON
  - Fan OFF

---

## 📱 Mobile Application

The Flutter application provides:

- Voice Control
- Gesture Control
- Manual Switch Control
- Real-time appliance management

---

## 📡 Communication Flow

```
Flutter App
      │
      ▼
 Flask Server
      │
MediaPipe + ML Model
      │
      ▼
 MQTT Broker (HiveMQ)
      │
      ▼
 ESP8266 NodeMCU
      │
      ▼
 Relay Module
      │
      ▼
 Home Appliances
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Smart-Home-Automation.git
```

### Install Python Dependencies

```bash
pip install flask opencv-python mediapipe scikit-learn numpy pandas paho-mqtt
```

### Run Flask Server

```bash
python server.py
```

### Upload ESP8266 Code

Upload the Arduino sketch using Arduino IDE.

### Run Flutter App

```bash
flutter pub get
flutter run
```

---

## 📈 Future Improvements

- Face Recognition Authentication
- Home Automation Dashboard
- Firebase Cloud Integration
- Appliance Scheduling
- Energy Consumption Monitoring
- Multiple Room Support
- Smart Sensors Integration

---

##  Team

Team Size: **3 Members**

This project was developed as part of an IoT and Machine Learning based Smart Home Automation system.

---

