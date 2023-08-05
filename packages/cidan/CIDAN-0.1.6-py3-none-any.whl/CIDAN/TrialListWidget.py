from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore
import os
class TrialListWidget(QWidget):
    def __init__(self):

        self.trial_paths = []
        self.trial_items = []

        super().__init__()
        self.list = QListWidget()
        self.setStyleSheet("QListView::item { border-bottom: 1px solid rgb(50, 65, " +
                           "75); }")
        self.top_labels_layout = QHBoxLayout()
        label1 = QLabel(text="Trial Selection")
        self.top_labels_layout.addWidget(label1)
        label1.setStyleSheet("font-size:20")


        self.model = QStandardItemModel(self.list)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.top_labels_layout)
        self.layout.addWidget(self.list)
        self.roi_item_list = []
        self.setLayout(self.layout)
    def setItems(self, folder_path):
        """
        Takes in a folder path and adds the trials to the list view
        Parameters
        ----------
        folder_path path to folder

        Returns
        -------
        Nothing
        """
        self.list.clear()
        self.trial_items = []
        self.trial_paths = sorted(os.listdir(folder_path))
        for path in self.trial_paths:
            self.trial_items.append(QListWidgetItem(path,self.list))
            self.trial_items[-1].setFlags(self.trial_items[-1].flags() | QtCore.Qt.ItemIsUserCheckable)
            self.trial_items[-1].setCheckState(QtCore.Qt.Checked)

    def selectedTrials(self):
        return [self.trial_paths[x[0]] for x in enumerate(self.trial_items)
                if x[1].checkState() == Qt.CheckState.Checked]