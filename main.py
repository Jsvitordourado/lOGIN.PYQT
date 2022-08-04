from tkinter import Button
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys # IMPORTAR O SISTEMA 

#crio a MainWindow a partir da QMainWindow 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #titulo
        self.setWindowTitle("Sistema de login")
        button = QPushButton("Clique aqui!")
        #definir a função a ser chamada pelo botão
        button.clicked.connect(self.imprimeClique)
        self.setCentralWidget(button)

    def imprimeClique(self):
        print("Botão clicado!")

# Criar a aplicação
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.axec() # executar