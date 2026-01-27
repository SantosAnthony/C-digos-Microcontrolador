#include <Wire.h>
#include <RTClib.h>

RTC_DS1307 rtc;

const int PINO_RELE = 7; 

// --- VARIÁVEIS PARA O TEMPORIZADOR ---
unsigned long ultimaRegaAleatoria = 0;
unsigned long intervaloAtualSorteado = 0; // Armazena o tempo alvo (em milissegundos)

void setup() {
  pinMode(PINO_RELE, OUTPUT);
  digitalWrite(PINO_RELE, LOW); // Garante sistema desligado ao iniciar

  Serial.begin(9600);

  // --- INICIALIZAÇÃO DO HARDWARE ---
  if (!rtc.begin()) {
    // Se falhar, avisa e trava o sistema para não rodar sem relógio
    Serial.println("ERRO CRÍTICO: Relógio (RTC) não encontrado!");
    while (1);
  }

  // Se o relógio perdeu a energia, ajusta para a hora da compilação
  if (!rtc.isrunning()) {
    Serial.println("RTC parado. Ajustando horário...");
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  }

  // --- INICIALIZAÇÃO DA ALEATORIEDADE ---
  // Usa o ruído elétrico da porta A1 vazia para criar uma semente única
  randomSeed(analogRead(A1)); 
  
  // 1. PRIMEIRO SORTEIO (Setup):
  // Define um intervalo entre 1 e 5 minutos (60.000ms a 300.000ms)
  // Isso evita que a rega ligue imediatamente ao conectar na tomada
  intervaloAtualSorteado = random(0, 60001);  // ajustado para apresentação

  Serial.println("--- SISTEMA DE IRRIGAÇÃO INICIADO ---");
  Serial.print(">>> Aguardando primeiro intervalo de: ");
  Serial.print(intervaloAtualSorteado / 1000); // Converte ms -> min
  Serial.println(" minutos.");
}

void loop() {
  DateTime agora = rtc.now();
  unsigned long tempoAtual = millis();

  // --- REGRA 1: SISTEMA ALEATÓRIO ---
  // Verifica se o tempo decorrido é maior que o número sorteado
  if (tempoAtual - ultimaRegaAleatoria >= intervaloAtualSorteado) {
    
    Serial.println("[AUTO] Tempo aleatório atingido! Iniciando rega...");
    
    // Executa rega por 5 SEGUNDOS
    // (Engenharia: Usamos segundos como base para evitar erros de arredondamento)
    executarRega(30); 

    // --- PREPARAÇÃO DO PRÓXIMO CICLO ---
    ultimaRegaAleatoria = tempoAtual; // Zera o cronômetro
    
    // Sorteia novo tempo entre 1 e 5 MINUTOS (60000 a 300.000 ms)
    intervaloAtualSorteado = random(0, 60001);  // ajustado para apresentação

    // Relatório de Status
    Serial.print(">>> Próxima rega agendada para daqui a: ");
    Serial.print(intervaloAtualSorteado / 1000); // Mostra em segundos
    Serial.println(" minutos.");
  }

  // --- REGRA 2: HORÁRIO FIXO (Agendamento) ---
  // Verifica se é exatamente 08:00:00
  /*if (agora.hour() == 8 && agora.minute() == 0 && agora.second() == 0) {
    Serial.println("[AGENDA] Horário de 08:00 detectado.");
    
    // Executa rega por 60 segundos (1 minuto)
    executarRega(60); 
  }

  delay(500); // Delay curto para não sobrecarregar o processador
 */
}
// --- FUNÇÃO AUXILIAR DE CONTROLE ---
// Recebe o tempo em SEGUNDOS (int) para maior precisão
void executarRega(int segundos) {
  Serial.print(">>> ATUANDO VÁLVULA por ");
  Serial.print(segundos);
  Serial.println(" segundos...");

  digitalWrite(PINO_RELE, HIGH); // Abre a válvula (LIGA)
  
  // O '1000UL' força a conta a ser Unsigned Long.
  // Isso evita erro matemático se o tempo for longo.
  delay(segundos * 1000UL);      
  
  digitalWrite(PINO_RELE, LOW);  // Fecha a válvula (DESLIGA)
  
  Serial.println(">>> VÁLVULA FECHADA.");
}