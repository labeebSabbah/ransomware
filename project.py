import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout

class Calculator(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    # Create the line edit for displaying the result
    self.result = QLineEdit(self)
    self.result.setReadOnly(True)
    self.result.setMaxLength(15)

    # Create the buttons for the digits
    self.digit_buttons = []
    for i in range(10):
      self.digit_buttons.append(QPushButton(str(i), self))

    # Create the buttons for the operations
    self.mul_button = QPushButton("*", self)
    self.div_button = QPushButton("/", self)
    self.add_button = QPushButton("+", self)
    self.sub_button = QPushButton("-", self)
    self.eq_button = QPushButton("=", self)

    # Create the layout
    grid = QGridLayout()
    grid.setSpacing(10)

    # Add the widgets to the layout
    grid.addWidget(self.result, 0, 0, 1, 4)
    for i in range(1, 10):
      grid.addWidget(self.digit_buttons[i], 3 - (i - 1) // 3, (i - 1) % 3)
    grid.addWidget(self.digit_buttons[0], 4, 0)
    grid.addWidget(self.mul_button, 1, 3)
    grid.addWidget(self.div_button, 2, 3)
    grid.addWidget(self.add_button, 3, 3)
    grid.addWidget(self.sub_button, 4, 3)
    grid.addWidget(self.eq_button, 4, 2)

    # Set the layout
    self.setLayout(grid)

    # Connect the buttons to their respective actions
    for button in self.digit_buttons:
      button.clicked.connect(self.input_digit)
    self.mul_button.clicked.connect(self.multiply)
    self.div_button.clicked.connect(self.divide)
    self.add_button.clicked.connect(self.add)
    self.sub_button.clicked.connect(self.subtract)
    self.eq_button.clicked.connect(self.calculate)

    # Set the window properties
    self.setGeometry(300, 300, 300, 300)
    self.setWindowTitle("Calculator")
    self.show()

  def input_digit(self):
    # Get the digit from the button
    digit = self.sender().text()
    # Append the digit to the result
    self.result.setText(self.result.text() + digit)

  def multiply(self):
    # Store the current value in memory and clear the result
    self.memory = float(self.result.text())
    self.result.setText("")
    # Set the operation to multiplication
    self.operation = "*"

  def divide(self):
    # Store the current value in memory and clear the result
    self.memory = float(self.result.text())
    self.result.setText("")
    # Set the operation to division
    self.operation = "/"

  def add(self):
    # Store the current value in memory and clear the result
    self.memory = float(self.result.text())
    self.result.setText("")
    # Set the operation to addition
    self.operation = "+"

  def subtract(self):
    # Store the current value in memory and clear the result
    self.memory = float(self.result.text())
    self.result.setText("")
    # Set the operation to subtraction
    self.operation = "-"

  def calculate(self):
    # Get the current value and perform the calculation
    current = float(self.result.text())
    if self.operation == "*":
      result = self.memory * current
    elif self.operation == "/":
      result = self.memory / current
    elif self.operation == "+":
      result = self.memory + current
    elif self.operation == "-":
      result = self.memory - current
    # Display the result
    self.result.setText(str(result))

app = QApplication(sys.argv)
calc = Calculator()
sys.exit(app.exec())
