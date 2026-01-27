int pin = 13;
String data_logger_response; 

void setup() {
  Serial.begin(9600);
  pinMode(pin, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    data_logger_response = Serial.readStringUntil('\n');

    if (data_logger_response.startsWith("S:")) {
      int water_need = data_logger_response.substring(2).toInt();

      if (water_need == 0) {
        digitalWrite(pin, LOW);
        Serial.println("D:0");
      } 
      else {
        int irrigation_time = water_need * 20;
        digitalWrite(pin, HIGH);
        Serial.print("L:");
        Serial.println(irrigation_time);
        
        delay(irrigation_time);
      }
    }
  }
}