# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowBAsvkb.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1016, 693)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(197, 195, 198);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMinimumSize(QSize(800, 50))
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setStyleSheet(u"")
        self.main_header.setFrameShape(QFrame.WinPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_header)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 4, -1, -1)
        self.title_bar_container = QFrame(self.main_header)
        self.title_bar_container.setObjectName(u"title_bar_container")
        self.title_bar_container.setMinimumSize(QSize(151, 51))
        self.title_bar_container.setMaximumSize(QSize(200, 16777215))
        self.title_bar_container.setFrameShape(QFrame.StyledPanel)
        self.title_bar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.title_bar_container)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.left_menu_toggle = QFrame(self.title_bar_container)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.left_menu_toggle)

        self.title_bar = QFrame(self.title_bar_container)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.title_bar)


        self.horizontalLayout_3.addWidget(self.title_bar_container)

        self.horizontalSpacer = QSpacerItem(10000, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.top_right_buttons = QFrame(self.main_header)
        self.top_right_buttons.setObjectName(u"top_right_buttons")
        self.top_right_buttons.setMinimumSize(QSize(100, 38))
        self.top_right_buttons.setMaximumSize(QSize(100, 16777215))
        self.top_right_buttons.setStyleSheet(u"")
        self.top_right_buttons.setFrameShape(QFrame.StyledPanel)
        self.top_right_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_right_buttons)
#ifndef Q_OS_MAC
        self.horizontalLayout_2.setSpacing(-1)
#endif
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minimizeButton = QPushButton(self.top_right_buttons)
        self.minimizeButton.setObjectName(u"minimizeButton")

        self.horizontalLayout_2.addWidget(self.minimizeButton)

        self.restoreButton = QPushButton(self.top_right_buttons)
        self.restoreButton.setObjectName(u"restoreButton")

        self.horizontalLayout_2.addWidget(self.restoreButton)

        self.closeButton = QPushButton(self.top_right_buttons)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.horizontalLayout_3.addWidget(self.top_right_buttons)


        self.verticalLayout.addWidget(self.main_header, 0, Qt.AlignRight)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMinimumSize(QSize(80, 0))
        self.left_side_menu.setMaximumSize(QSize(70, 16777215))
        self.left_side_menu.setStyleSheet(u"#left_side_menu{\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px;\n"
"background: rgb(126, 125, 128);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.left_side_menu.setFrameShape(QFrame.WinPanel)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.button_load_data = QPushButton(self.left_side_menu)
        self.button_load_data.setObjectName(u"button_load_data")
        self.button_load_data.setGeometry(QRect(10, 10, 51, 32))
        self.button_save_data = QPushButton(self.left_side_menu)
        self.button_save_data.setObjectName(u"button_save_data")
        self.button_save_data.setGeometry(QRect(10, 50, 51, 32))
        self.button_new_investment = QPushButton(self.left_side_menu)
        self.button_new_investment.setObjectName(u"button_new_investment")
        self.button_new_investment.setGeometry(QRect(10, 90, 51, 32))
        self.button_compare = QPushButton(self.left_side_menu)
        self.button_compare.setObjectName(u"button_compare")
        self.button_compare.setGeometry(QRect(10, 130, 51, 32))
        self.pushButton_5 = QPushButton(self.left_side_menu)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 170, 51, 32))

        self.horizontalLayout.addWidget(self.left_side_menu)

        self.center_main_items = QFrame(self.main_body)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setMinimumSize(QSize(0, 530))
        self.center_main_items.setStyleSheet(u"")
        self.center_main_items.setFrameShape(QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.center_main_items)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_currently_opened = QFrame(self.center_main_items)
        self.frame_currently_opened.setObjectName(u"frame_currently_opened")
        self.frame_currently_opened.setMinimumSize(QSize(0, 31))
        self.frame_currently_opened.setStyleSheet(u"#frame_currently_opened{\n"
"\n"
"border: 2px solid gray;\n"
"border-radius: 5px;\n"
"}")
        self.frame_currently_opened.setFrameShape(QFrame.StyledPanel)
        self.frame_currently_opened.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_currently_opened)

        self.scrollArea = QScrollArea(self.center_main_items)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"#scrollArea {\n"
