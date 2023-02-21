import sys

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        self.combobox = QComboBox()
        self.combobox.addItems(["Metric (km)", "Imperial (miles)"])

        distance_label = QLabel("Distance: ")
        self.distance_input = QLineEdit()

        time_label = QLabel("Time (hours): ")
        self.time_input = QLineEdit()

        # Add buttons
        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add widgets to grid

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(calculate_button, 3, 1)
        grid.addWidget(self.combobox, 0, 3)
        grid.addWidget(self.output_label, 4, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        # Get distance and time from the input boxes
        distance = float(self.distance_input.text())
        time = float(self.time_input.text())

        # Calculate average speed
        speed = distance / time

        # Check what user chose in the combo
        if self.combobox.currentText() == 'Metric (km)':
            speed = round(speed, 2)
            unit = 'km/h'
        if self.combobox.currentText() == 'Imperial (miles)':
            speed = round(speed * 0.621371, 2)
            unit = 'mph'

        # Display the result
        self.output_label.setText(f"Average Speed: {speed} {unit}")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
