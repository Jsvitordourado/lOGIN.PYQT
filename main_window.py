from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

FILE_UI = 'main_window.ui'

class MainWindow(QMainWindow):
    loginAdm = 'adm'
    senhaAdm = '123'

    def __init__(self):
        #
        uic.loadUI(FILE_UI, self)

        # Atribuir um evento (função) para um botão
        self.btn_ok.clickedconnect(self.logar)

    def logar(self):
        """Função a ser chamada quando o botão for pressionado"""
        login =  self.loginLineEdit.text()
        senha = self.senhaLineEdit.text()
        if login == "" or senha == "":
            self.label_aviso.setText("Preencha todos os campos!!")
        else:
            if login == self.loginAdm:
                # verificar a senha 
                if senha == self.senhaAdm:
                    self.label_aviso.setText("LOGIN REALIZADO COM SUCESSO...")
                    # Apaga os campos login e senha 
                    self.loginLineEdit.clear()
                    self.senhaLineEdit.clear()
                else:
                    self.label_aviso.setText(
                        "senha invalida, tente novamente !")
            else:
                self.label_aviso.setText("Login inválido, tente novamente!")HHHBHBBHBHHBHB