# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(814, 406)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.context = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context.sizePolicy().hasHeightForWidth())
        self.context.setSizePolicy(sizePolicy)
        self.context.setMaximumSize(QtCore.QSize(140, 50))
        self.context.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.context.setObjectName("context")
        self.gridLayout.addWidget(self.context, 2, 1, 1, 1)
        self.pushButton_pause = QtGui.QPushButton(Dialog)
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.gridLayout.addWidget(self.pushButton_pause, 4, 1, 1, 1)
        self.logo_example = QtGui.QLabel(Dialog)
        self.logo_example.setMaximumSize(QtCore.QSize(100, 100))
        self.logo_example.setText("")
        self.logo_example.setPixmap(QtGui.QPixmap(":/res/sg_logo.png"))
        self.logo_example.setObjectName("logo_example")
        self.gridLayout.addWidget(self.logo_example, 2, 0, 1, 1)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 2, 3, 1, 2)
        self.pushButton_stop = QtGui.QPushButton(Dialog)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout.addWidget(self.pushButton_stop, 4, 4, 1, 1)
        self.pushButton_start = QtGui.QPushButton(Dialog)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 4, 0, 1, 1)
        self.label_time = QtGui.QLabel(Dialog)
        self.label_time.setMinimumSize(QtCore.QSize(400, 100))
        self.label_time.setMaximumSize(QtCore.QSize(700, 100))
        self.label_time.setObjectName("label_time")
        self.gridLayout.addWidget(self.label_time, 0, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.context.setText(QtGui.QApplication.translate("Dialog", "Your Current Context: ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_pause.setText(QtGui.QApplication.translate("Dialog", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_stop.setText(QtGui.QApplication.translate("Dialog", "Stop / Create Log", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_start.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_time.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
from . import resources_rc
