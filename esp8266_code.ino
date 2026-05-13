#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// 🔐 WiFi
const char* ssid = "testwifi";
const char* password = "12345678";

// 🌐 MQTT
const char* mqtt_server = "broker.hivemq.com";

WiFiClient espClient;
PubSubClient client(espClient);

// 🔌 Pins
#define LIGHT_PIN D5
#define FAN_PIN   D6

// 📶 WiFi Connect
void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to WiFi: ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\n✅ WiFi Connected");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

// 📩 MQTT Callback
void callback(char* topic, byte* payload, unsigned int length) {

  String msg = "";
  for (int i = 0; i < length; i++) {
    msg += (char)payload[i];
  }

  msg.trim();
  msg.toLowerCase();

  Serial.print("📩 ");
  Serial.print(topic);
  Serial.print(" → ");
  Serial.println(msg);

  // 💡 LIGHT CONTROL
  if (String(topic) == "home/light") {

    if (msg == "on") {
      digitalWrite(LIGHT_PIN, LOW);   // relay ON
      Serial.println("💡 Light ON");
    }

    else if (msg == "off") {
      digitalWrite(LIGHT_PIN, HIGH);  // relay OFF
      Serial.println("💡 Light OFF");
    }
  }

  // 🌀 FAN CONTROL
  else if (String(topic) == "home/fan") {

    if (msg == "on") {
      digitalWrite(FAN_PIN, LOW);
      Serial.println("🌀 Fan ON");
    }

    else if (msg == "off" || msg == "of") {
      digitalWrite(FAN_PIN, HIGH);
      Serial.println("🌀 Fan OFF");
    }
  }
}

// 🔄 MQTT Reconnect
void reconnect() {

  while (!client.connected()) {

    Serial.print("Connecting MQTT...");

    String clientId = "ESP-" + String(ESP.getChipId());

    if (client.connect(clientId.c_str())) {

      Serial.println("✅ MQTT Connected");

      client.subscribe("home/light");
      client.subscribe("home/fan");

    } else {
      Serial.print("❌ Failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

// 🚀 SETUP
void setup() {

  Serial.begin(115200);

  pinMode(LIGHT_PIN, OUTPUT);
  pinMode(FAN_PIN, OUTPUT);

  // 🔥 Safe default OFF
  digitalWrite(LIGHT_PIN, HIGH);
  digitalWrite(FAN_PIN, HIGH);

  setup_wifi();

  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

// 🔁 LOOP
void loop() {

  if (!client.connected()) {
    reconnect();
  }

  client.loop();
}
