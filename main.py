from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import sip

###################################
# DECLARE GLOBAL VARIABLES (OUT CLASS)
isRightName = False
isRightPhone = False
########################################

grid = QVBoxLayout()
i = 0

class Main(QMainWindow):


    def __init__(self):
        super(Main,self).__init__()
        loadUi('user_entry.ui',self)
        global grid
        self.frm4Status.setLayout(grid)
        grid.setSpacing(0)
        grid.setAlignment(Qt.AlignTop)
        self.setEvent()


    def setEvent(self):
        self.leName.textChanged.connect(lambda: self.checkRightEntry(1))
        self.lePhone.textChanged.connect(lambda: self.checkRightEntry(2))
        self.leAddress.textChanged.connect(lambda: self.checkRightEntry(3))

        self.pbShow.clicked.connect(self.addToList)
        self.pbReset.clicked.connect(self.resetInfo)
        
        self.pbShow.setEnabled(False)

    def showInfo(self):
    
        strStatus = f'''Welcome to my application\nYour Info: 
        {self.leName.text()}
        {self.lePhone.text()}
        {self.leAddress.text()}\nThank you and Regards'''

        self.lbStatus.setText(strStatus)

    def addToList(self):
        ##########################################
        ######### DECLARE WIDGET
        global i
        
        frm_1 = QFrame()
        frm_1.setObjectName(f'frm_{i}')
        
        lb_1 = QLabel(self.leName.text())
        lb_1.setObjectName(f'lb_name_{i}')

        lb_2 = QLabel(self.lePhone.text())
        lb_2.setObjectName(f'lb_phone_{i}')

        lb_3 = QLabel(self.leAddress.text())
        lb_3.setObjectName(f'lb_address_{i}')

        btn = QPushButton('Del')
        btn.setObjectName(f'btn_{i}')
        btn.clicked.connect(lambda: self.deleteRow(frm_1))
        
        i=i+1
        ############################################

        ################################################
        ############ STYLE SHEET WIDGET: BORDER, COLOR, SIZE
        lb_1.setStyleSheet('border: 1px solid blue; border-radius:3px; ')
        lb_2.setStyleSheet('border: 1px solid blue; border-radius:3px;')
        lb_3.setStyleSheet('border: 1px solid blue; border-radius:3px;')
        btn.setStyleSheet('background:blue; color:white;')
        lb_1.setMaximumHeight(20)
        lb_2.setMaximumHeight(20)
        lb_3.setMaximumHeight(20)
        btn.setMaximumHeight(20)

        lb_1.setMaximumWidth(150)
        btn.setMaximumWidth(30)
        #lb_2.setMaximumWidth(150)
        #lb_3.setMaximumWidth(150)
        lb_1.setMinimumWidth(150)
        btn.setMinimumWidth(30)
        #lb_2.setMinimumWidth(150)
        #lb_3.setMinimumWidth(150)
        ################################################

        ################################################
        ###### CONFIG LAYOUT: ADD, UPDATE WIDGETS
        global grid
        
        grid_ = QGridLayout()
        grid_.setContentsMargins(0,0,0,0)
        grid_.addWidget(lb_1,0,0)
        grid_.addWidget(lb_2,0,1)
        grid_.addWidget(lb_3,0,2)
        grid_.addWidget(btn,0,3)
        frm_1.setLayout(grid_)

        #grid.addStretch()
        grid.addWidget(frm_1)
        #grid.addStretch()

        # UPDATE LAYOUT AFTER ADDED WIDGET
        grid.update()
        ##############################################
    
    def deleteRow(self,w):

        ##################################
        # IN THIS CASE (WIDGET HAS CHILD): USING SIP
        global grid
        
        grid.removeWidget(w)
        sip.delete(w)
        w = None
        ###########################################


    def resetInfo(self):
        strStatus = 'This page will show your infomation!'
        self.lbStatus.setText(strStatus)
        self.leName.setText('')
        self.lePhone.setText('')
        self.leAddress.setText('')
    
    def checkRightEntry(self,flat):
        #######################################################################
        # TO USE GLOBAL VARIABLES: ADD 'global' BEFORE VARIABLES NAME
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
        ############################################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_()