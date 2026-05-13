from flask import Flask, request, jsonify
import cv2
import numpy as np
import pickle
import mediapipe as mp
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT setup
client = mqtt.Client(client_id="gesture_server_client", protocol=mqtt.MQTTv311)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ MQTT Connected")
    else:
        print("❌ MQTT Failed")

client.on_connect = on_connect
client.connect("broker.hivemq.com", 1883, 60)
client.loop_start()

def send(device, action):
    client.publish(f"home/{device}", action)
    print(f"📤 Sent: {device} {action}")

# Load model
model = pickle.load(open("gesture_model.pkl", "rb"))

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

@app.route('/')
def home():
    return "Server running 🚀"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files.get('image')

        if file is None:
            return jsonify({"gesture": "no_image"})

        npimg = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        if img is None:
            return jsonify({"gesture": "invalid_image"})

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:

            hand_landmarks = results.multi_hand_landmarks[0]

            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.append(lm.x)
                landmarks.append(lm.y)

            if len(landmarks) == 42:

                prediction = str(model.predict([landmarks])[0]).lower()

                print("🤚 Gesture:", prediction)

                # 🔥 MQTT CONTROL
                if prediction == "light_on":
                    send("light", "ON")

                elif prediction == "light_off":
                    send("light", "OFF")

                elif prediction == "fan_on":
                    send("fan", "ON")

                elif prediction == "fan_off":
                    send("fan", "OFF")

                return jsonify({"gesture": prediction})

        return jsonify({"gesture": "none"})

    except Exception as e:
        print("Error:", e)
        return jsonify({"gesture": "error"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)