# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 785)
        MainWindow.setDockNestingEnabled(True)
        self.mainLayout = QtWidgets.QWidget(MainWindow)
        self.mainLayout.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainLayout.sizePolicy().hasHeightForWidth())
        self.mainLayout.setSizePolicy(sizePolicy)
        self.mainLayout.setMinimumSize(QtCore.QSize(0, 0))
        self.mainLayout.setObjectName("mainLayout")
        MainWindow.setCentralWidget(self.mainLayout)
        self.textOutDock = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textOutDock.sizePolicy().hasHeightForWidth())
        self.textOutDock.setSizePolicy(sizePolicy)
        self.textOutDock.setMinimumSize(QtCore.QSize(181, 155))
        self.textOutDock.setMaximumSize(QtCore.QSize(524287, 524287))
        self.textOutDock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.textOutDock.setObjectName("textOutDock")
        self.textOutLayout = QtWidgets.QWidget()
        self.textOutLayout.setObjectName("textOutLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.textOutLayout)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textOutBrowser = QtWidgets.QTextBrowser(self.textOutLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textOutBrowser.sizePolicy().hasHeightForWidth())
        self.textOutBrowser.setSizePolicy(sizePolicy)
        self.textOutBrowser.setObjectName("textOutBrowser")
        self.verticalLayout_2.addWidget(self.textOutBrowser)
        self.textOutGridLayout = QtWidgets.QGridLayout()
        self.textOutGridLayout.setObjectName("textOutGridLayout")
        self.strollingLabel = QtWidgets.QLabel(self.textOutLayout)
        self.strollingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.strollingLabel.setObjectName("strollingLabel")
        self.textOutGridLayout.addWidget(self.strollingLabel, 0, 0, 1, 1)
        self.strollComboBox = QtWidgets.QComboBox(self.textOutLayout)
        self.strollComboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.strollComboBox.setObjectName("strollComboBox")
        self.textOutGridLayout.addWidget(self.strollComboBox, 1, 0, 1, 1)
        self.schemingLabel = QtWidgets.QLabel(self.textOutLayout)
        self.schemingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.schemingLabel.setObjectName("schemingLabel")
        self.textOutGridLayout.addWidget(self.schemingLabel, 0, 1, 1, 1)
        self.schemeComboBox = QtWidgets.QComboBox(self.textOutLayout)
        self.schemeComboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.schemeComboBox.setObjectName("schemeComboBox")
        self.textOutGridLayout.addWidget(self.schemeComboBox, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.textOutGridLayout)
        self.textOutDock.setWidget(self.textOutLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.textOutDock)
        self.archiveListDock = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveListDock.sizePolicy().hasHeightForWidth())
        self.archiveListDock.setSizePolicy(sizePolicy)
        self.archiveListDock.setMinimumSize(QtCore.QSize(96, 131))
        self.archiveListDock.setMaximumSize(QtCore.QSize(524287, 524287))
        self.archiveListDock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.archiveListDock.setObjectName("archiveListDock")
        self.archiveListLayout = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveListLayout.sizePolicy().hasHeightForWidth())
        self.archiveListLayout.setSizePolicy(sizePolicy)
        self.archiveListLayout.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.archiveListLayout.setObjectName("archiveListLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.archiveListLayout)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.archiveList = ArchiveListWidget(self.archiveListLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveList.sizePolicy().hasHeightForWidth())
        self.archiveList.setSizePolicy(sizePolicy)
        self.archiveList.setMinimumSize(QtCore.QSize(0, 0))
        self.archiveList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.archiveList.setObjectName("archiveList")
        self.verticalLayout.addWidget(self.archiveList)
        self.archiveListLineEdit = QtWidgets.QLineEdit(self.archiveListLayout)
        self.archiveListLineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.archiveListLineEdit.setObjectName("archiveListLineEdit")
        self.verticalLayout.addWidget(self.archiveListLineEdit)
        self.archiveListDock.setWidget(self.archiveListLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.archiveListDock)
        self.mapDock = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapDock.sizePolicy().hasHeightForWidth())
        self.mapDock.setSizePolicy(sizePolicy)
        self.mapDock.setMinimumSize(QtCore.QSize(78, 103))
        self.mapDock.setMaximumSize(QtCore.QSize(524287, 524287))
        self.mapDock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.mapDock.setObjectName("mapDock")
        self.mayLayout = QtWidgets.QWidget()
        self.mayLayout.setObjectName("mayLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.mayLayout)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.mapWidget = MapWidget(self.mayLayout)
        self.mapWidget.setObjectName("mapWidget")
        self.verticalLayout_6.addWidget(self.mapWidget)
        self.mapDock.setWidget(self.mayLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.mapDock)
        self.archiveViewDock = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveViewDock.sizePolicy().hasHeightForWidth())
        self.archiveViewDock.setSizePolicy(sizePolicy)
        self.archiveViewDock.setMinimumSize(QtCore.QSize(78, 126))
        self.archiveViewDock.setMaximumSize(QtCore.QSize(524287, 524287))
        self.archiveViewDock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.archiveViewDock.setObjectName("archiveViewDock")
        self.archiveViewLayout = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveViewLayout.sizePolicy().hasHeightForWidth())
        self.archiveViewLayout.setSizePolicy(sizePolicy)
        self.archiveViewLayout.setObjectName("archiveViewLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.archiveViewLayout)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.archiveViewTextLayout = QtWidgets.QHBoxLayout()
        self.archiveViewTextLayout.setSpacing(0)
        self.archiveViewTextLayout.setObjectName("archiveViewTextLayout")
        self.archiveSpanT0Label = DblClickLabelWidget(self.archiveViewLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveSpanT0Label.sizePolicy().hasHeightForWidth())
        self.archiveSpanT0Label.setSizePolicy(sizePolicy)
        self.archiveSpanT0Label.setMinimumSize(QtCore.QSize(0, 10))
        self.archiveSpanT0Label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.archiveSpanT0Label.setFont(font)
        self.archiveSpanT0Label.setText("")
        self.archiveSpanT0Label.setObjectName("archiveSpanT0Label")
        self.archiveViewTextLayout.addWidget(self.archiveSpanT0Label)
        self.archiveSpanT1Label = DblClickLabelWidget(self.archiveViewLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveSpanT1Label.sizePolicy().hasHeightForWidth())
        self.archiveSpanT1Label.setSizePolicy(sizePolicy)
        self.archiveSpanT1Label.setMinimumSize(QtCore.QSize(0, 10))
        self.archiveSpanT1Label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.archiveSpanT1Label.setFont(font)
        self.archiveSpanT1Label.setText("")
        self.archiveSpanT1Label.setObjectName("archiveSpanT1Label")
        self.archiveViewTextLayout.addWidget(self.archiveSpanT1Label)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.archiveViewTextLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.archiveViewTextLayout)
        self.archiveSpan = ArchiveSpanWidget(self.archiveViewLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveSpan.sizePolicy().hasHeightForWidth())
        self.archiveSpan.setSizePolicy(sizePolicy)
        self.archiveSpan.setMinimumSize(QtCore.QSize(0, 20))
        self.archiveSpan.setMaximumSize(QtCore.QSize(16777215, 65))
        self.archiveSpan.setObjectName("archiveSpan")
        self.verticalLayout_3.addWidget(self.archiveSpan)
        self.archiveEvent = ArchiveEventWidget(self.archiveViewLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveEvent.sizePolicy().hasHeightForWidth())
        self.archiveEvent.setSizePolicy(sizePolicy)
        self.archiveEvent.setMinimumSize(QtCore.QSize(0, 20))
        self.archiveEvent.setMaximumSize(QtCore.QSize(16777215, 40))
        self.archiveEvent.setObjectName("archiveEvent")
        self.verticalLayout_3.addWidget(self.archiveEvent)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.archiveViewDock.setWidget(self.archiveViewLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.archiveViewDock)
        self.traceViewDock = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.traceViewDock.sizePolicy().hasHeightForWidth())
        self.traceViewDock.setSizePolicy(sizePolicy)
        self.traceViewDock.setMinimumSize(QtCore.QSize(80, 82))
        self.traceViewDock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.traceViewDock.setObjectName("traceViewDock")
        self.traceViewLayout = QtWidgets.QWidget()
        self.traceViewLayout.setObjectName("traceViewLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.traceViewLayout)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.traceSplitter = QtWidgets.QSplitter(self.traceViewLayout)
        self.traceSplitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.traceSplitter.setLineWidth(0)
        self.traceSplitter.setOrientation(QtCore.Qt.Vertical)
        self.traceSplitter.setHandleWidth(1)
        self.traceSplitter.setChildrenCollapsible(False)
        self.traceSplitter.setObjectName("traceSplitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.traceSplitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.timeImageLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.timeImageLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.timeImageLayout.setContentsMargins(0, 0, 0, 0)
        self.timeImageLayout.setSpacing(1)
        self.timeImageLayout.setObjectName("timeImageLayout")
        self.timeWidget = TimeWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeWidget.sizePolicy().hasHeightForWidth())
        self.timeWidget.setSizePolicy(sizePolicy)
        self.timeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.timeWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.timeWidget.setBaseSize(QtCore.QSize(0, 0))
        self.timeWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.timeWidget.setObjectName("timeWidget")
        self.timeImageLayout.addWidget(self.timeWidget)
        self.imageWidget = ImageWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageWidget.sizePolicy().hasHeightForWidth())
        self.imageWidget.setSizePolicy(sizePolicy)
        self.imageWidget.setMinimumSize(QtCore.QSize(0, 1))
        self.imageWidget.setObjectName("imageWidget")
        self.timeImageLayout.addWidget(self.imageWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.traceSplitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.traceLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.traceLayout.setContentsMargins(0, 0, 0, 0)
        self.traceLayout.setSpacing(1)
        self.traceLayout.setObjectName("traceLayout")
        self.verticalLayout_4.addWidget(self.traceSplitter)
        self.traceViewDock.setWidget(self.traceViewLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.traceViewDock)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lazylyst"))
        self.textOutDock.setWindowTitle(_translate("MainWindow", "Standard Out"))
        self.strollingLabel.setText(_translate("MainWindow", "Strolling (0)"))
        self.schemingLabel.setText(_translate("MainWindow", "Scheming (0)"))
        self.archiveListDock.setWindowTitle(_translate("MainWindow", "Archive List"))
        self.archiveListLineEdit.setPlaceholderText(_translate("MainWindow", "Search"))
        self.mapDock.setWindowTitle(_translate("MainWindow", "Map View"))
        self.archiveViewDock.setWindowTitle(_translate("MainWindow", "Archive View"))
        self.traceViewDock.setWindowTitle(_translate("MainWindow", "Trace View"))

from CustomWidgets import DblClickLabelWidget
from MapWidgets import MapWidget
from TemporalWidgets import ArchiveEventWidget, ArchiveListWidget, ArchiveSpanWidget, ImageWidget, TimeWidget
