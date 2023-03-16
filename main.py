from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

# Declear global variables (Out of class)
isRightName = False
isRightPhone = False

class Main(QMainWindow):


    def __init__(self):
        super(Main,self).__init__()
        loadUi('user_entry.ui',self)
        self.setEvent()


    def setEvent(self):
        self.leName.textChanged.connect(lambda: self.checkRightEntry(1))
        self.lePhone.textChanged.connect(lambda: self.checkRightEntry(2))
        self.leAddress.textChanged.connect(lambda: self.checkRightEntry(3))

        self.pbShow.clicked.connect(self.showInfo)
        self.pbReset.clicked.connect(self.resetInfo)
        
        self.pbShow.setEnabled(False)

    def showInfo(self):
    
        strStatus = f'''Welcome to my application\nYour Info: 
        {self.leName.text()}
        {self.lePhone.text()}
        {self.leAddress.text()}\nThank you and Regards'''

        self.lbStatus.setText(strStatus)

    def resetInfo(self):
        strStatus = 'This page will show your infomation!'
        self.lbStatus.setText(strStatus)
        self.leName.setText('')
        self.lePhone.setText('')
        self.leAddress.setText('')
    
    def checkRightEntry(self,flat):
        # To use global variables => add 'global' before name
        global isRightName
        global isRightPhone
        if flat == 1:
            if self.leName.text().isalpha():
                self.leName.setStyleSheet('color:blue;')
                isRightName = True
            else:
                self.leName.setStyleSheet('color:red;')
                isRightName = False
        elif flat == 2:
            if self.lePhone.text().isnumeric():
                self.lePhone.setStyleSheet('color:blue;')
                isRightPhone = True
            else:
                self.lePhone.setStyleSheet('color:red;')
                isRightPhone = False
        if isRightName and isRightPhone:
            self.pbShow.setEnabled(True)
        else:
            self.pbShow.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_()