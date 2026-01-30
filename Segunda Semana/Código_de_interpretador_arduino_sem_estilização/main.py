import pandas as pd
import random
from datetime import datetime, timedelta
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QDoubleValidator
from PyQt6.QtWidgets import *

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.dataInicial = datetime.today()
        self.inicarInterface()

    def inicarInterface(self):
        self.setWindowTitle("Gerador")
        self.setGeometry(0, 0, 400, 500)
        #self.showMaximized()

        self.dataLabel = QLabel("Data inicial")
        self.dataLine = QLineEdit()
        self.dataLine.setText(f"{self.dataInicial.date()}")

        self.numeroDeIrrigacoesLabel = QLabel("Número de irrigações")
        self.distribuicaoIrrigacoesComboBox = QComboBox()
        self.distribuicaoIrrigacoesComboBox.addItems(["Distribuição Triangular", "Distribuição Gaussiana"])
        self.campo1IrrigacoesLabel = QLabel("Valor mínimo")
        self.campo1IrrigacoesLine = QLineEdit()
        self.campo1IrrigacoesLine.setText("0")
        self.campo2IrrigacoesLabel = QLabel("Moda")
        self.campo2IrrigacoesLine = QLineEdit()
        self.campo2IrrigacoesLine.setText("2")
        self.campo3IrrigacoesLabel = QLabel("Valor máximo")
        self.campo3IrrigacoesLine = QLineEdit()
        self.campo3IrrigacoesLine.setText("4")

        self.intervaloHorarioLabel = QLabel("Intervalo de horário")
        self.intervalo1Line = QLineEdit()
        self.intervalo1Line.setText("06:00")
        self.intervalo_Label = QLabel("-")
        self.intervalo2Line = QLineEdit()
        self.intervalo2Line.setText("18:00")

        self.quantidadeDiaLabel = QLabel("Quantidade de dias")
        self.quantidadeDiaLine = QLineEdit()
        self.quantidadeDiaLine.setText("30")

        self.duracaoIrrigacaoLabel = QLabel("Duração de irrigação")
        self.distribuicaoDuracaoComboBox = QComboBox()
        self.distribuicaoDuracaoComboBox.addItems(["Distribuição Triangular", "Distribuição Gaussiana"])
        self.distribuicaoDuracaoComboBox.setCurrentText("Distribuição Gaussiana")
        self.campo1DuracaoLabel = QLabel("Média")
        self.campo1DuracaoLine = QLineEdit()
        self.campo1DuracaoLine.setText("15")
        self.campo2DuracaoLabel = QLabel("Desvio padrão")
        self.campo2DuracaoLine = QLineEdit()
        self.campo2DuracaoLine.setText("5")

        self.botaoExportar = QPushButton("Exportar")
        self.botaoExportar.clicked.connect(self.gerarCSV)

        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()

        layout3.addWidget(self.campo1IrrigacoesLabel)
        layout3.addWidget(self.campo2IrrigacoesLabel)
        layout3.addWidget(self.campo3IrrigacoesLabel)
        layout4 = QHBoxLayout()
        layout4.addWidget(self.campo1IrrigacoesLine)
        layout4.addWidget(self.campo2IrrigacoesLine)
        layout4.addWidget(self.campo3IrrigacoesLine)
        layout1.addWidget(self.dataLabel)
        layout1.addWidget(self.dataLine)
        layout1.addWidget(self.numeroDeIrrigacoesLabel)
        layout1.addWidget(self.distribuicaoIrrigacoesComboBox)
        layout1.addLayout(layout3)
        layout1.addLayout(layout4)
        layout1.addWidget(self.intervaloHorarioLabel)
        layout2.addWidget(self.intervalo1Line)
        layout2.addWidget(self.intervalo_Label)
        layout2.addWidget(self.intervalo2Line)
        layout1.addLayout(layout2)
        layout1.addWidget(self.quantidadeDiaLabel)
        layout1.addWidget(self.quantidadeDiaLine)
        layout1.addWidget(self.duracaoIrrigacaoLabel)
        layout1.addWidget(self.distribuicaoDuracaoComboBox)
        layout5 = QHBoxLayout()
        layout5.addWidget(self.campo1DuracaoLabel)
        layout5.addWidget(self.campo2DuracaoLabel)
        layout6 = QHBoxLayout()
        layout6.addWidget(self.campo1DuracaoLine)
        layout6.addWidget(self.campo2DuracaoLine)
        layout1.addLayout(layout5)
        layout1.addLayout(layout6)

        layout1.addWidget(self.botaoExportar)




        self.setLayout(layout1)


    def distribuicaoTriangular(self, left, moda, right, dias):
        return [int(round(random.triangular(left - 0.5, right + 0.5, moda))) for i in range(dias)]

    def distribuicaoGaussiana(self, media, desvioPadrao, dias):
        return [max(1, int(round(random.gauss(media, desvioPadrao)))) for i in range(dias)]

    def str_to_min(self, horario_str):
        try:
            # Quebra "06:15" em ["06", "15"] e converte para inteiros
            h, m = map(int, horario_str.split(':'))
            return h * 60 + m
        except ValueError:
            return 0

    def gerarCSV(self):
        self.quantidadeDia = int(self.quantidadeDiaLine.text())
        self.maxAtivacoesPorDia = int(self.campo3IrrigacoesLine.text())
        dadosLista = []

        for i in range(self.quantidadeDia):
            dataAtual = self.dataInicial + timedelta(days=i)
            dataFormatada = dataAtual.strftime("%d/%m/%Y")

            print(self.campo1IrrigacoesLine.text())
            val_min = float(self.campo1IrrigacoesLine.text()) - 0.5
            val_max = float(self.campo3IrrigacoesLine.text()) + 0.5
            val_moda = float(self.campo2IrrigacoesLine.text())
            qtdHoje = int(round(random.triangular(val_min, val_max,val_moda)))


            duracoes = self.distribuicaoGaussiana(float(self.campo1DuracaoLine.text()), float(self.campo2DuracaoLine.text()), qtdHoje)

            horarios = []
            limite_min = self.str_to_min(self.intervalo1Line.text())
            limite_max = self.str_to_min(self.intervalo2Line.text())
            for _ in range(qtdHoje):
                minutos_total = random.randint(limite_min, limite_max)

                h = minutos_total // 60
                m = minutos_total % 60

                horarios.append(f"{h:02d}:{m:02d}")

            horarios.sort()

            linha = {"data": dataFormatada}

            for k in range(self.maxAtivacoesPorDia):
                idx = k + 1
                if k < qtdHoje:
                    linha[f"horaInicio{idx}"] = horarios[k]
                    linha[f"tempoAtivado{idx}"] = duracoes[k]
                else:
                    linha[f"horaInicio{idx}"] = "00:00"
                    linha[f"tempoAtivado{idx}"] = "0"

            dadosLista.append(linha)

        df = pd.DataFrame(dadosLista)

        colunasFinais = ["data"]
        for k in range(1, self.maxAtivacoesPorDia + 1):
            colunasFinais.append(f"horaInicio{k}")
            colunasFinais.append(f"tempoAtivado{k}")

        df = df[colunasFinais]

        nomeArquivo, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Arquivo CSV",
            "",
            "Arquivos CSV (*.csv);;Todos os Arquivos (*)"
        )

        if nomeArquivo:
            df.to_csv(nomeArquivo, sep=";", index=False, encoding="utf-8")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor = Interface()
    monitor.show()
    sys.exit(app.exec())