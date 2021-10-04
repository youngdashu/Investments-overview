from typing import List

from PySide6.QtWidgets import QFrame

noBorderFrameStyleSheetTemplate = """{
        border: 0px solid gray;
        border-radius: 10px;
        background: rgb(207, 206, 209);
        }"""


def setProperStyleSheet(frame: QFrame):
    frame.setStyleSheet("#" + frame.objectName() + noBorderFrameStyleSheetTemplate)
    return frame


def removeExcessiveBorders(frames: List[QFrame]):
    return list(map(setProperStyleSheet, frames))


def disconnectFunction(editableTextEdit):
    editableTextEdit.textChanged.disconnect()
    return editableTextEdit
