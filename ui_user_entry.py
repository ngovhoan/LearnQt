# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_entrylHoaOo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 235)
        MainWindow.setStyleSheet(u"* {\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#leftBody {\n"
"	background-color:rgb(85, 170, 255);\n"
"}\n"
"\n"
"#frm1Head {\n"
"	border-radius:5px;\n"
"	background-color:rgb(85, 0, 255);\n"
"}\n"
"\n"
"#frm2Entry {\n"
"	border-radius:5px;\n"
"	background-color:rgb(85, 170, 255);\n"
"}\n"
"\n"
"#frm3Submit QPushButton {\n"
"	Border: 0px solid blue;\n"
"	border-radius: 5px;\n"
"	color:white;\n"
"}\n"
"\n"
"#pbShow {\n"
"	background-color:rgb(85, 170, 127)\n"
"}\n"
"\n"
"#pbReset {\n"
"	background-color:rgb(255, 85, 127);\n"
"}\n"
"\n"
"#leftBody QLabel, QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#leftBody QLineEdit {\n"
"	background-color:rgb(255, 255, 255);\n"
"	border:1px solid white;\n"
"	border-radius:4px;\n"
"\n"
"	color:rgb(85, 85, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"#leftBody QPushButton:pressed {\n"
"	background-color:rgb(255, 255, 255);\n"
"	color:grey;\n"
"}\n"
"\n"
"#lbTitle {\n"
"	font-size:14px;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"#right"
                        "Body {\n"
"	background-color:white;\n"
"}\n"
"\n"
"#rightBody QLabel {\n"
"	color:rgb(85, 85, 255);\n"
"	font-size:16px;\n"
"}")
        self.wholeBody = QWidget(MainWindow)
        self.wholeBody.setObjectName(u"wholeBody")
        self.wholeBody.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.wholeBody)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftBody = QWidget(self.wholeBody)
        self.leftBody.setObjectName(u"leftBody")
        self.leftBody.setMinimumSize(QSize(272, 0))
        self.leftBody.setMaximumSize(QSize(272, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftBody)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 11, -1, -1)
        self.widget = QWidget(self.leftBody)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 0))
        self.widget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frm1Head = QFrame(self.widget)
        self.frm1Head.setObjectName(u"frm1Head")
        self.frm1Head.setFrameShape(QFrame.StyledPanel)
        self.frm1Head.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frm1Head)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbTitle = QLabel(self.frm1Head)
        self.lbTitle.setObjectName(u"lbTitle")

        self.verticalLayout_3.addWidget(self.lbTitle, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frm1Head)

        self.frm2Entry = QFrame(self.widget)
        self.frm2Entry.setObjectName(u"frm2Entry")
        self.frm2Entry.setMaximumSize(QSize(16777215, 16777215))
        self.frm2Entry.setFrameShape(QFrame.StyledPanel)
        self.frm2Entry.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frm2Entry)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setHorizontalSpacing(7)
        self.formLayout.setVerticalSpacing(15)
        self.label_2 = QLabel(self.frm2Entry)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.leName = QLineEdit(self.frm2Entry)
        self.leName.setObjectName(u"leName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leName)

        self.label_3 = QLabel(self.frm2Entry)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lePhone = QLineEdit(self.frm2Entry)
        self.lePhone.setObjectName(u"lePhone")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lePhone)

        self.label_4 = QLabel(self.frm2Entry)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.leAddress = QLineEdit(self.frm2Entry)
        self.leAddress.setObjectName(u"leAddress")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.leAddress)


        self.verticalLayout_8.addWidget(self.frm2Entry)

        self.frm3Submit = QFrame(self.widget)
        self.frm3Submit.setObjectName(u"frm3Submit")
        self.frm3Submit.setFrameShape(QFrame.StyledPanel)
        self.frm3Submit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frm3Submit)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.pbReset = QPushButton(self.frm3Submit)
        self.pbReset.setObjectName(u"pbReset")
        self.pbReset.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_2.addWidget(self.pbReset)

        self.pbShow = QPushButton(self.frm3Submit)
        self.pbShow.setObjectName(u"pbShow")
        self.pbShow.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_2.addWidget(self.pbShow)


        self.verticalLayout_8.addWidget(self.frm3Submit)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)

        self.verticalLayout.addLayout(self.verticalLayout_7)


        self.horizontalLayout.addWidget(self.leftBody)

        self.rightBody = QWidget(self.wholeBody)
        self.rightBody.setObjectName(u"rightBody")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightBody.sizePolicy().hasHeightForWidth())
        self.rightBody.setSizePolicy(sizePolicy)
        self.rightBody.setMinimumSize(QSize(0, 0))
        self.rightBody.setMaximumSize(QSize(16777215, 16777215))
        self.rightBody.setSizeIncrement(QSize(1, 0))
        self.rightBody.setBaseSize(QSize(1, 1))
        self.verticalLayout_2 = QVBoxLayout(self.rightBody)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frm4Status = QFrame(self.rightBody)
        self.frm4Status.setObjectName(u"frm4Status")
        self.frm4Status.setMinimumSize(QSize(0, 200))
        self.frm4Status.setMaximumSize(QSize(16777215, 16777215))
        self.frm4Status.setFrameShape(QFrame.StyledPanel)
        self.frm4Status.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frm4Status, 0, Qt.AlignTop)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.rightBody)

        MainWindow.setCentralWidget(self.wholeBody)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbTitle.setText(QCoreApplication.translate("MainWindow", u"Entry App", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.pbReset.setText(QCoreApplication.translate("MainWindow", u"Resset", None))
        self.pbShow.setText(QCoreApplication.translate("MainWindow", u"Show", None))
    # retranslateUi

