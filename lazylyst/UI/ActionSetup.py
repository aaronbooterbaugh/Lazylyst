# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ActionSetup.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_actionDialog(object):
    def setupUi(self, actionDialog):
        actionDialog.setObjectName("actionDialog")
        actionDialog.resize(626, 626)
        self.verticalLayout = QtWidgets.QVBoxLayout(actionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.actShortInputLayout = QtWidgets.QGridLayout()
        self.actShortInputLayout.setSpacing(1)
        self.actShortInputLayout.setObjectName("actShortInputLayout")
        self.actOptionalsLabel = QtWidgets.QLabel(actionDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actOptionalsLabel.sizePolicy().hasHeightForWidth())
        self.actOptionalsLabel.setSizePolicy(sizePolicy)
        self.actOptionalsLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actOptionalsLabel.setFont(font)
        self.actOptionalsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actOptionalsLabel.setObjectName("actOptionalsLabel")
        self.actShortInputLayout.addWidget(self.actOptionalsLabel, 6, 1, 1, 1)
        self.actTriggerLineEdit = KeyBindLineEdit(actionDialog)
        self.actTriggerLineEdit.setObjectName("actTriggerLineEdit")
        self.actShortInputLayout.addWidget(self.actTriggerLineEdit, 2, 4, 1, 1)
        self.actTagLabel = QtWidgets.QLabel(actionDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actTagLabel.sizePolicy().hasHeightForWidth())
        self.actTagLabel.setSizePolicy(sizePolicy)
        self.actTagLabel.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actTagLabel.setFont(font)
        self.actTagLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actTagLabel.setObjectName("actTagLabel")
        self.actShortInputLayout.addWidget(self.actTagLabel, 0, 1, 1, 1)
        self.actNameLabel = QtWidgets.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actNameLabel.setFont(font)
        self.actNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actNameLabel.setObjectName("actNameLabel")
        self.actShortInputLayout.addWidget(self.actNameLabel, 2, 1, 1, 1)
        self.actPassiveRadio = QtWidgets.QRadioButton(actionDialog)
        self.actPassiveRadio.setChecked(True)
        self.actPassiveRadio.setObjectName("actPassiveRadio")
        self.actShortInputLayout.addWidget(self.actPassiveRadio, 6, 3, 1, 1)
        self.actOptionalsLineEdit = QtWidgets.QLineEdit(actionDialog)
        self.actOptionalsLineEdit.setObjectName("actOptionalsLineEdit")
        self.actShortInputLayout.addWidget(self.actOptionalsLineEdit, 6, 2, 1, 1)
        self.actIntervalLabel = QtWidgets.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actIntervalLabel.setFont(font)
        self.actIntervalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actIntervalLabel.setObjectName("actIntervalLabel")
        self.actShortInputLayout.addWidget(self.actIntervalLabel, 4, 3, 1, 1)
        self.actActiveRadio = QtWidgets.QRadioButton(actionDialog)
        self.actActiveRadio.setObjectName("actActiveRadio")
        self.actShortInputLayout.addWidget(self.actActiveRadio, 0, 3, 1, 1)
        self.actNameLineEdit = QtWidgets.QLineEdit(actionDialog)
        self.actNameLineEdit.setObjectName("actNameLineEdit")
        self.actShortInputLayout.addWidget(self.actNameLineEdit, 2, 2, 1, 1)
        self.passiveBeforeCheck = QtWidgets.QCheckBox(actionDialog)
        self.passiveBeforeCheck.setObjectName("passiveBeforeCheck")
        self.actShortInputLayout.addWidget(self.passiveBeforeCheck, 6, 4, 1, 1)
        self.actPathLabel = QtWidgets.QLabel(actionDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actPathLabel.sizePolicy().hasHeightForWidth())
        self.actPathLabel.setSizePolicy(sizePolicy)
        self.actPathLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actPathLabel.setFont(font)
        self.actPathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actPathLabel.setObjectName("actPathLabel")
        self.actShortInputLayout.addWidget(self.actPathLabel, 4, 1, 1, 1)
        self.actTagLineEdit = HoverLineEdit(actionDialog)
        self.actTagLineEdit.setObjectName("actTagLineEdit")
        self.actShortInputLayout.addWidget(self.actTagLineEdit, 0, 2, 1, 1)
        self.actPathLineEdit = QtWidgets.QLineEdit(actionDialog)
        self.actPathLineEdit.setObjectName("actPathLineEdit")
        self.actShortInputLayout.addWidget(self.actPathLineEdit, 4, 2, 1, 1)
        self.actTriggerLabel = QtWidgets.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actTriggerLabel.setFont(font)
        self.actTriggerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actTriggerLabel.setObjectName("actTriggerLabel")
        self.actShortInputLayout.addWidget(self.actTriggerLabel, 2, 3, 1, 1)
        self.actIntervalLineEdit = QtWidgets.QLineEdit(actionDialog)
        self.actIntervalLineEdit.setObjectName("actIntervalLineEdit")
        self.actShortInputLayout.addWidget(self.actIntervalLineEdit, 4, 4, 1, 1)
        self.actActiveCheckLayout = QtWidgets.QHBoxLayout()
        self.actActiveCheckLayout.setObjectName("actActiveCheckLayout")
        self.activeTimerCheck = QtWidgets.QCheckBox(actionDialog)
        self.activeTimerCheck.setObjectName("activeTimerCheck")
        self.actActiveCheckLayout.addWidget(self.activeTimerCheck)
        self.activeThreadedCheck = QtWidgets.QCheckBox(actionDialog)
        self.activeThreadedCheck.setObjectName("activeThreadedCheck")
        self.actActiveCheckLayout.addWidget(self.activeThreadedCheck)
        self.actShortInputLayout.addLayout(self.actActiveCheckLayout, 0, 4, 1, 1)
        self.actShortInputLayout.setColumnStretch(1, 1)
        self.actShortInputLayout.setColumnStretch(2, 7)
        self.actShortInputLayout.setColumnStretch(3, 1)
        self.actShortInputLayout.setColumnStretch(4, 1)
        self.verticalLayout.addLayout(self.actShortInputLayout)
        self.actReturnLayout = QtWidgets.QGridLayout()
        self.actReturnLayout.setSpacing(1)
        self.actReturnLayout.setObjectName("actReturnLayout")
        self.actSelectInputList = KeyListWidget(actionDialog)
        self.actSelectInputList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.actSelectInputList.setObjectName("actSelectInputList")
        self.actReturnLayout.addWidget(self.actSelectInputList, 1, 2, 1, 1)
        self.actAvailReturnList = QtWidgets.QListWidget(actionDialog)
        self.actAvailReturnList.setObjectName("actAvailReturnList")
        self.actReturnLayout.addWidget(self.actAvailReturnList, 2, 3, 1, 1)
        self.actAvailTriggerList = QtWidgets.QListWidget(actionDialog)
        self.actAvailTriggerList.setObjectName("actAvailTriggerList")
        self.actReturnLayout.addWidget(self.actAvailTriggerList, 2, 1, 1, 1)
        self.actInputLabel = QtWidgets.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actInputLabel.setFont(font)
        self.actInputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actInputLabel.setObjectName("actInputLabel")
        self.actReturnLayout.addWidget(self.actInputLabel, 0, 2, 1, 1)
        self.actReturnLabel = QtWidgets.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actReturnLabel.setFont(font)
        self.actReturnLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actReturnLabel.setObjectName("actReturnLabel")
        self.actReturnLayout.addWidget(self.actReturnLabel, 0, 3, 1, 1)
        self.actSelectReturnList = KeyListWidget(actionDialog)
        self.actSelectReturnList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.actSelectReturnList.setObjectName("actSelectReturnList")
        self.actReturnLayout.addWidget(self.actSelectReturnList, 1, 3, 1, 1)
        self.actAvailInputList = QtWidgets.QListWidget(actionDialog)
        self.actAvailInputList.setViewMode(QtWidgets.QListView.ListMode)
        self.actAvailInputList.setObjectName("actAvailInputList")
        self.actReturnLayout.addWidget(self.actAvailInputList, 2, 2, 1, 1)
        self.actSelectLabel = QtWidgets.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actSelectLabel.setFont(font)
        self.actSelectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actSelectLabel.setObjectName("actSelectLabel")
        self.actReturnLayout.addWidget(self.actSelectLabel, 1, 0, 1, 1)
        self.actSelectTriggerList = KeyListWidget(actionDialog)
        self.actSelectTriggerList.setObjectName("actSelectTriggerList")
        self.actReturnLayout.addWidget(self.actSelectTriggerList, 1, 1, 1, 1)
        self.actAvailLabel = QtWidgets.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actAvailLabel.setFont(font)
        self.actAvailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actAvailLabel.setObjectName("actAvailLabel")
        self.actReturnLayout.addWidget(self.actAvailLabel, 2, 0, 1, 1)
        self.actPassiveTriggerLabel = QtWidgets.QLabel(actionDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.actPassiveTriggerLabel.setFont(font)
        self.actPassiveTriggerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actPassiveTriggerLabel.setObjectName("actPassiveTriggerLabel")
        self.actReturnLayout.addWidget(self.actPassiveTriggerLabel, 0, 1, 1, 1)
        self.actReturnLayout.setRowStretch(1, 1)
        self.actReturnLayout.setRowStretch(2, 2)
        self.verticalLayout.addLayout(self.actReturnLayout)
        self.actLowerLayout = QtWidgets.QHBoxLayout()
        self.actLowerLayout.setObjectName("actLowerLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.actLowerLayout.addItem(spacerItem)
        self.actButtonBox = QtWidgets.QDialogButtonBox(actionDialog)
        self.actButtonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.actButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.actButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.actButtonBox.setCenterButtons(True)
        self.actButtonBox.setObjectName("actButtonBox")
        self.actLowerLayout.addWidget(self.actButtonBox)
        self.actLowerLayout.setStretch(0, 20)
        self.actLowerLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.actLowerLayout)

        self.retranslateUi(actionDialog)
        self.actButtonBox.accepted.connect(actionDialog.accept)
        self.actButtonBox.rejected.connect(actionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(actionDialog)
        actionDialog.setTabOrder(self.actTagLineEdit, self.actNameLineEdit)
        actionDialog.setTabOrder(self.actNameLineEdit, self.actPathLineEdit)
        actionDialog.setTabOrder(self.actPathLineEdit, self.actOptionalsLineEdit)
        actionDialog.setTabOrder(self.actOptionalsLineEdit, self.actActiveRadio)
        actionDialog.setTabOrder(self.actActiveRadio, self.actTriggerLineEdit)
        actionDialog.setTabOrder(self.actTriggerLineEdit, self.actIntervalLineEdit)
        actionDialog.setTabOrder(self.actIntervalLineEdit, self.actPassiveRadio)
        actionDialog.setTabOrder(self.actPassiveRadio, self.passiveBeforeCheck)
        actionDialog.setTabOrder(self.passiveBeforeCheck, self.actSelectTriggerList)
        actionDialog.setTabOrder(self.actSelectTriggerList, self.actAvailTriggerList)
        actionDialog.setTabOrder(self.actAvailTriggerList, self.actSelectInputList)
        actionDialog.setTabOrder(self.actSelectInputList, self.actAvailInputList)
        actionDialog.setTabOrder(self.actAvailInputList, self.actSelectReturnList)
        actionDialog.setTabOrder(self.actSelectReturnList, self.actAvailReturnList)
        actionDialog.setTabOrder(self.actAvailReturnList, self.actButtonBox)

    def retranslateUi(self, actionDialog):
        _translate = QtCore.QCoreApplication.translate
        actionDialog.setWindowTitle(_translate("actionDialog", "Setup Action"))
        self.actOptionalsLabel.setToolTip(_translate("actionDialog", "Optionals to send to function"))
        self.actOptionalsLabel.setText(_translate("actionDialog", "Optionals"))
        self.actTagLabel.setToolTip(_translate("actionDialog", "Human readable name of action"))
        self.actTagLabel.setText(_translate("actionDialog", "Tag "))
        self.actNameLabel.setToolTip(_translate("actionDialog", "Function name of action"))
        self.actNameLabel.setText(_translate("actionDialog", "Name"))
        self.actPassiveRadio.setToolTip(_translate("actionDialog", "Action is triggered by an active action"))
        self.actPassiveRadio.setText(_translate("actionDialog", "Passive"))
        self.actIntervalLabel.setToolTip(_translate("actionDialog", "Time in seconds between calling action"))
        self.actIntervalLabel.setText(_translate("actionDialog", "Interval (s)"))
        self.actActiveRadio.setToolTip(_translate("actionDialog", "Action is called using a keybind or click"))
        self.actActiveRadio.setText(_translate("actionDialog", "Active"))
        self.passiveBeforeCheck.setToolTip(_translate("actionDialog", "Action is to applied prior its triggering active action"))
        self.passiveBeforeCheck.setText(_translate("actionDialog", "Before Trigger"))
        self.actPathLabel.setToolTip(_translate("actionDialog", "Path relative a directory on the computers PATH variable"))
        self.actPathLabel.setText(_translate("actionDialog", "Path"))
        self.actTriggerLabel.setToolTip(_translate("actionDialog", "Keybind to activate action"))
        self.actTriggerLabel.setText(_translate("actionDialog", "Trigger"))
        self.activeTimerCheck.setToolTip(_translate("actionDialog", "Repeat action every interval"))
        self.activeTimerCheck.setText(_translate("actionDialog", "Timer"))
        self.activeThreadedCheck.setToolTip(_translate("actionDialog", "Run action in background"))
        self.activeThreadedCheck.setText(_translate("actionDialog", "Thread"))
        self.actAvailReturnList.setSortingEnabled(True)
        self.actAvailTriggerList.setSortingEnabled(True)
        self.actInputLabel.setToolTip(_translate("actionDialog", "Variable(s) to send to function"))
        self.actInputLabel.setText(_translate("actionDialog", "Inputs"))
        self.actReturnLabel.setToolTip(_translate("actionDialog", "Variable(s) to be returned by function "))
        self.actReturnLabel.setText(_translate("actionDialog", "Returns"))
        self.actAvailInputList.setSortingEnabled(True)
        self.actSelectLabel.setText(_translate("actionDialog", "Selected"))
        self.actSelectTriggerList.setSortingEnabled(True)
        self.actAvailLabel.setText(_translate("actionDialog", "Available"))
        self.actPassiveTriggerLabel.setToolTip(_translate("actionDialog", "Active actions which trigger a passive action"))
        self.actPassiveTriggerLabel.setText(_translate("actionDialog", "Passive Triggers"))

from lazylyst.CustomWidgets import HoverLineEdit, KeyBindLineEdit, KeyListWidget