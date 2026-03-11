# 🚀 Códigos-Microcontrolador
Códigos referentes ao projeto de tratamento do açaí utilizando (IoT)

> **Engenharia de precisão aplicada ao cultivo de açaí através de estresse hídrico controlado por IA e Hardware.**

---

## 📌 Sumário
* [Sobre o Projeto](#-sobre-o-projeto)
* [Tecnologias e Arquitetura](#️-tecnologias-e-arquitetura)
* [Cronograma de Desenvolvimento](#-cronograma-de-desenvolvimento)
* [Funcionalidades](#-funcionalidades-e-status-de-desenvolvimento)

---

## 💻 Sobre o Projeto

<p align="center">
  <img width="948" height="640" alt="Dashboard do Projeto" src="https://github.com/user-attachments/assets/f0a92b3b-bafd-4ed1-8479-2e36b06bd13b" />
</p>

# 🎋 Sistema de Monitoramento e Estresse Hídrico - Cultivo de Açaí

<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
  <img src="https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white" />
  <img src="https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white" />
</p>

Este projeto integra **Hardware (IoT)** e **Software** para estudar o comportamento de mudas de açaí sob diferentes regimes de irrigação. Através de um sistema híbrido, simulamos cenários variáveis para coletar dados sobre a resiliência da planta em condições dinâmicas.

---

## 🛠️ Tecnologias e Arquitetura
O sistema é dividido em duas camadas principais:

1. **Camada Digital (Controle e Inteligência):**
   - **Python & PyQt6:** Interface Homem-Máquina (HMI) para configuração e monitoramento.
   - **Algoritmo de Aleatoriedade:** Gera intervalos de irrigação randômicos para testar a resposta hídrica da planta.
   - **Comunicação Serial:** Protocolo desenvolvido em Python para envio de pacotes binários para o hardware.

2. **Camada Física (Execução e Campo):**
   - **C++/C (Arduino):** Firmware responsável por processar os sinais do cérebro (Python) e acionar os sistemas de bombeamento.

---

## 📈 Cronograma de Desenvolvimento

### 🗓️ Semana 1: Arquitetura e Planejamento
- Divisão de tarefas e responsabilidades.
- Definição do protocolo de comunicação (Handshake entre Python e C++).
- Estruturação dos requisitos de hardware.

### 🗓️ Semana 2: Desenvolvimento do Core (Atual)
- **Simulação de Estresse:** Implementação do dispositivo que lê intervalos aleatórios.
- **Data Logging:** Agrupamento de dados para análise de performance da muda.
- **Interface UI:** Criação de containers e grupos de entrada usando QSS externo no PyQt6.



## ✨ Funcionalidades e Status de Desenvolvimento

- [x] **Interface Modular (HMI)**: UI desenvolvida em PyQt6 com estilização externa via QSS para melhor manutenção.
- [x] **Gerador de Estresse Hídrico**: Algoritmo Python que calcula e envia intervalos aleatórios de irrigação para o Arduino.
- [ ] **Data Logging CSV**: Exportação automática dos dados de umidade e tempo de resposta para análise em planilhas.
- [ ] **Dark Mode Nativo**: Suporte a temas visuais customizados para operação em diferentes ambientes de luminosidade.
- [x] **Modo de Bloqueio de Segurança**: Lógica no Arduino que impede comandos conflitantes enquanto a irrigação está ativa.

---

<img width="1020" height="791" alt="image" src="https://github.com/user-attachments/assets/2f12f43b-61e3-4b3f-a9d4-2d1e46afec53" />

