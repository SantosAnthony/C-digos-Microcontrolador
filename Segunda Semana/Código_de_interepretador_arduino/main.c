#include <SPI.h>
#include <SD.h>
#include <RTClib.h>

const int pinoCS = 4;
const int PinoRele = 7;

RTC_DS1307 rtc;
File arquivo;

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ;
  }
  pinMode(PinoRele, OUTPUT);
  digitalWrite(PinoRele, LOW);

  if (!rtc.begin()) {
    while (1);
  }

  if (!rtc.isrunning()) {
    rtc.adjust(DateTime(F(_DATE), F(TIME_)));
  }

  if (!SD.begin(pinoCS)) {
    while (1);
  }
}

void loop() {
    verificarAgenda();
    delay(60000);
}

void verificarAgenda() {
  DateTime agora = rtc.now();
  
  char dataHoje[11]; 
  sprintf(dataHoje, "%02d/%02d/%04d", agora.day(), agora.month(), agora.year());
  
  char horaAgora[6];
  sprintf(horaAgora, "%02d:%02d", agora.hour(), agora.minute());

  arquivo = SD.open("dados.csv");
  if (!arquivo) {
    Serial.println("Erro ao abrir dados.csv");
    return;
  }

  char bufferLinha[100];
  bool encontrouHoje = false;

  while (arquivo.available()) {
    int len = arquivo.readBytesUntil('\n', bufferLinha, 99);
    bufferLinha[len] = '\0';

    char* token = strtok(bufferLinha, ";");
    
    if (!token) continue; 

    if (strcmp(token, dataHoje) == 0) {
      encontrouHoje = true;

      for (int i = 1; i <= 4; i++) {
        char* horaInicio = strtok(NULL, ";");
        char* duracaoStr = strtok(NULL, ";");

        if (horaInicio && duracaoStr) {
          if (strcmp(horaInicio, horaAgora) == 0) {
            int tempoRega = atoi(duracaoStr);
            if (tempoRega > 0) {
              arquivo.close(); 
              
              executarRega(tempoRega);
              return;
            }
          }
        }
      }
      break; 
    }
  }
  arquivo.close();
}

void executarRega(int minutos) {
  digitalWrite(PinoRele, HIGH);
  unsigned long tempoMs = minutos * 60000UL;
  
  delay(tempoMs);
  
  digitalWrite(PinoRele, LOW);
}