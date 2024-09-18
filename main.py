import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PySide6.QtCore import QDateTime
from design import Ui_habitWidget  # Import the compiled UI Python file (created from .ui)
import json  # save data


app = QApplication(sys.argv)
mainWidget = QWidget()

# Instance of the Ui_habitWidget class, which contains the setup for the UI layout
ui = Ui_habitWidget()

# Display the GUI
ui.setupUi(mainWidget)
time = QDateTime.currentDateTime().toString()

def addHabitDateToTable():
    habitInput = ui.textInputHabit.text()
    rowPosition = ui.tableWidget.rowCount()
    ui.tableWidget.insertRow((rowPosition))
    ui.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(habitInput))
    ui.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(time))
    ui.textInputHabit.clear()

def saveDataToJson():
    habits = []
    for row in range(ui.tableWidget.rowCount()):
        habit = ui.tableWidget.item(row, 0).text()
        date = ui.tableWidget.item(row, 1).text()
        habits.append({
            "habits" : habit,
            "date" : date
        })

    with open('habitsData.json', 'w') as f:
        json.dump(habits, f)

def loadDataFromJson():
    f = open('habitsData.json')
    data = json.load(f)
    for habits in data:
        rowPosition = ui.tableWidget.rowCount()
        ui.tableWidget.insertRow(rowPosition)
        ui.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(habits['habits']))
        ui.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(habits['date']))
    f.close()

# Connect the save button to save_data method

ui.addButton.clicked.connect(addHabitDateToTable)
ui.saveButton.clicked.connect(saveDataToJson)

ui.loadButton.clicked.connect(loadDataFromJson)


mainWidget.show()
sys.exit(app.exec())
