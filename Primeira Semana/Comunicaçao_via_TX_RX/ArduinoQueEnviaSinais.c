int simulated_humidity;

bool is_irrigating = false;
bool waiting_response = false;

unsigned long irrigation_start;
unsigned long irrigation_time;
unsigned long real_time;

String sensor_response;

void setup() {
  Serial.begin(9600);
}

void loop() {
  
  if (Serial.available()) {
     sensor_response = Serial.readStringUntil('\n');

    if (sensor_response.startsWith("L:")) {
      irrigation_time = sensor_response.substring(2).toInt();
      irrigation_start = millis();
      is_irrigating = true;
    }

    if (sensor_response.startsWith("D")) {
      is_irrigating = false;
    }
  }
  
  if (!is_irrigating) {
    simulated_humidity = random(0, 100);
    Serial.print("S:");
    Serial.println(simulated_humidity);
  }

  if (is_irrigating) {
    real_time = millis() - irrigation_start;
    
    if (real_time >= irrigation_time) {
      simulated_humidity = 0; 
      is_irrigating = false;
      Serial.print("S:");
      Serial.println(simulated_humidity);
      delay(real_time);
    }
  }

  delay(1000);
}
