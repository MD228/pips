from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class AddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить запись")
        self.layout = QVBoxLayout(self)

        # Поля для ввода данных новой записи
        self.username_edit = QLineEdit() #!
        self.passwordd_edit = QLineEdit() #!
        self.role_edit = QLineEdit() #!
        self.btn_ok = QPushButton("ок")
        self.btn_close = QPushButton("закрыть")

        # Добавляем поля с подписями в макет
        self.layout.addWidget(QLabel("Имя:"))
        self.layout.addWidget(self.username_edit) #!
        self.layout.addWidget(QLabel("Пароль"))
        self.layout.addWidget(self.passwordd_edit) #!
        self.layout.addWidget(QLabel("Роль"))
        self.layout.addWidget(self.role_edit) #!
        self.layout.addWidget(self.btn_ok)
        self.layout.addWidget(self.btn_close)

        # Подключаем кнопки к соответствующим методам
        self.btn_ok.clicked.connect(self.accept)
        self.btn_close.clicked.connect(self.reject)

class EditDialog(QDialog):
    def __init__(self, current_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Редактировать запись")
        self.layout = QVBoxLayout(self)

        # Поля для редактирования данных существующей записи
        self.username_edit = QLineEdit() #!
        self.passwordd_edit = QLineEdit() #!
        self.role_edit = QLineEdit() #!
        self.btn_ok = QPushButton("ок")
        self.btn_close = QPushButton("закрыть")

        # Добавляем поля с подписями в макет
        self.layout.addWidget(QLabel("Имя:"))
        self.layout.addWidget(self.username_edit) #!
        self.layout.addWidget(QLabel("Пароль"))
        self.layout.addWidget(self.passwordd_edit) #!
        self.layout.addWidget(QLabel("Роль"))
        self.layout.addWidget(self.role_edit) #!
        self.layout.addWidget(self.btn_ok)
        self.layout.addWidget(self.btn_close)

        # Устанавливаем текущие данные в поля для редактирования
        self.username_edit.setText(current_data[1]) #!
        self.passwordd_edit.setText(current_data[2]) #!
        self.role_edit.setText(current_data[3]) #!

        # Подключаем кнопки к соответствующим методам
        self.btn_ok.clicked.connect(self.accept)
        self.btn_close.clicked.connect(self.reject)
