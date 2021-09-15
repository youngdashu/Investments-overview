# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UnsavedDialogTBSVxN.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_UnsavedDialog(object):
    def setupUi(self, UnsavedDialog):
        if not UnsavedDialog.objectName():
            UnsavedDialog.setObjectName(u"UnsavedDialog")
        UnsavedDialog.resize(290, 140)
        UnsavedDialog.setMinimumSize(QSize(290, 140))
        UnsavedDialog.setMaximumSize(QSize(300, 150))
        self.buttonBox = QDialogButtonBox(UnsavedDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(100, 60, 161, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.label = QLabel(UnsavedDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 261, 51))

        self.retranslateUi(UnsavedDialog)
        self.buttonBox.accepted.connect(UnsavedDialog.accept)
        self.buttonBox.rejected.connect(UnsavedDialog.reject)

        QMetaObject.connectSlotsByName(UnsavedDialog)
    # setupUi

    def retranslateUi(self, UnsavedDialog):
        UnsavedDialog.setWindowTitle(QCoreApplication.translate("UnsavedDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("UnsavedDialog", u"Czy chcesz zapisa\u0107 zmiany do inwestycji?", None))
    # retranslateUi

