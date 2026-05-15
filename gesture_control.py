import cv2
import mediapipe as mp
import numpy as np
import pickle
import paho.mqtt.client as mqtt

# MQTT setup
client = mqtt.Client("gesture_pc_client")
client.connect("broker.hivemq.com", 1883, 60)
client.loop_start()

def send(device, action):
    client.publish(f"home/{device}", action)
    print(f"📤 Sent: {device} {action}")

# Load model
model = pickle.load(open("gesture_model.pkl", "rb"))

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.append(lm.x)
                landmarks.append(lm.y)

            if len(landmarks) == 42:
                gesture = str(model.predict([landmarks])[0]).lower()

                print("🤚 Gesture:", gesture)

                # 🔥 MQTT CONTROL
                if gesture == "light_on":
                    send("light", "ON")

                elif gesture == "light_off":
                    send("light", "OFF")

                elif gesture == "fan_on":
                    send("fan", "ON")

                elif gesture == "fan_off":
                    send("fan", "OFF")

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()