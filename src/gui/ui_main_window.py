# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowOtxQwl.ui'
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
        self.verticalLayout_18 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(6, -1, 6, -1)
        self.button_load_data = QPushButton(self.left_side_menu)
        self.button_load_data.setObjectName(u"button_load_data")
        self.button_load_data.setMinimumSize(QSize(0, 60))

        self.verticalLayout_18.addWidget(self.button_load_data)

        self.button_save_data = QPushButton(self.left_side_menu)
        self.button_save_data.setObjectName(u"button_save_data")
        self.button_save_data.setMinimumSize(QSize(0, 60))

        self.verticalLayout_18.addWidget(self.button_save_data)

        self.button_new_investment = QPushButton(self.left_side_menu)
        self.button_new_investment.setObjectName(u"button_new_investment")
        self.button_new_investment.setMinimumSize(QSize(0, 60))

        self.verticalLayout_18.addWidget(self.button_new_investment)

        self.button_compare = QPushButton(self.left_side_menu)
        self.button_compare.setObjectName(u"button_compare")
        self.button_compare.setMinimumSize(QSize(0, 60))

        self.verticalLayout_18.addWidget(self.button_compare)

        self.button_home_page = QPushButton(self.left_side_menu)
        self.button_home_page.setObjectName(u"button_home_page")
        self.button_home_page.setMinimumSize(QSize(0, 60))

        self.verticalLayout_18.addWidget(self.button_home_page)


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
        self.horizontalLayout_44 = QHBoxLayout(self.frame_currently_opened)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.frame_42 = QFrame(self.frame_currently_opened)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(0, 0))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_44.addWidget(self.frame_42)


        self.verticalLayout_3.addWidget(self.frame_currently_opened)

        self.all_pages = QStackedWidget(self.center_main_items)
        self.all_pages.setObjectName(u"all_pages")
        self.investment_page = QWidget()
        self.investment_page.setObjectName(u"investment_page")
        self.verticalLayout_16 = QVBoxLayout(self.investment_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.scrollArea_current_investment = QScrollArea(self.investment_page)
        self.scrollArea_current_investment.setObjectName(u"scrollArea_current_investment")
        self.scrollArea_current_investment.setStyleSheet(u"#scrollArea {\n"
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
        self.scrollArea_current_investment.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -472, 812, 2794))
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContainer{\n"
"border: 3px solid gray;\n"
"border-radius: 8px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 24, -1)
        self.frame_main_characteristics = QFrame(self.scrollAreaWidgetContents)
        self.frame_main_characteristics.setObjectName(u"frame_main_characteristics")
        self.frame_main_characteristics.setMinimumSize(QSize(0, 80))
        self.frame_main_characteristics.setMaximumSize(QSize(16777215, 80))
        self.frame_main_characteristics.setFrameShape(QFrame.StyledPanel)
        self.frame_main_characteristics.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_main_characteristics)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_15 = QFrame(self.frame_main_characteristics)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_11 = QLabel(self.frame_15)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_16.addWidget(self.label_11)

        self.textEdit_11 = QTextEdit(self.frame_15)
        self.textEdit_11.setObjectName(u"textEdit_11")

        self.horizontalLayout_16.addWidget(self.textEdit_11)


        self.horizontalLayout_6.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_main_characteristics)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_12 = QLabel(self.frame_16)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_17.addWidget(self.label_12)

        self.textEdit_12 = QTextEdit(self.frame_16)
        self.textEdit_12.setObjectName(u"textEdit_12")

        self.horizontalLayout_17.addWidget(self.textEdit_12)


        self.horizontalLayout_6.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_main_characteristics)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_18.addWidget(self.label_13)

        self.textEdit_13 = QTextEdit(self.frame_17)
        self.textEdit_13.setObjectName(u"textEdit_13")

        self.horizontalLayout_18.addWidget(self.textEdit_13)


        self.horizontalLayout_6.addWidget(self.frame_17)


        self.verticalLayout_2.addWidget(self.frame_main_characteristics)

        self.frame_information = QFrame(self.scrollAreaWidgetContents)
        self.frame_information.setObjectName(u"frame_information")
        self.frame_information.setMinimumSize(QSize(300, 400))
        self.frame_information.setFrameShape(QFrame.StyledPanel)
        self.frame_information.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_information)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 2, -1, 2)
        self.button_information = QPushButton(self.frame_information)
        self.button_information.setObjectName(u"button_information")
        self.button_information.setMinimumSize(QSize(0, 24))

        self.verticalLayout_4.addWidget(self.button_information)

        self.frame_information_data = QFrame(self.frame_information)
        self.frame_information_data.setObjectName(u"frame_information_data")
        self.frame_information_data.setMinimumSize(QSize(0, 210))
        self.frame_information_data.setFrameShape(QFrame.StyledPanel)
        self.frame_information_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_information_data)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(4, 4, 4, 4)
        self.frame_18 = QFrame(self.frame_information_data)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(12, 2, -1, 2)
        self.label_14 = QLabel(self.frame_18)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_19.addWidget(self.label_14)

        self.textEdit_14 = QTextEdit(self.frame_18)
        self.textEdit_14.setObjectName(u"textEdit_14")

        self.horizontalLayout_19.addWidget(self.textEdit_14)


        self.verticalLayout_13.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_information_data)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 2, -1, 2)
        self.label_15 = QLabel(self.frame_19)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_20.addWidget(self.label_15)

        self.textEdit_15 = QTextEdit(self.frame_19)
        self.textEdit_15.setObjectName(u"textEdit_15")

        self.horizontalLayout_20.addWidget(self.textEdit_15)


        self.verticalLayout_13.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_information_data)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 2, -1, 2)
        self.label_16 = QLabel(self.frame_20)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_21.addWidget(self.label_16)

        self.textEdit_16 = QTextEdit(self.frame_20)
        self.textEdit_16.setObjectName(u"textEdit_16")

        self.horizontalLayout_21.addWidget(self.textEdit_16)


        self.verticalLayout_13.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_information_data)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 2, -1, 2)
        self.label_17 = QLabel(self.frame_21)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_22.addWidget(self.label_17)

        self.textEdit_17 = QTextEdit(self.frame_21)
        self.textEdit_17.setObjectName(u"textEdit_17")

        self.horizontalLayout_22.addWidget(self.textEdit_17)


        self.verticalLayout_13.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_information_data)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 2, -1, 2)
        self.label_18 = QLabel(self.frame_22)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_23.addWidget(self.label_18)

        self.textEdit_18 = QTextEdit(self.frame_22)
        self.textEdit_18.setObjectName(u"textEdit_18")

        self.horizontalLayout_23.addWidget(self.textEdit_18)


        self.verticalLayout_13.addWidget(self.frame_22)

        self.frame_7 = QFrame(self.frame_information_data)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 2, -1, 2)
        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_24.addWidget(self.label_19)

        self.textEdit_19 = QTextEdit(self.frame_7)
        self.textEdit_19.setObjectName(u"textEdit_19")

        self.horizontalLayout_24.addWidget(self.textEdit_19)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_information_data)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 2, -1, 2)
        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_25.addWidget(self.label_20)

        self.textEdit_20 = QTextEdit(self.frame_8)
        self.textEdit_20.setObjectName(u"textEdit_20")

        self.horizontalLayout_25.addWidget(self.textEdit_20)


        self.verticalLayout_13.addWidget(self.frame_8)


        self.verticalLayout_4.addWidget(self.frame_information_data)


        self.verticalLayout_2.addWidget(self.frame_information)

        self.frame_own_contribution = QFrame(self.scrollAreaWidgetContents)
        self.frame_own_contribution.setObjectName(u"frame_own_contribution")
        self.frame_own_contribution.setMinimumSize(QSize(630, 500))
        self.frame_own_contribution.setFrameShape(QFrame.StyledPanel)
        self.frame_own_contribution.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_own_contribution)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.button_own_contribution = QPushButton(self.frame_own_contribution)
        self.button_own_contribution.setObjectName(u"button_own_contribution")
        self.button_own_contribution.setMinimumSize(QSize(0, 24))

        self.verticalLayout_5.addWidget(self.button_own_contribution)

        self.frame_own_contribution_data = QFrame(self.frame_own_contribution)
        self.frame_own_contribution_data.setObjectName(u"frame_own_contribution_data")
        self.frame_own_contribution_data.setMinimumSize(QSize(0, 250))
        self.frame_own_contribution_data.setStyleSheet(u"QFrame{\n"
"border: 1px solid gray;\n"
"border-radius: 2px;\n"
"background: rgb(207, 206, 209);\n"
"}")
        self.frame_own_contribution_data.setFrameShape(QFrame.StyledPanel)
        self.frame_own_contribution_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_own_contribution_data)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 2, -1, 2)
        self.frame_3 = QFrame(self.frame_own_contribution_data)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 2, -1, 2)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(138, 0))

        self.horizontalLayout_5.addWidget(self.label)

        self.textEdit_9 = QTextEdit(self.frame_3)
        self.textEdit_9.setObjectName(u"textEdit_9")

        self.horizontalLayout_5.addWidget(self.textEdit_9)

        self.textEdit = QTextEdit(self.frame_3)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_5.addWidget(self.textEdit)


        self.verticalLayout_9.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame_own_contribution_data)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 2, -1, 2)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(138, 0))

        self.horizontalLayout_7.addWidget(self.label_2)

        self.textEdit_10 = QTextEdit(self.frame_6)
        self.textEdit_10.setObjectName(u"textEdit_10")

        self.horizontalLayout_7.addWidget(self.textEdit_10)

        self.textEdit_2 = QTextEdit(self.frame_6)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.horizontalLayout_7.addWidget(self.textEdit_2)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.frame_own_contribution_data)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 2, -1, 2)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(138, 0))

        self.horizontalLayout_8.addWidget(self.label_3)

        self.textEdit_21 = QTextEdit(self.frame_9)
        self.textEdit_21.setObjectName(u"textEdit_21")

        self.horizontalLayout_8.addWidget(self.textEdit_21)

        self.textEdit_3 = QTextEdit(self.frame_9)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.horizontalLayout_8.addWidget(self.textEdit_3)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_own_contribution_data)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 2, -1, 2)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(138, 0))

        self.horizontalLayout_9.addWidget(self.label_4)

        self.textEdit_22 = QTextEdit(self.frame_5)
        self.textEdit_22.setObjectName(u"textEdit_22")

        self.horizontalLayout_9.addWidget(self.textEdit_22)

        self.textEdit_6 = QTextEdit(self.frame_5)
        self.textEdit_6.setObjectName(u"textEdit_6")

        self.horizontalLayout_9.addWidget(self.textEdit_6)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.frame_10 = QFrame(self.frame_own_contribution_data)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 2, -1, 2)
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(138, 0))

        self.horizontalLayout_10.addWidget(self.label_5)

        self.textEdit_23 = QTextEdit(self.frame_10)
        self.textEdit_23.setObjectName(u"textEdit_23")

        self.horizontalLayout_10.addWidget(self.textEdit_23)

        self.textEdit_4 = QTextEdit(self.frame_10)
        self.textEdit_4.setObjectName(u"textEdit_4")

        self.horizontalLayout_10.addWidget(self.textEdit_4)


        self.verticalLayout_9.addWidget(self.frame_10)

        self.frame_4 = QFrame(self.frame_own_contribution_data)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 2, -1, 2)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(138, 0))

        self.horizontalLayout_11.addWidget(self.label_6)

        self.textEdit_24 = QTextEdit(self.frame_4)
        self.textEdit_24.setObjectName(u"textEdit_24")

        self.horizontalLayout_11.addWidget(self.textEdit_24)

        self.textEdit_7 = QTextEdit(self.frame_4)
        self.textEdit_7.setObjectName(u"textEdit_7")

        self.horizontalLayout_11.addWidget(self.textEdit_7)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.frame = QFrame(self.frame_own_contribution_data)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 2, -1, 2)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(138, 0))

        self.horizontalLayout_12.addWidget(self.label_7)

        self.textEdit_5 = QTextEdit(self.frame)
        self.textEdit_5.setObjectName(u"textEdit_5")

        self.horizontalLayout_12.addWidget(self.textEdit_5)


        self.verticalLayout_9.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_own_contribution_data)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 2, -1, 2)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(138, 0))

        self.horizontalLayout_13.addWidget(self.label_8)

        self.textEdit_8 = QTextEdit(self.frame_2)
        self.textEdit_8.setObjectName(u"textEdit_8")

        self.horizontalLayout_13.addWidget(self.textEdit_8)


        self.verticalLayout_9.addWidget(self.frame_2)


        self.verticalLayout_5.addWidget(self.frame_own_contribution_data)


        self.verticalLayout_2.addWidget(self.frame_own_contribution)

        self.frame_credit = QFrame(self.scrollAreaWidgetContents)
        self.frame_credit.setObjectName(u"frame_credit")
        self.frame_credit.setMinimumSize(QSize(630, 560))
        self.frame_credit.setFrameShape(QFrame.StyledPanel)
        self.frame_credit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_credit)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.button_credit = QPushButton(self.frame_credit)
        self.button_credit.setObjectName(u"button_credit")
        self.button_credit.setMinimumSize(QSize(0, 24))

        self.verticalLayout_6.addWidget(self.button_credit)

        self.frame_credit_data = QFrame(self.frame_credit)
        self.frame_credit_data.setObjectName(u"frame_credit_data")
        self.frame_credit_data.setFrameShape(QFrame.StyledPanel)
        self.frame_credit_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_credit_data)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 2, -1, 2)
        self.frame_11 = QFrame(self.frame_credit_data)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 40))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 2, -1, 2)
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(195, 0))

        self.horizontalLayout_14.addWidget(self.label_9)

        self.textEdit_25 = QTextEdit(self.frame_11)
        self.textEdit_25.setObjectName(u"textEdit_25")

        self.horizontalLayout_14.addWidget(self.textEdit_25)


        self.verticalLayout_10.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_credit_data)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 40))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 2, -1, 2)
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(195, 0))

        self.horizontalLayout_15.addWidget(self.label_10)

        self.textEdit_26 = QTextEdit(self.frame_12)
        self.textEdit_26.setObjectName(u"textEdit_26")

        self.horizontalLayout_15.addWidget(self.textEdit_26)


        self.verticalLayout_10.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_credit_data)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 40))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 2, -1, 2)
        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(195, 0))

        self.horizontalLayout_26.addWidget(self.label_21)

        self.textEdit_33 = QTextEdit(self.frame_13)
        self.textEdit_33.setObjectName(u"textEdit_33")

        self.horizontalLayout_26.addWidget(self.textEdit_33)


        self.verticalLayout_10.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_credit_data)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 40))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 2, -1, 2)
        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(195, 0))

        self.horizontalLayout_27.addWidget(self.label_22)

        self.textEdit_27 = QTextEdit(self.frame_14)
        self.textEdit_27.setObjectName(u"textEdit_27")

        self.horizontalLayout_27.addWidget(self.textEdit_27)


        self.verticalLayout_10.addWidget(self.frame_14)

        self.frame_23 = QFrame(self.frame_credit_data)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 120))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_23)
        self.verticalLayout_11.setSpacing(1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 2, -1, 2)
        self.frame_28 = QFrame(self.frame_23)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, 2, -1, 2)
        self.label_23 = QLabel(self.frame_28)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(185, 0))

        self.horizontalLayout_28.addWidget(self.label_23)

        self.textEdit_28 = QTextEdit(self.frame_28)
        self.textEdit_28.setObjectName(u"textEdit_28")

        self.horizontalLayout_28.addWidget(self.textEdit_28)


        self.verticalLayout_11.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_23)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 2, -1, 2)
        self.label_28 = QLabel(self.frame_29)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(185, 0))

        self.horizontalLayout_33.addWidget(self.label_28)

        self.textEdit_34 = QTextEdit(self.frame_29)
        self.textEdit_34.setObjectName(u"textEdit_34")

        self.horizontalLayout_33.addWidget(self.textEdit_34)


        self.verticalLayout_11.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_23)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(-1, 2, -1, 2)
        self.label_29 = QLabel(self.frame_30)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(185, 0))

        self.horizontalLayout_34.addWidget(self.label_29)

        self.textEdit_35 = QTextEdit(self.frame_30)
        self.textEdit_35.setObjectName(u"textEdit_35")

        self.horizontalLayout_34.addWidget(self.textEdit_35)


        self.verticalLayout_11.addWidget(self.frame_30)


        self.verticalLayout_10.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_credit_data)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 40))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 2, -1, 2)
        self.label_24 = QLabel(self.frame_24)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_29.addWidget(self.label_24)

        self.textEdit_29 = QTextEdit(self.frame_24)
        self.textEdit_29.setObjectName(u"textEdit_29")

        self.horizontalLayout_29.addWidget(self.textEdit_29)


        self.verticalLayout_10.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_credit_data)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 40))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 2, -1, 2)
        self.label_25 = QLabel(self.frame_25)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(195, 0))

        self.horizontalLayout_30.addWidget(self.label_25)

        self.textEdit_30 = QTextEdit(self.frame_25)
        self.textEdit_30.setObjectName(u"textEdit_30")

        self.horizontalLayout_30.addWidget(self.textEdit_30)


        self.verticalLayout_10.addWidget(self.frame_25)


        self.verticalLayout_6.addWidget(self.frame_credit_data)


        self.verticalLayout_2.addWidget(self.frame_credit)

        self.frame_rent = QFrame(self.scrollAreaWidgetContents)
        self.frame_rent.setObjectName(u"frame_rent")
        self.frame_rent.setMinimumSize(QSize(630, 750))
        self.frame_rent.setFrameShape(QFrame.StyledPanel)
        self.frame_rent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_rent)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.button_rent = QPushButton(self.frame_rent)
        self.button_rent.setObjectName(u"button_rent")
        self.button_rent.setMinimumSize(QSize(0, 24))

        self.verticalLayout_7.addWidget(self.button_rent)

        self.frame_rent_data = QFrame(self.frame_rent)
        self.frame_rent_data.setObjectName(u"frame_rent_data")
        self.frame_rent_data.setFrameShape(QFrame.StyledPanel)
        self.frame_rent_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_rent_data)
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 2, -1, 2)
        self.frame_rent_header = QFrame(self.frame_rent_data)
        self.frame_rent_header.setObjectName(u"frame_rent_header")
        self.frame_rent_header.setMinimumSize(QSize(0, 30))
        self.frame_rent_header.setStyleSheet(u"#frame_rent_header{\n"
"border: 1px solid gray;\n"
"border-radius: 10px;\n"
"background: rgb(207, 206, 209);\n"
"}\n"
"QLabel{\n"
"border: 1px white;\n"
"}")
        self.frame_rent_header.setFrameShape(QFrame.StyledPanel)
        self.frame_rent_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_rent_header)
