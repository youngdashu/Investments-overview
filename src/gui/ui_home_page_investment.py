# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_page_investmentVnJLEH.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_InvestmentHomePageWidget(object):
    def setupUi(self, InvestmentHomePageWidget):
        if not InvestmentHomePageWidget.objectName():
            InvestmentHomePageWidget.setObjectName(u"InvestmentHomePageWidget")
        InvestmentHomePageWidget.resize(828, 80)
        InvestmentHomePageWidget.setMinimumSize(QSize(686, 80))
        InvestmentHomePageWidget.setStyleSheet(u"#InvestmentHomePageWidget{\n"
"border: 1px solid gray;\n"
"border-radius: 10px;\n"
"background: rgb(207, 206, 209);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(InvestmentHomePageWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.MainFrame = QFrame(InvestmentHomePageWidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setMinimumSize(QSize(0, 0))
        self.MainFrame.setStyleSheet(u"QFrame{\n"
"border: 0px solid gray;\n"
"border-radius: 10px;\n"
"background: rgb(207, 206, 209);\n"
"}\n"
"\n"
"QLabel{\n"
"border: 0px solid gray;\n"
"border-radius: 10px;\n"
"background: rgb(207, 206, 209);\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px;\n"
"background: rgb(126, 125, 128);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid gray;\n"
"border-radius: 5px;\n"
"background: rgb(176, 175, 178);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.MainFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 12, 8, 12)
        self.buttonInvestmentName = QPushButton(self.MainFrame)
        self.buttonInvestmentName.setObjectName(u"buttonInvestmentName")
        self.buttonInvestmentName.setMinimumSize(QSize(300, 40))

        self.horizontalLayout.addWidget(self.buttonInvestmentName)

        self.buttonInvestmentTime = QPushButton(self.MainFrame)
        self.buttonInvestmentTime.setObjectName(u"buttonInvestmentTime")
        self.buttonInvestmentTime.setMinimumSize(QSize(175, 40))

        self.horizontalLayout.addWidget(self.buttonInvestmentTime)

        self.horizontalSpacer_2 = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.buttonDeleteInvestment = QPushButton(self.MainFrame)
        self.buttonDeleteInvestment.setObjectName(u"buttonDeleteInvestment")
        self.buttonDeleteInvestment.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.buttonDeleteInvestment)


        self.horizontalLayout_2.addWidget(self.MainFrame)


        self.retranslateUi(InvestmentHomePageWidget)

        QMetaObject.connectSlotsByName(InvestmentHomePageWidget)
    # setupUi

    def retranslateUi(self, InvestmentHomePageWidget):
        InvestmentHomePageWidget.setWindowTitle(QCoreApplication.translate("InvestmentHomePageWidget", u"Form", None))
        self.buttonInvestmentName.setText("")
        self.buttonInvestmentTime.setText("")
        self.buttonDeleteInvestment.setText(QCoreApplication.translate("InvestmentHomePageWidget", u"XXX", None))
    # retranslateUi

