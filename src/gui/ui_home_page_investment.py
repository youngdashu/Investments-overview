# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_page_investmentRuwcez.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
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
        InvestmentHomePageWidget.resize(686, 94)
        InvestmentHomePageWidget.setMinimumSize(QSize(686, 94))
        InvestmentHomePageWidget.setStyleSheet(u"#InvestmentHomePageWidget{\n"
"border: 1px solid gray;\n"
"border-radius: 10px;\n"
"background: rgb(207, 206, 209);\n"
"}")
        self.MainFrame = QFrame(InvestmentHomePageWidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(9, 10, 661, 81))
        self.MainFrame.setStyleSheet(u"QFrame{\n"
"/*border: 1px solid gray;*/\n"
"border-radius: 10px;\n"
"background: rgb(207, 206, 209);\n"
"}\n"
"\n"
"QLabel{\n"
"border: 1px solid gray;\n"
"border-radius: 10px;\n"
"background: rgb(207, 206, 209);\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px;\n"
"background: rgb(126, 125, 128);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.MainFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 12, 8, 12)
        self.labelInvestmentId = QLabel(self.MainFrame)
        self.labelInvestmentId.setObjectName(u"labelInvestmentId")

        self.horizontalLayout.addWidget(self.labelInvestmentId)

        self.InvestmentId = QLabel(self.MainFrame)
        self.InvestmentId.setObjectName(u"InvestmentId")
        self.InvestmentId.setMinimumSize(QSize(40, 0))

        self.horizontalLayout.addWidget(self.InvestmentId)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.labelInvestmentName = QLabel(self.MainFrame)
        self.labelInvestmentName.setObjectName(u"labelInvestmentName")
        self.labelInvestmentName.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.labelInvestmentName)

        self.buttonInvestmentName = QPushButton(self.MainFrame)
        self.buttonInvestmentName.setObjectName(u"buttonInvestmentName")
        self.buttonInvestmentName.setMinimumSize(QSize(200, 40))

        self.horizontalLayout.addWidget(self.buttonInvestmentName)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.buttonDeleteInvestment = QPushButton(self.MainFrame)
        self.buttonDeleteInvestment.setObjectName(u"buttonDeleteInvestment")
        self.buttonDeleteInvestment.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.buttonDeleteInvestment)


        self.retranslateUi(InvestmentHomePageWidget)

        QMetaObject.connectSlotsByName(InvestmentHomePageWidget)
    # setupUi

    def retranslateUi(self, InvestmentHomePageWidget):
        InvestmentHomePageWidget.setWindowTitle(QCoreApplication.translate("InvestmentHomePageWidget", u"Form", None))
        self.labelInvestmentId.setText(QCoreApplication.translate("InvestmentHomePageWidget", u"Id inwetycji:", None))
        self.InvestmentId.setText("")
        self.labelInvestmentName.setText(QCoreApplication.translate("InvestmentHomePageWidget", u"Nazwa inwestycji", None))
        self.buttonInvestmentName.setText("")
        self.buttonDeleteInvestment.setText(QCoreApplication.translate("InvestmentHomePageWidget", u"XXX", None))
    # retranslateUi