#ifndef Q_OS_MAC
        self.horizontalLayout_43.setSpacing(-1)
#endif
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, 2, -1, 2)
        self.horizontalSpacer_2 = QSpacerItem(185, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_2)

        self.label_40 = QLabel(self.frame_rent_header)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(0, 20))
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_rent_header)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 20))
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_41)

        self.label_42 = QLabel(self.frame_rent_header)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 20))
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_42)


        self.verticalLayout_12.addWidget(self.frame_rent_header)

        self.frame_rent_data_income = QFrame(self.frame_rent_data)
        self.frame_rent_data_income.setObjectName(u"frame_rent_data_income")
        self.frame_rent_data_income.setMinimumSize(QSize(0, 130))
        self.frame_rent_data_income.setFrameShape(QFrame.StyledPanel)
        self.frame_rent_data_income.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_rent_data_income)
        self.verticalLayout_14.setSpacing(2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 2, -1, 2)
        self.label_26 = QLabel(self.frame_rent_data_income)
        self.label_26.setObjectName(u"label_26")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setLayoutDirection(Qt.LeftToRight)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_26)

        self.frame_31 = QFrame(self.frame_rent_data_income)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, 2, -1, 2)
        self.label_37 = QLabel(self.frame_31)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_31.addWidget(self.label_37)

        self.textEdit_31 = QTextEdit(self.frame_31)
        self.textEdit_31.setObjectName(u"textEdit_31")

        self.horizontalLayout_31.addWidget(self.textEdit_31)

        self.textEdit_32 = QTextEdit(self.frame_31)
        self.textEdit_32.setObjectName(u"textEdit_32")

        self.horizontalLayout_31.addWidget(self.textEdit_32)

        self.textEdit_36 = QTextEdit(self.frame_31)
        self.textEdit_36.setObjectName(u"textEdit_36")

        self.horizontalLayout_31.addWidget(self.textEdit_36)


        self.verticalLayout_14.addWidget(self.frame_31)

        self.frame_34 = QFrame(self.frame_rent_data_income)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, 2, -1, 2)
        self.label_38 = QLabel(self.frame_34)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_32.addWidget(self.label_38)

        self.textEdit_37 = QTextEdit(self.frame_34)
        self.textEdit_37.setObjectName(u"textEdit_37")

        self.horizontalLayout_32.addWidget(self.textEdit_37)

        self.textEdit_38 = QTextEdit(self.frame_34)
        self.textEdit_38.setObjectName(u"textEdit_38")

        self.horizontalLayout_32.addWidget(self.textEdit_38)

        self.textEdit_39 = QTextEdit(self.frame_34)
        self.textEdit_39.setObjectName(u"textEdit_39")

        self.horizontalLayout_32.addWidget(self.textEdit_39)


        self.verticalLayout_14.addWidget(self.frame_34)

        self.frame_33 = QFrame(self.frame_rent_data_income)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(-1, 2, -1, 2)
        self.label_39 = QLabel(self.frame_33)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_35.addWidget(self.label_39)

        self.textEdit_40 = QTextEdit(self.frame_33)
        self.textEdit_40.setObjectName(u"textEdit_40")

        self.horizontalLayout_35.addWidget(self.textEdit_40)

        self.textEdit_41 = QTextEdit(self.frame_33)
        self.textEdit_41.setObjectName(u"textEdit_41")

        self.horizontalLayout_35.addWidget(self.textEdit_41)

        self.textEdit_42 = QTextEdit(self.frame_33)
        self.textEdit_42.setObjectName(u"textEdit_42")

        self.horizontalLayout_35.addWidget(self.textEdit_42)


        self.verticalLayout_14.addWidget(self.frame_33)


        self.verticalLayout_12.addWidget(self.frame_rent_data_income)

        self.frame_rent_data_cost = QFrame(self.frame_rent_data)
        self.frame_rent_data_cost.setObjectName(u"frame_rent_data_cost")
        self.frame_rent_data_cost.setMinimumSize(QSize(0, 450))
        self.frame_rent_data_cost.setFrameShape(QFrame.StyledPanel)
        self.frame_rent_data_cost.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_rent_data_cost)
        self.verticalLayout_15.setSpacing(2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 2, -1, 2)
        self.label_27 = QLabel(self.frame_rent_data_cost)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QSize(0, 30))
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_27)

        self.frame_35 = QFrame(self.frame_rent_data_cost)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, 2, -1, 2)
        self.label_30 = QLabel(self.frame_35)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_36.addWidget(self.label_30)

        self.textEdit_43 = QTextEdit(self.frame_35)
        self.textEdit_43.setObjectName(u"textEdit_43")

        self.horizontalLayout_36.addWidget(self.textEdit_43)

        self.textEdit_44 = QTextEdit(self.frame_35)
        self.textEdit_44.setObjectName(u"textEdit_44")

        self.horizontalLayout_36.addWidget(self.textEdit_44)

        self.textEdit_45 = QTextEdit(self.frame_35)
        self.textEdit_45.setObjectName(u"textEdit_45")

        self.horizontalLayout_36.addWidget(self.textEdit_45)


        self.verticalLayout_15.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_rent_data_cost)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, 2, -1, 2)
        self.label_31 = QLabel(self.frame_36)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_37.addWidget(self.label_31)

        self.textEdit_46 = QTextEdit(self.frame_36)
        self.textEdit_46.setObjectName(u"textEdit_46")

        self.horizontalLayout_37.addWidget(self.textEdit_46)

        self.textEdit_47 = QTextEdit(self.frame_36)
        self.textEdit_47.setObjectName(u"textEdit_47")

        self.horizontalLayout_37.addWidget(self.textEdit_47)

        self.textEdit_48 = QTextEdit(self.frame_36)
        self.textEdit_48.setObjectName(u"textEdit_48")

        self.horizontalLayout_37.addWidget(self.textEdit_48)


        self.verticalLayout_15.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_rent_data_cost)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, 2, -1, 2)
        self.label_32 = QLabel(self.frame_37)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_38.addWidget(self.label_32)

        self.textEdit_49 = QTextEdit(self.frame_37)
        self.textEdit_49.setObjectName(u"textEdit_49")

        self.horizontalLayout_38.addWidget(self.textEdit_49)

        self.textEdit_50 = QTextEdit(self.frame_37)
        self.textEdit_50.setObjectName(u"textEdit_50")

        self.horizontalLayout_38.addWidget(self.textEdit_50)

        self.textEdit_51 = QTextEdit(self.frame_37)
        self.textEdit_51.setObjectName(u"textEdit_51")

        self.horizontalLayout_38.addWidget(self.textEdit_51)


        self.verticalLayout_15.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_rent_data_cost)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(-1, 2, -1, 2)
        self.label_33 = QLabel(self.frame_38)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_39.addWidget(self.label_33)

        self.textEdit_54 = QTextEdit(self.frame_38)
        self.textEdit_54.setObjectName(u"textEdit_54")

        self.horizontalLayout_39.addWidget(self.textEdit_54)

        self.textEdit_53 = QTextEdit(self.frame_38)
        self.textEdit_53.setObjectName(u"textEdit_53")

        self.horizontalLayout_39.addWidget(self.textEdit_53)

        self.textEdit_52 = QTextEdit(self.frame_38)
        self.textEdit_52.setObjectName(u"textEdit_52")

        self.horizontalLayout_39.addWidget(self.textEdit_52)


        self.verticalLayout_15.addWidget(self.frame_38)

        self.frame_40 = QFrame(self.frame_rent_data_cost)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(-1, 2, -1, 2)
        self.label_34 = QLabel(self.frame_40)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_40.addWidget(self.label_34)

        self.textEdit_57 = QTextEdit(self.frame_40)
        self.textEdit_57.setObjectName(u"textEdit_57")

        self.horizontalLayout_40.addWidget(self.textEdit_57)

        self.textEdit_56 = QTextEdit(self.frame_40)
        self.textEdit_56.setObjectName(u"textEdit_56")

        self.horizontalLayout_40.addWidget(self.textEdit_56)

        self.textEdit_55 = QTextEdit(self.frame_40)
        self.textEdit_55.setObjectName(u"textEdit_55")

        self.horizontalLayout_40.addWidget(self.textEdit_55)


        self.verticalLayout_15.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_rent_data_cost)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(-1, 2, -1, 2)
        self.label_35 = QLabel(self.frame_41)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_41.addWidget(self.label_35)

        self.textEdit_60 = QTextEdit(self.frame_41)
        self.textEdit_60.setObjectName(u"textEdit_60")

        self.horizontalLayout_41.addWidget(self.textEdit_60)

        self.textEdit_59 = QTextEdit(self.frame_41)
        self.textEdit_59.setObjectName(u"textEdit_59")

        self.horizontalLayout_41.addWidget(self.textEdit_59)

        self.textEdit_58 = QTextEdit(self.frame_41)
        self.textEdit_58.setObjectName(u"textEdit_58")

        self.horizontalLayout_41.addWidget(self.textEdit_58)


        self.verticalLayout_15.addWidget(self.frame_41)

        self.frame_39 = QFrame(self.frame_rent_data_cost)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(-1, 2, -1, 2)
        self.label_36 = QLabel(self.frame_39)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_42.addWidget(self.label_36)

        self.textEdit_63 = QTextEdit(self.frame_39)
        self.textEdit_63.setObjectName(u"textEdit_63")

        self.horizontalLayout_42.addWidget(self.textEdit_63)

        self.textEdit_62 = QTextEdit(self.frame_39)
        self.textEdit_62.setObjectName(u"textEdit_62")

        self.horizontalLayout_42.addWidget(self.textEdit_62)

        self.textEdit_61 = QTextEdit(self.frame_39)
        self.textEdit_61.setObjectName(u"textEdit_61")

        self.horizontalLayout_42.addWidget(self.textEdit_61)


        self.verticalLayout_15.addWidget(self.frame_39)

        self.frame_26 = QFrame(self.frame_rent_data_cost)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(-1, 2, -1, 2)
        self.label_47 = QLabel(self.frame_26)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_46.addWidget(self.label_47)

        self.textEdit_64 = QTextEdit(self.frame_26)
        self.textEdit_64.setObjectName(u"textEdit_64")

        self.horizontalLayout_46.addWidget(self.textEdit_64)

        self.textEdit_65 = QTextEdit(self.frame_26)
        self.textEdit_65.setObjectName(u"textEdit_65")

        self.horizontalLayout_46.addWidget(self.textEdit_65)

        self.horizontalSpacer_4 = QSpacerItem(255, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_4)


        self.verticalLayout_15.addWidget(self.frame_26)


        self.verticalLayout_12.addWidget(self.frame_rent_data_cost)

        self.frame_32 = QFrame(self.frame_rent_data)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 55))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(-1, 2, -1, 2)
        self.label_48 = QLabel(self.frame_32)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(190, 0))

        self.horizontalLayout_47.addWidget(self.label_48)

        self.textEdit_66 = QTextEdit(self.frame_32)
        self.textEdit_66.setObjectName(u"textEdit_66")

        self.horizontalLayout_47.addWidget(self.textEdit_66)

        self.textEdit_67 = QTextEdit(self.frame_32)
        self.textEdit_67.setObjectName(u"textEdit_67")

        self.horizontalLayout_47.addWidget(self.textEdit_67)

        self.horizontalSpacer_5 = QSpacerItem(265, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_5)


        self.verticalLayout_12.addWidget(self.frame_32)


        self.verticalLayout_7.addWidget(self.frame_rent_data)


        self.verticalLayout_2.addWidget(self.frame_rent)

        self.frame_investment_assessment = QFrame(self.scrollAreaWidgetContents)
        self.frame_investment_assessment.setObjectName(u"frame_investment_assessment")
        self.frame_investment_assessment.setMinimumSize(QSize(630, 400))
        self.frame_investment_assessment.setFrameShape(QFrame.StyledPanel)
        self.frame_investment_assessment.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_investment_assessment)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.button_investment_assessment = QPushButton(self.frame_investment_assessment)
        self.button_investment_assessment.setObjectName(u"button_investment_assessment")
        self.button_investment_assessment.setMinimumSize(QSize(0, 24))

        self.verticalLayout_8.addWidget(self.button_investment_assessment)

        self.frame_investment_assessment_data = QFrame(self.frame_investment_assessment)
        self.frame_investment_assessment_data.setObjectName(u"frame_investment_assessment_data")
        self.frame_investment_assessment_data.setFrameShape(QFrame.StyledPanel)
        self.frame_investment_assessment_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_investment_assessment_data)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_investment_assessment_header = QFrame(self.frame_investment_assessment_data)
        self.frame_investment_assessment_header.setObjectName(u"frame_investment_assessment_header")
        self.frame_investment_assessment_header.setMinimumSize(QSize(0, 30))
        self.frame_investment_assessment_header.setStyleSheet(u"#frame_rent_header{\n"
"border: 1px solid gray;\n"
"border-radius: 10px;\n"
"background: rgb(207, 206, 209);\n"
"}\n"
"QLabel{\n"
"border: 1px white;\n"
"}")
        self.frame_investment_assessment_header.setFrameShape(QFrame.StyledPanel)
        self.frame_investment_assessment_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_investment_assessment_header)
