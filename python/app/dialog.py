# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
import os
import sys
import threading
import datetime

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog

def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system. 
    
    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
    app_instance.engine.show_dialog("SG TimeSlogger", app_instance, AppDialog)

class AppDialog(QtGui.QWidget):
    """
    Main application dialog window
    """
    """
    Set Font
    """
    def showEvent(self, event):
        font = QtGui.QFont()
        font.setPointSize(65)
        self.ui.label_time.setFont(font)

    def __init__(self):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)
        
        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        self.ui.pushButton_start.clicked.connect(self.start_timer)
        self.ui.pushButton_stop.clicked.connect(self.stop_and_log)
        self.ui.pushButton_pause.clicked.connect(self.pause_timer)

        # timer stuff
        self._update_timer = QtCore.QTimer(self)
        self._update_timer.timeout.connect(self.update_ticker)

        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:

        self._app = sgtk.platform.current_bundle()
        self.sg = self._app.shotgun
        self.context = self._app.context
        print self.sg

        # via the self._app handle we can for example access:
        # - The engine, via self._app.engine
        # - A Shotgun API instance, via self._app.shotgun
        # - A tk API instance, via self._app.tk 
        
        # lastly, set up our very basic UI
        self.ui.context.setText("Current Context: %s" % self._app.context)

    # Start the Timer and Prints the Context in the Shell
    """
    Function for Time Start
    """
    def start_timer(self):
        print "start timer"
        self.start_time = datetime.datetime.now()
        self._update_timer.start(1000)
        print "Context is "
        print repr(self.context)

    # Stops the Timer, Creates Time in Minutes, Updates Shotgun with Timelog against Context
    """
    Stop Timer and Log Time in Shotgun
    """
    def stop_and_log(self):
        print "Stop Timer, Create Time Log"
        self.stop_time = datetime.datetime.now()
        time_delta = self.stop_time - self.start_time
        self._update_timer.stop()
        time_string_min = (time_delta.seconds // 60) % 60
        print "Time Logged in Minutes: ",time_string_min
        print "Time Logged for",self._app.context

        data = {
            "project": self.context.project,
            "entity": self.context.task,
            "description": "TimeSlogger Timelog",
            "duration": time_string_min
        }
        self.sg.create('TimeLog', data)

    # Pause the Running of the Timer /  Add One minute in Dev build
    """
    Function for Time Pause
    """
    def pause_timer(self):
        print "Time set to 1 Minute"

    # Updates the Ticker and Formats it
    """
    Ticker Update
    """
    def update_ticker(self):
        self.stop_time = datetime.datetime.now()
        time_delta = self.stop_time - self.start_time
        time_string = "{0}:{1}:{2}".format(time_delta.seconds//3600,(time_delta.seconds//60)%60,time_delta.seconds)
        self.ui.label_time.setText(time_string)
        print time_string
