# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(871, 785)
        MainWindow.setDockNestingEnabled(True)
        self.mainLayout = QtGui.QWidget(MainWindow)
        self.mainLayout.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainLayout.sizePolicy().hasHeightForWidth())
        self.mainLayout.setSizePolicy(sizePolicy)
        self.mainLayout.setMinimumSize(QtCore.QSize(0, 0))
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        MainWindow.setCentralWidget(self.mainLayout)
        self.textOutDock = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textOutDock.sizePolicy().hasHeightForWidth())
        self.textOutDock.setSizePolicy(sizePolicy)
        self.textOutDock.setMinimumSize(QtCore.QSize(181, 155))
        self.textOutDock.setMaximumSize(QtCore.QSize(524287, 524287))
        self.textOutDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.textOutDock.setObjectName(_fromUtf8("textOutDock"))
        self.textOutLayout = QtGui.QWidget()
        self.textOutLayout.setObjectName(_fromUtf8("textOutLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.textOutLayout)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textOutBrowser = QtGui.QTextBrowser(self.textOutLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textOutBrowser.sizePolicy().hasHeightForWidth())
        self.textOutBrowser.setSizePolicy(sizePolicy)
        self.textOutBrowser.setObjectName(_fromUtf8("textOutBrowser"))
        self.verticalLayout_2.addWidget(self.textOutBrowser)
        self.textOutGridLayout = QtGui.QGridLayout()
        self.textOutGridLayout.setObjectName(_fromUtf8("textOutGridLayout"))
        self.strollingLabel = QtGui.QLabel(self.textOutLayout)
        self.strollingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.strollingLabel.setObjectName(_fromUtf8("strollingLabel"))
        self.textOutGridLayout.addWidget(self.strollingLabel, 0, 0, 1, 1)
        self.strollComboBox = QtGui.QComboBox(self.textOutLayout)
        self.strollComboBox.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.strollComboBox.setObjectName(_fromUtf8("strollComboBox"))
        self.textOutGridLayout.addWidget(self.strollComboBox, 1, 0, 1, 1)
        self.schemingLabel = QtGui.QLabel(self.textOutLayout)
        self.schemingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.schemingLabel.setObjectName(_fromUtf8("schemingLabel"))
        self.textOutGridLayout.addWidget(self.schemingLabel, 0, 1, 1, 1)
        self.schemeComboBox = QtGui.QComboBox(self.textOutLayout)
        self.schemeComboBox.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.schemeComboBox.setObjectName(_fromUtf8("schemeComboBox"))
        self.textOutGridLayout.addWidget(self.schemeComboBox, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.textOutGridLayout)
        self.textOutDock.setWidget(self.textOutLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.textOutDock)
        self.archiveListDock = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveListDock.sizePolicy().hasHeightForWidth())
        self.archiveListDock.setSizePolicy(sizePolicy)
        self.archiveListDock.setMinimumSize(QtCore.QSize(96, 131))
        self.archiveListDock.setMaximumSize(QtCore.QSize(524287, 524287))
        self.archiveListDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.archiveListDock.setObjectName(_fromUtf8("archiveListDock"))
        self.archiveListLayout = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveListLayout.sizePolicy().hasHeightForWidth())
        self.archiveListLayout.setSizePolicy(sizePolicy)
        self.archiveListLayout.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.archiveListLayout.setObjectName(_fromUtf8("archiveListLayout"))
        self.verticalLayout = QtGui.QVBoxLayout(self.archiveListLayout)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.archiveList = ArchiveListWidget(self.archiveListLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveList.sizePolicy().hasHeightForWidth())
        self.archiveList.setSizePolicy(sizePolicy)
        self.archiveList.setMinimumSize(QtCore.QSize(0, 0))
        self.archiveList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.archiveList.setObjectName(_fromUtf8("archiveList"))
        self.verticalLayout.addWidget(self.archiveList)
        self.archiveListLineEdit = QtGui.QLineEdit(self.archiveListLayout)
        self.archiveListLineEdit.setObjectName(_fromUtf8("archiveListLineEdit"))
        self.verticalLayout.addWidget(self.archiveListLineEdit)
        self.archiveListDock.setWidget(self.archiveListLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.archiveListDock)
        self.mapDock = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapDock.sizePolicy().hasHeightForWidth())
        self.mapDock.setSizePolicy(sizePolicy)
        self.mapDock.setMinimumSize(QtCore.QSize(78, 103))
        self.mapDock.setMaximumSize(QtCore.QSize(524287, 524287))
        self.mapDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.mapDock.setObjectName(_fromUtf8("mapDock"))
        self.mayLayout = QtGui.QWidget()
        self.mayLayout.setObjectName(_fromUtf8("mayLayout"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.mayLayout)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.mapWidget = MapWidget(self.mayLayout)
        self.mapWidget.setObjectName(_fromUtf8("mapWidget"))
        self.verticalLayout_6.addWidget(self.mapWidget)
        self.mapDock.setWidget(self.mayLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.mapDock)
        self.archiveViewDock = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveViewDock.sizePolicy().hasHeightForWidth())
        self.archiveViewDock.setSizePolicy(sizePolicy)
        self.archiveViewDock.setMinimumSize(QtCore.QSize(78, 126))
        self.archiveViewDock.setMaximumSize(QtCore.QSize(524287, 524287))
        self.archiveViewDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.archiveViewDock.setObjectName(_fromUtf8("archiveViewDock"))
        self.archiveViewLayout = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveViewLayout.sizePolicy().hasHeightForWidth())
        self.archiveViewLayout.setSizePolicy(sizePolicy)
        self.archiveViewLayout.setObjectName(_fromUtf8("archiveViewLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.archiveViewLayout)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.archiveViewTextLayout = QtGui.QHBoxLayout()
        self.archiveViewTextLayout.setSpacing(0)
        self.archiveViewTextLayout.setObjectName(_fromUtf8("archiveViewTextLayout"))
        self.archiveSpanT0Label = DblClickLabelWidget(self.archiveViewLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveSpanT0Label.sizePolicy().hasHeightForWidth())
        self.archiveSpanT0Label.setSizePolicy(sizePolicy)
        self.archiveSpanT0Label.setMinimumSize(QtCore.QSize(0, 10))
        self.archiveSpanT0Label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.archiveSpanT0Label.setFont(font)
        self.archiveSpanT0Label.setText(_fromUtf8(""))
        self.archiveSpanT0Label.setObjectName(_fromUtf8("archiveSpanT0Label"))
        self.archiveViewTextLayout.addWidget(self.archiveSpanT0Label)
        self.archiveSpanT1Label = DblClickLabelWidget(self.archiveViewLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveSpanT1Label.sizePolicy().hasHeightForWidth())
        self.archiveSpanT1Label.setSizePolicy(sizePolicy)
        self.archiveSpanT1Label.setMinimumSize(QtCore.QSize(0, 10))
        self.archiveSpanT1Label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.archiveSpanT1Label.setFont(font)
        self.archiveSpanT1Label.setText(_fromUtf8(""))
        self.archiveSpanT1Label.setObjectName(_fromUtf8("archiveSpanT1Label"))
        self.archiveViewTextLayout.addWidget(self.archiveSpanT1Label)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.archiveViewTextLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.archiveViewTextLayout)
        self.archiveSpan = ArchiveSpanWidget(self.archiveViewLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveSpan.sizePolicy().hasHeightForWidth())
        self.archiveSpan.setSizePolicy(sizePolicy)
        self.archiveSpan.setMinimumSize(QtCore.QSize(0, 20))
        self.archiveSpan.setMaximumSize(QtCore.QSize(16777215, 65))
        self.archiveSpan.setObjectName(_fromUtf8("archiveSpan"))
        self.verticalLayout_3.addWidget(self.archiveSpan)
        self.archiveEvent = ArchiveEventWidget(self.archiveViewLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archiveEvent.sizePolicy().hasHeightForWidth())
        self.archiveEvent.setSizePolicy(sizePolicy)
        self.archiveEvent.setMinimumSize(QtCore.QSize(0, 20))
        self.archiveEvent.setMaximumSize(QtCore.QSize(16777215, 40))
        self.archiveEvent.setObjectName(_fromUtf8("archiveEvent"))
        self.verticalLayout_3.addWidget(self.archiveEvent)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.archiveViewDock.setWidget(self.archiveViewLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.archiveViewDock)
        self.traceViewDock = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.traceViewDock.sizePolicy().hasHeightForWidth())
        self.traceViewDock.setSizePolicy(sizePolicy)
        self.traceViewDock.setMinimumSize(QtCore.QSize(80, 82))
        self.traceViewDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.traceViewDock.setObjectName(_fromUtf8("traceViewDock"))
        self.traceViewLayout = QtGui.QWidget()
        self.traceViewLayout.setObjectName(_fromUtf8("traceViewLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.traceViewLayout)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.traceSplitter = QtGui.QSplitter(self.traceViewLayout)
        self.traceSplitter.setFrameShape(QtGui.QFrame.NoFrame)
        self.traceSplitter.setLineWidth(0)
        self.traceSplitter.setOrientation(QtCore.Qt.Vertical)
        self.traceSplitter.setHandleWidth(1)
        self.traceSplitter.setChildrenCollapsible(False)
        self.traceSplitter.setObjectName(_fromUtf8("traceSplitter"))
        self.verticalLayoutWidget = QtGui.QWidget(self.traceSplitter)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.timeImageLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.timeImageLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.timeImageLayout.setSpacing(1)
        self.timeImageLayout.setObjectName(_fromUtf8("timeImageLayout"))
        self.timeWidget = TimeWidget(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeWidget.sizePolicy().hasHeightForWidth())
        self.timeWidget.setSizePolicy(sizePolicy)
        self.timeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.timeWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.timeWidget.setBaseSize(QtCore.QSize(0, 0))
        self.timeWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.timeWidget.setObjectName(_fromUtf8("timeWidget"))
        self.timeImageLayout.addWidget(self.timeWidget)
        self.imageWidget = ImageWidget(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageWidget.sizePolicy().hasHeightForWidth())
        self.imageWidget.setSizePolicy(sizePolicy)
        self.imageWidget.setMinimumSize(QtCore.QSize(0, 1))
        self.imageWidget.setObjectName(_fromUtf8("imageWidget"))
        self.timeImageLayout.addWidget(self.imageWidget)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.traceSplitter)
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.traceLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.traceLayout.setSpacing(1)
        self.traceLayout.setObjectName(_fromUtf8("traceLayout"))
        self.verticalLayout_4.addWidget(self.traceSplitter)
        self.traceViewDock.setWidget(self.traceViewLayout)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.traceViewDock)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Lazylyst", None))
        self.textOutDock.setWindowTitle(_translate("MainWindow", "Standard Out", None))
        self.strollingLabel.setText(_translate("MainWindow", "Strolling (0)", None))
        self.schemingLabel.setText(_translate("MainWindow", "Scheming (0)", None))
        self.archiveListDock.setWindowTitle(_translate("MainWindow", "Archive List", None))
        self.mapDock.setWindowTitle(_translate("MainWindow", "Map View", None))
        self.archiveViewDock.setWindowTitle(_translate("MainWindow", "Archive View", None))
        self.traceViewDock.setWindowTitle(_translate("MainWindow", "Trace View", None))

from CustomWidgets import ArchiveEventWidget, ArchiveListWidget, ArchiveSpanWidget, DblClickLabelWidget, ImageWidget, MapWidget, TimeWidget
