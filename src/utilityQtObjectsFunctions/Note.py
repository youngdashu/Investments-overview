from typing import List

from PySide6.QtWidgets import QTextEdit, QFrame, QPushButton


class Note:

    def __init__(self, noteStr: str, noteTextEdit: QTextEdit, frame: QFrame, deleteButton: QPushButton, index: int,
                 notesStr: List[str], notes: List):
        self.noteStr: str = noteStr
        self.noteTextEdit: QTextEdit = noteTextEdit
        self.frame: QFrame = frame
        self.deleteButton: QPushButton = deleteButton
        self.index: int = index
        self.notesStr: List[str] = notesStr
        self.notes = notes

    def deleteNote(self):

        self.notesStr[self.index] = None
        self.notes[self.index] = None
        self.frame.hide()
        self.deleteButton.deleteLater()
        self.noteTextEdit.deleteLater()
        self.frame.deleteLater()
        del self
