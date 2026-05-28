import PyQt6.QtWidgets
import PyQt6.uic

app = PyQt6.QtWidgets.QApplication([])
tela = PyQt6.uic.loadUi("media.ui")


def calcular_media():
    try:
        nome = tela.txt_nome.text()

        nota1 = float(tela.txt_nota1.text())
        nota2 = float(tela.txt_nota2.text())
        nota3 = float(tela.txt_nota3.text())

        media = (nota1 + nota2 + nota3) / 3
        media = round(media, 2)

        if media < 7:
            resultado = "Reprovado"
        elif media >= 4:
            resultado = "Aprovado"
        else:
            resultado = "Recuperação"

        tela.lbl_resultado.setText(f"{nome} - Média: {media} - {resultado}")

    except ValueError:
        tela.lbl_resultado.setText("Erro: digite apenas números")


def clean_camp():
    tela.txt_nome.setText("")
    tela.txt_nota1.setText("")
    tela.txt_nota2.setText("")
    tela.txt_nota3.setText("")
    tela.lbl_resultado.setText("")


tela.btn_calcular.clicked.connect(calcular_media)
tela.btn_limpar.clicked.connect(limpar_campos)

tela.show()
app.exec()