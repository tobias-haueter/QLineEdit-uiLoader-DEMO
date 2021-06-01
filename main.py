import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout

# Load the UI file
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('qlineeditDemo.ui', self) # Load the .ui file

        ## Pointing GUI Elements

        # integer validator [e1]
        e1 = self.le_e1 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_e1') # Find the element
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont("Arial", 20))

        # Double validator [e2]
        e2 = self.le_e2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_e2') # Find the element
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        # Input Mask [e3]
        e3 = self.le_e3 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_e3') # Find the element
        e3.setInputMask("+99_9999_999999")

        # Text changed [e4]
        e4 = self.le_e4 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_e4') # Find the element
        e4.textChanged.connect(self.textchanged)

        # Password [e5]]
        e5 = self.le_e5 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_e5')# Find the element
        e5.setEchoMode(QLineEdit.Password)

        # Read Only [e6]
        e6 = self.le_e6 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_e6') # Find the element
        self.le_e6.setText('ReadOnly')
        e6.setReadOnly(True)
        e5.editingFinished.connect(self.enterPress)

        ## show MainWindows
        self.show()

    def textchanged(self,text):
            print("Changed: " + text)

    def enterPress(self):
            print("Enter pressed")

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application