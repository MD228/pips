from PyQt6.QtWidgets import *
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from MainWind import Ui_MainWindow
import sys
from connectiondb import load_data, add_record, update_record, delete_record, get_record_by_id
from dialogs import AddDialog, EditDialog

class Main_prog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Auth = QMainWindow()
        self.ui_Auth = Ui_MainWindow()
        self.ui_Auth.setupUi(self.Auth)

        # Подключаем кнопки интерфейса к соответствующим методам
        self.ui_Auth.pushButton_add.clicked.connect(self.show_add_dialog)
        self.ui_Auth.pushButton_edit.clicked.connect(self.show_edit_dialog)
        self.ui_Auth.pushButton_delete.clicked.connect(self.delete_record)
        self.ui_Auth.pushButton_search.clicked.connect(self.search_records)  # Подключаем кнопку поиска

        # Загружаем данные из базы данных в таблицу
        self.load_data()

    def load_data(self, query="SELECT * FROM users"):
        try:
            rows, columns = load_data(query)

            # Создаем модель для отображения данных в таблице
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(columns)

            # Добавляем данные в модель
            for row in rows:
                items = [QStandardItem(str(field)) for field in row]
                model.appendRow(items)

            # Устанавливаем модель в таблицу и настраиваем отображение
            self.ui_Auth.tableView.setModel(model)
            self.ui_Auth.tableView.setColumnHidden(0, True)  # Скрываем колонку ID
            self.ui_Auth.tableView.resizeColumnsToContents()

        except Exception as e:
            # Обрабатываем ошибки, связанные с загрузкой данных
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные: {str(e)}")

    def get_selected_id(self):
        # Получаем ID выбранной записи в таблице
        selection = self.ui_Auth.tableView.selectionModel()
        if not selection.hasSelection():
            QMessageBox.warning(self, "Ошибка", "Выберите запись для редактирования")
            return None

        selected_row = selection.currentIndex().row()
        return self.ui_Auth.tableView.model().index(selected_row, 0).data()

    def show_add_dialog(self):
        # Отображаем диалог добавления новой записи
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            try:
                add_record(
                    dialog.username_edit.text(), #!
                    dialog.passwordd_edit.text(), #!
                    dialog.role_edit.text() #!
                )
                self.load_data()
                QMessageBox.information(self, "Успех", "Данные добавлены!")

            except Exception as e:
                # Обрабатываем ошибки, связанные с добавлением данных
                QMessageBox.critical(self, "Ошибка", f"Ошибка базы данных: {str(e)}")

    def show_edit_dialog(self):
        # Получаем ID выбранной записи
        selected_id = self.get_selected_id()
        if not selected_id:
            return

        try:
            current_data = get_record_by_id(selected_id)

            # Отображаем диалог редактирования записи
            dialog = EditDialog(current_data, self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                update_record(
                    dialog.username_edit.text(), #!
                    dialog.passwordd_edit.text(), #!
                    dialog.role_edit.text(), #!
                    selected_id
                )
                self.load_data()
                QMessageBox.information(self, "Успех", "Данные обновлены!")

        except Exception as e:
            # Обрабатываем ошибки, связанные с редактированием данных
            QMessageBox.critical(self, "Ошибка", f"Ошибка базы данных: {str(e)}")

    def delete_record(self):
        # Получаем ID выбранной записи
        selected_id = self.get_selected_id()
        if not selected_id:
            return

        # Запрашиваем подтверждение удаления у пользователя
        confirm = QMessageBox.question(self, "Подтверждение", "Вы уверены, что хотите удалить эту запись?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.Yes:
            try:
                delete_record(selected_id)
                self.load_data()
                QMessageBox.information(self, "Успех", "Запись удалена!")

            except Exception as e:
                # Обрабатываем ошибки, связанные с удалением данных
                QMessageBox.critical(self, "Ошибка", f"Ошибка базы данных: {str(e)}")

    def search_records(self):
        # Получаем текст поискового запроса
        search_text = self.ui_Auth.lineEdit_search.text()
        if not search_text:
            QMessageBox.warning(self, "Ошибка", "Введите текст для поиска")
            return

        # Формируем SQL-запрос для поиска записей
        query = f"SELECT * FROM users WHERE username LIKE '%{search_text}%' or passwordd LIKE '%{search_text}%' or role LIKE '%{search_text}%'"
        self.load_data(query)

if __name__ == "__main__":
    # Запускаем приложение
    app = QApplication(sys.argv)
    prog = Main_prog()
    prog.Auth.show()
    sys.exit(app.exec())