#ifndef Q_OS_MAC
        self.horizontalLayout_45.setSpacing(-1)
#endif
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(-1, 2, -1, 2)
        self.horizontalSpacer_3 = QSpacerItem(267, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_3)

        self.label_43 = QLabel(self.frame_investment_assessment_header)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(0, 20))
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.label_43)

        self.label_44 = QLabel(self.frame_investment_assessment_header)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(0, 20))
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.label_44)

        self.label_46 = QLabel(self.frame_investment_assessment_header)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 20))
        self.label_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.label_46)


        self.verticalLayout_17.addWidget(self.frame_investment_assessment_header)

        self.frame_44 = QFrame(self.frame_investment_assessment_data)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_44)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 2, -1, 2)
        self.frame_27 = QFrame(self.frame_44)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 40))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(-1, 2, -1, 2)
        self.label_49 = QLabel(self.frame_27)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(267, 0))

        self.horizontalLayout_48.addWidget(self.label_49)

        self.label_53 = QLabel(self.frame_27)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_48.addWidget(self.label_53)

        self.label_57 = QLabel(self.frame_27)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_48.addWidget(self.label_57)

        self.label_61 = QLabel(self.frame_27)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_48.addWidget(self.label_61)


        self.verticalLayout_19.addWidget(self.frame_27)

        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(0, 40))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(-1, 2, -1, 2)
        self.label_50 = QLabel(self.frame_46)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(267, 0))

        self.horizontalLayout_49.addWidget(self.label_50)

        self.label_54 = QLabel(self.frame_46)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_49.addWidget(self.label_54)

        self.label_58 = QLabel(self.frame_46)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_49.addWidget(self.label_58)

        self.label_62 = QLabel(self.frame_46)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_49.addWidget(self.label_62)


        self.verticalLayout_19.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.frame_44)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 40))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(-1, 2, -1, 2)
        self.label_51 = QLabel(self.frame_47)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(267, 0))

        self.horizontalLayout_50.addWidget(self.label_51)

        self.label_55 = QLabel(self.frame_47)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_50.addWidget(self.label_55)

        self.label_59 = QLabel(self.frame_47)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_50.addWidget(self.label_59)

        self.label_63 = QLabel(self.frame_47)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_50.addWidget(self.label_63)


        self.verticalLayout_19.addWidget(self.frame_47)

        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 40))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(-1, 2, -1, 2)
        self.label_52 = QLabel(self.frame_45)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(267, 0))

        self.horizontalLayout_51.addWidget(self.label_52)

        self.label_56 = QLabel(self.frame_45)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_51.addWidget(self.label_56)

        self.label_60 = QLabel(self.frame_45)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_51.addWidget(self.label_60)

        self.label_64 = QLabel(self.frame_45)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_51.addWidget(self.label_64)


        self.verticalLayout_19.addWidget(self.frame_45)


        self.verticalLayout_17.addWidget(self.frame_44)


        self.verticalLayout_8.addWidget(self.frame_investment_assessment_data)


        self.verticalLayout_2.addWidget(self.frame_investment_assessment)

        self.scrollArea_current_investment.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_16.addWidget(self.scrollArea_current_investment)

        self.all_pages.addWidget(self.investment_page)
        self.new_investment_page = QWidget()
        self.new_investment_page.setObjectName(u"new_investment_page")
        self.frame_43 = QFrame(self.new_investment_page)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setGeometry(QRect(0, 20, 831, 521))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.all_pages.addWidget(self.new_investment_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.label_45 = QLabel(self.home_page)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(150, 20, 471, 16))
        self.all_pages.addWidget(self.home_page)

        self.verticalLayout_3.addWidget(self.all_pages)


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

        self.all_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minimizeButton.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.restoreButton.setText(QCoreApplication.translate("MainWindow", u"[]", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.button_load_data.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj\n"
"dane", None))
        self.button_save_data.setText(QCoreApplication.translate("MainWindow", u"Zapisz\n"
"dane", None))
        self.button_new_investment.setText(QCoreApplication.translate("MainWindow", u"Nowa", None))
        self.button_compare.setText(QCoreApplication.translate("MainWindow", u"Por\u00f3wnaj", None))
        self.button_home_page.setText(QCoreApplication.translate("MainWindow", u"Strona \n"
"g\u0142\u00f3wna", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Cena zakupu", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"POW. [m\u00b2]", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Cena/m\u00b2", None))
        self.button_information.setText(QCoreApplication.translate("MainWindow", u"Informacje", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Data rozpocz\u0119cia", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Opis", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Adres - ulica, numer", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Adres - miejscowo\u015b\u0107", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Szac. warto\u015b\u0107 obecna", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Data ost. szacowania", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Data zako\u0144czenia", None))
        self.button_own_contribution.setText(QCoreApplication.translate("MainWindow", u"Wk\u0142ad w\u0142asny", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wk\u0142ad w\u0142asny", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mar\u017ca maklera ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mar\u017ca notariusza", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Podatek", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Inne koszty", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Remont", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Koszty wej\u015bcia razem", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cena zakupu", None))
        self.button_credit.setText(QCoreApplication.translate("MainWindow", u"Kredyt", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Kredyt bankowy", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Wk\u0142ad banku [%]", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Stopa procentowa", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Okres sp\u0142aty", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Rata miesi\u0119czna", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Cz\u0119\u015b\u0107 kapita\u0142owa", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Cz\u0119\u015b\u0107 odestkowa", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Ubezpieczenie kredytu/miesi\u0105c", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Koszty kredytowania razem", None))
        self.button_rent.setText(QCoreApplication.translate("MainWindow", u"Wynajem", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Na miesi\u0105c", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Na rok", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"PRZYCHODY", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Przychody z wynajmu (min)", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Przychody z wynajmu (max)", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Przychody uzyskane", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"KOSZTY", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Podatek od wynajmu", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Podatek od nieruchomo\u015bci", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Pr\u0105d", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Gaz", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Woda", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Internet", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Inne", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"KOSZTY RAZEM", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"ZYSK/STRATA Z WYNAJMU", None))
        self.button_investment_assessment.setText(QCoreApplication.translate("MainWindow", u"Ocena inwestycji", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Na miesi\u0105c", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Na rok", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Czas zwrotu kapita\u0142u w\u0142asnego z wynajmu", None))
        self.label_53.setText("")
        self.label_57.setText("")
        self.label_61.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Czas zwrotu kapita\u0142u \u0142\u0105cznie z kredytem", None))
        self.label_54.setText("")
        self.label_58.setText("")
        self.label_62.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Stopa zwrotu kapita\u0142u w\u0142asnego z wynajmu", None))
        self.label_55.setText("")
        self.label_59.setText("")
        self.label_63.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Stopa zwrotu kapita\u0142u \u0142\u0105cznie z kredytem", None))
        self.label_56.setText("")
        self.label_60.setText("")
        self.label_64.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Witamy na stronie g\u0142\u00f3wnej", None))
    # retranslateUi