"border: 3px solid gray;\n"
"border-radius: 8px;\n"
"background: white;\n"
"}\n"
"\n"
"QFrame{\n"
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
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 832, 552))
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContainer{\n"
"border: 3px solid gray;\n"
"border-radius: 8px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 24, -1)
        self.frame_main_characteristics = QFrame(self.scrollAreaWidgetContents)
        self.frame_main_characteristics.setObjectName(u"frame_main_characteristics")
        self.frame_main_characteristics.setMinimumSize(QSize(630, 40))
        self.frame_main_characteristics.setFrameShape(QFrame.StyledPanel)
        self.frame_main_characteristics.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_main_characteristics)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.button_main_characteristics = QPushButton(self.frame_main_characteristics)
        self.button_main_characteristics.setObjectName(u"button_main_characteristics")
        self.button_main_characteristics.setMinimumSize(QSize(0, 24))

        self.verticalLayout_4.addWidget(self.button_main_characteristics)

        self.tableMainCharacteristics = QTableWidget(self.frame_main_characteristics)
        if (self.tableMainCharacteristics.columnCount() < 1):
            self.tableMainCharacteristics.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableMainCharacteristics.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableMainCharacteristics.rowCount() < 3):
            self.tableMainCharacteristics.setRowCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableMainCharacteristics.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableMainCharacteristics.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableMainCharacteristics.setVerticalHeaderItem(2, __qtablewidgetitem3)
        self.tableMainCharacteristics.setObjectName(u"tableMainCharacteristics")

        self.verticalLayout_4.addWidget(self.tableMainCharacteristics)


        self.verticalLayout_2.addWidget(self.frame_main_characteristics)

        self.frame_information = QFrame(self.scrollAreaWidgetContents)
        self.frame_information.setObjectName(u"frame_information")
        self.frame_information.setMinimumSize(QSize(630, 40))
        self.frame_information.setFrameShape(QFrame.StyledPanel)
        self.frame_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_information)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.button_information = QPushButton(self.frame_information)
        self.button_information.setObjectName(u"button_information")
        self.button_information.setMinimumSize(QSize(0, 24))

        self.verticalLayout_9.addWidget(self.button_information)

        self.tableInformation = QTableWidget(self.frame_information)
        self.tableInformation.setObjectName(u"tableInformation")

        self.verticalLayout_9.addWidget(self.tableInformation)


        self.verticalLayout_2.addWidget(self.frame_information)

        self.frame_own_contribution = QFrame(self.scrollAreaWidgetContents)
        self.frame_own_contribution.setObjectName(u"frame_own_contribution")
        self.frame_own_contribution.setMinimumSize(QSize(630, 40))
        self.frame_own_contribution.setFrameShape(QFrame.StyledPanel)
        self.frame_own_contribution.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_own_contribution)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.button_own_contribution = QPushButton(self.frame_own_contribution)
        self.button_own_contribution.setObjectName(u"button_own_contribution")
        self.button_own_contribution.setMinimumSize(QSize(0, 24))

        self.verticalLayout_5.addWidget(self.button_own_contribution)

        self.tableOwnContribution = QTableWidget(self.frame_own_contribution)
        self.tableOwnContribution.setObjectName(u"tableOwnContribution")

        self.verticalLayout_5.addWidget(self.tableOwnContribution)


        self.verticalLayout_2.addWidget(self.frame_own_contribution)

        self.frame_credit = QFrame(self.scrollAreaWidgetContents)
        self.frame_credit.setObjectName(u"frame_credit")
        self.frame_credit.setMinimumSize(QSize(630, 40))
        self.frame_credit.setFrameShape(QFrame.StyledPanel)
        self.frame_credit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_credit)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.button_credit = QPushButton(self.frame_credit)
        self.button_credit.setObjectName(u"button_credit")
        self.button_credit.setMinimumSize(QSize(0, 24))

        self.verticalLayout_6.addWidget(self.button_credit)

        self.tableCredit = QTableWidget(self.frame_credit)
        self.tableCredit.setObjectName(u"tableCredit")

        self.verticalLayout_6.addWidget(self.tableCredit)


        self.verticalLayout_2.addWidget(self.frame_credit)

        self.frame_rent = QFrame(self.scrollAreaWidgetContents)
        self.frame_rent.setObjectName(u"frame_rent")
        self.frame_rent.setMinimumSize(QSize(630, 40))
        self.frame_rent.setFrameShape(QFrame.StyledPanel)
        self.frame_rent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_rent)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.button_rent = QPushButton(self.frame_rent)
        self.button_rent.setObjectName(u"button_rent")
        self.button_rent.setMinimumSize(QSize(0, 24))

        self.verticalLayout_7.addWidget(self.button_rent)

        self.tableRent = QTableWidget(self.frame_rent)
        self.tableRent.setObjectName(u"tableRent")

        self.verticalLayout_7.addWidget(self.tableRent)


        self.verticalLayout_2.addWidget(self.frame_rent)

        self.frame_investment_assessment = QFrame(self.scrollAreaWidgetContents)
        self.frame_investment_assessment.setObjectName(u"frame_investment_assessment")
        self.frame_investment_assessment.setMinimumSize(QSize(630, 40))
        self.frame_investment_assessment.setFrameShape(QFrame.StyledPanel)
        self.frame_investment_assessment.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_investment_assessment)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.button_investment_assessment = QPushButton(self.frame_investment_assessment)
        self.button_investment_assessment.setObjectName(u"button_investment_assessment")
        self.button_investment_assessment.setMinimumSize(QSize(0, 24))

        self.verticalLayout_8.addWidget(self.button_investment_assessment)

        self.tableInvestmentAssessment = QTableWidget(self.frame_investment_assessment)
        self.tableInvestmentAssessment.setObjectName(u"tableInvestmentAssessment")

        self.verticalLayout_8.addWidget(self.tableInvestmentAssessment)


        self.verticalLayout_2.addWidget(self.frame_investment_assessment)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.center_main_items)

        self.right_side_menu = QFrame(self.main_body)
        self.right_side_menu.setObjectName(u"right_side_menu")
        self.right_side_menu.setMinimumSize(QSize(70, 0))
        self.right_side_menu.setMaximumSize(QSize(100, 16777215))
        self.right_side_menu.setStyleSheet(u"")
        self.right_side_menu.setFrameShape(QFrame.WinPanel)
        self.right_side_menu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.right_side_menu)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMaximumSize(QSize(16777215, 50))
        self.main_footer.setStyleSheet(u"")
        self.main_footer.setFrameShape(QFrame.WinPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minimizeButton.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.restoreButton.setText(QCoreApplication.translate("MainWindow", u"[]", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.button_load_data.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj dane", None))
        self.button_save_data.setText(QCoreApplication.translate("MainWindow", u"Zapisz dane", None))
        self.button_new_investment.setText(QCoreApplication.translate("MainWindow", u"Nowa", None))
        self.button_compare.setText(QCoreApplication.translate("MainWindow", u"Por\u00f3wnaj", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.button_main_characteristics.setText(QCoreApplication.translate("MainWindow", u"Cechy g\u0142\u00f3wne", None))
        ___qtablewidgetitem = self.tableMainCharacteristics.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cena zakupu", None));
        ___qtablewidgetitem1 = self.tableMainCharacteristics.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"POW. m\u00b2", None));
        ___qtablewidgetitem2 = self.tableMainCharacteristics.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Cena/m\u00b2", None));
        self.button_information.setText(QCoreApplication.translate("MainWindow", u"Informacje", None))
        self.button_own_contribution.setText(QCoreApplication.translate("MainWindow", u"Wk\u0142ad w\u0142asny", None))
        self.button_credit.setText(QCoreApplication.translate("MainWindow", u"Kredyt", None))
        self.button_rent.setText(QCoreApplication.translate("MainWindow", u"Wynajem", None))
        self.button_investment_assessment.setText(QCoreApplication.translate("MainWindow", u"Ocena inwestycji", None))
    # retranslateUi

