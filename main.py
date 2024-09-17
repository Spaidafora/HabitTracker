import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PySide6.QtCore import QDateTime, QTimeZone
from design import Ui_habitWidget  # Import the compiled UI Python file (created from .ui)



app = QApplication(sys.argv)

# Create the main widget, which will act as the container for the UI components
main_widget = QWidget()

# Create an instance of the Ui_habitWidget class, which contains the setup for the UI layout
ui = Ui_habitWidget()

# Apply the design (UI components) to the main_widget by calling setupUi. This populates the widget with buttons, labels, etc.
ui.setupUi(main_widget)


time = QDateTime.currentDateTime().toString()

####################  code test here




def add_habit_date_to_table():
    habit_input = ui.textInputHabit.text()
    row_position = ui.tableWidget.rowCount()
    ui.tableWidget.insertRow((row_position))
    ui.tableWidget.setItem(row_position,0,QTableWidgetItem(habit_input))
    ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(time))
    ui.textInputHabit.clear()


ui.addButton.clicked.connect(add_habit_date_to_table)


##################

# Display the main widget with all UI elements
main_widget.show()

# Execute the application event loop, which keeps the window open and responsive
sys.exit(app.exec())
