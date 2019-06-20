# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cam_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cam_gui(object):
    def setupUi(self, cam_gui):
        cam_gui.setObjectName("cam_gui")
        cam_gui.resize(863, 762)
        self.centralWidget = QtWidgets.QWidget(cam_gui)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Save = QtWidgets.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Save.setFont(font)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.gridLayout.addWidget(self.pushButton_Save, 11, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 11, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 7, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_19.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_19.setSpacing(6)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.lineEdit_Browse = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Browse.setObjectName("lineEdit_Browse")
        self.gridLayout_19.addWidget(self.lineEdit_Browse, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 11, 4, 1, 2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_14.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_14.setSpacing(6)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_Read_mode = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Read_mode.setFont(font)
        self.label_Read_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Read_mode.setObjectName("label_Read_mode")
        self.gridLayout_10.addWidget(self.label_Read_mode, 0, 0, 1, 1)
        self.comboBox_Read_mode = QtWidgets.QComboBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_Read_mode.setFont(font)
        self.comboBox_Read_mode.setEditable(False)
        self.comboBox_Read_mode.setObjectName("comboBox_Read_mode")
        self.gridLayout_10.addWidget(self.comboBox_Read_mode, 0, 1, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_5, 4, 4, 1, 3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_16.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_16.setSpacing(6)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_EMCCDGain_disp = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_EMCCDGain_disp.setFont(font)
        self.label_EMCCDGain_disp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_EMCCDGain_disp.setObjectName("label_EMCCDGain_disp")
        self.gridLayout_8.addWidget(self.label_EMCCDGain_disp, 0, 0, 1, 1)
        self.doubleSpinBox_EMCCD_Gain = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_EMCCD_Gain.setFont(font)
        self.doubleSpinBox_EMCCD_Gain.setDecimals(0)
        self.doubleSpinBox_EMCCD_Gain.setMaximum(300.0)
        self.doubleSpinBox_EMCCD_Gain.setObjectName("doubleSpinBox_EMCCD_Gain")
        self.gridLayout_8.addWidget(self.doubleSpinBox_EMCCD_Gain, 0, 1, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 5, 4, 1, 3)
        self.pushButton_Cam_Off = QtWidgets.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Cam_Off.setFont(font)
        self.pushButton_Cam_Off.setObjectName("pushButton_Cam_Off")
        self.gridLayout.addWidget(self.pushButton_Cam_Off, 2, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_17.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_17.setSpacing(6)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.doubleSpinBox_End_row = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_End_row.setFont(font)
        self.doubleSpinBox_End_row.setDecimals(0)
        self.doubleSpinBox_End_row.setMaximum(512.0)
        self.doubleSpinBox_End_row.setObjectName("doubleSpinBox_End_row")
        self.gridLayout_3.addWidget(self.doubleSpinBox_End_row, 1, 6, 1, 1)
        self.doubleSpinBox_Start_col = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_Start_col.setFont(font)
        self.doubleSpinBox_Start_col.setDecimals(0)
        self.doubleSpinBox_Start_col.setMaximum(512.0)
        self.doubleSpinBox_Start_col.setProperty("value", 1.0)
        self.doubleSpinBox_Start_col.setObjectName("doubleSpinBox_Start_col")
        self.gridLayout_3.addWidget(self.doubleSpinBox_Start_col, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 4, 1, 1)
        self.label_End_col = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_End_col.setFont(font)
        self.label_End_col.setAlignment(QtCore.Qt.AlignCenter)
        self.label_End_col.setObjectName("label_End_col")
        self.gridLayout_3.addWidget(self.label_End_col, 1, 1, 1, 1)
        self.label_Start_row = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Start_row.setFont(font)
        self.label_Start_row.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Start_row.setObjectName("label_Start_row")
        self.gridLayout_3.addWidget(self.label_Start_row, 0, 5, 1, 1)
        self.label_End_row = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_End_row.setFont(font)
        self.label_End_row.setAlignment(QtCore.Qt.AlignCenter)
        self.label_End_row.setObjectName("label_End_row")
        self.gridLayout_3.addWidget(self.label_End_row, 1, 5, 1, 1)
        self.doubleSpinBox_End_col = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_End_col.setFont(font)
        self.doubleSpinBox_End_col.setDecimals(0)
        self.doubleSpinBox_End_col.setMaximum(512.0)
        self.doubleSpinBox_End_col.setObjectName("doubleSpinBox_End_col")
        self.gridLayout_3.addWidget(self.doubleSpinBox_End_col, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_Start_col = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Start_col.setFont(font)
        self.label_Start_col.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Start_col.setObjectName("label_Start_col")
        self.gridLayout_3.addWidget(self.label_Start_col, 0, 1, 1, 1)
        self.doubleSpinBox_Start_row = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_Start_row.setFont(font)
        self.doubleSpinBox_Start_row.setDecimals(0)
        self.doubleSpinBox_Start_row.setMaximum(512.0)
        self.doubleSpinBox_Start_row.setProperty("value", 1.0)
        self.doubleSpinBox_Start_row.setObjectName("doubleSpinBox_Start_row")
        self.gridLayout_3.addWidget(self.doubleSpinBox_Start_row, 0, 6, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox_7)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 0, 3, 2, 1)
        self.gridLayout_17.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_7, 8, 1, 2, 6)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_18.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_18.setSpacing(6)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.doubleSpinBox_Accum_time = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_Accum_time.setFont(font)
        self.doubleSpinBox_Accum_time.setDecimals(3)
        self.doubleSpinBox_Accum_time.setSingleStep(0.001)
        self.doubleSpinBox_Accum_time.setObjectName("doubleSpinBox_Accum_time")
        self.gridLayout_2.addWidget(self.doubleSpinBox_Accum_time, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 5, 1, 1)
        self.doubleSpinBox_no_Kin = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_no_Kin.setFont(font)
        self.doubleSpinBox_no_Kin.setDecimals(0)
        self.doubleSpinBox_no_Kin.setMaximum(1000.0)
        self.doubleSpinBox_no_Kin.setProperty("value", 1.0)
        self.doubleSpinBox_no_Kin.setObjectName("doubleSpinBox_no_Kin")
        self.gridLayout_2.addWidget(self.doubleSpinBox_no_Kin, 0, 7, 1, 1)
        self.label_no_Kin = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_no_Kin.setFont(font)
        self.label_no_Kin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_no_Kin.setObjectName("label_no_Kin")
        self.gridLayout_2.addWidget(self.label_no_Kin, 0, 6, 1, 1)
        self.label_Kin_time = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Kin_time.setFont(font)
        self.label_Kin_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Kin_time.setObjectName("label_Kin_time")
        self.gridLayout_2.addWidget(self.label_Kin_time, 1, 6, 1, 1)
        self.doubleSpinBox_no_Accum = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_no_Accum.setFont(font)
        self.doubleSpinBox_no_Accum.setPrefix("")
        self.doubleSpinBox_no_Accum.setSuffix("")
        self.doubleSpinBox_no_Accum.setDecimals(0)
        self.doubleSpinBox_no_Accum.setProperty("value", 1.0)
        self.doubleSpinBox_no_Accum.setObjectName("doubleSpinBox_no_Accum")
        self.gridLayout_2.addWidget(self.doubleSpinBox_no_Accum, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_Accum_time = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Accum_time.setFont(font)
        self.label_Accum_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Accum_time.setObjectName("label_Accum_time")
        self.gridLayout_2.addWidget(self.label_Accum_time, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_no_Accum = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_no_Accum.setFont(font)
        self.label_no_Accum.setAlignment(QtCore.Qt.AlignCenter)
        self.label_no_Accum.setObjectName("label_no_Accum")
        self.gridLayout_2.addWidget(self.label_no_Accum, 0, 2, 1, 1)
        self.doubleSpinBox_Kin_time = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_Kin_time.setFont(font)
        self.doubleSpinBox_Kin_time.setDecimals(3)
        self.doubleSpinBox_Kin_time.setSingleStep(0.001)
        self.doubleSpinBox_Kin_time.setObjectName("doubleSpinBox_Kin_time")
        self.gridLayout_2.addWidget(self.doubleSpinBox_Kin_time, 1, 7, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_6)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 4, 2, 1)
        self.gridLayout_18.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_6, 6, 1, 2, 6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 11, 1, 1, 1)
        self.pushButton_Cam_On = QtWidgets.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Cam_On.setFont(font)
        self.pushButton_Cam_On.setObjectName("pushButton_Cam_On")
        self.gridLayout.addWidget(self.pushButton_Cam_On, 2, 5, 1, 1)
        self.pushButton_Browse = QtWidgets.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Browse.setFont(font)
        self.pushButton_Browse.setObjectName("pushButton_Browse")
        self.gridLayout.addWidget(self.pushButton_Browse, 11, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 8, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 6, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_12.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_Cooler_OnOff = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Cooler_OnOff.setFont(font)
        self.label_Cooler_OnOff.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Cooler_OnOff.setObjectName("label_Cooler_OnOff")
        self.gridLayout_5.addWidget(self.label_Cooler_OnOff, 0, 1, 1, 1)
        self.label_Temp_disp = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Temp_disp.setFont(font)
        self.label_Temp_disp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Temp_disp.setObjectName("label_Temp_disp")
        self.gridLayout_5.addWidget(self.label_Temp_disp, 0, 0, 1, 1)
        self.doubleSpinBox_Temp_set = QtWidgets.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_Temp_set.setFont(font)
        self.doubleSpinBox_Temp_set.setDecimals(0)
        self.doubleSpinBox_Temp_set.setMinimum(-70.0)
        self.doubleSpinBox_Temp_set.setMaximum(30.0)
        self.doubleSpinBox_Temp_set.setProperty("value", -30.0)
        self.doubleSpinBox_Temp_set.setObjectName("doubleSpinBox_Temp_set")
        self.gridLayout_5.addWidget(self.doubleSpinBox_Temp_set, 0, 2, 1, 1)
        self.pushButton_Temp_set = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Temp_set.setFont(font)
        self.pushButton_Temp_set.setObjectName("pushButton_Temp_set")
        self.gridLayout_5.addWidget(self.pushButton_Temp_set, 0, 3, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 6)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 5, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 0, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 9, 0, 1, 1)
        self.label_Cam_OnOff = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Cam_OnOff.setFont(font)
        self.label_Cam_OnOff.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Cam_OnOff.setObjectName("label_Cam_OnOff")
        self.gridLayout.addWidget(self.label_Cam_OnOff, 2, 4, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 3, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 10, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_13.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_13.setSpacing(6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_Acq_mode = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Acq_mode.setFont(font)
        self.label_Acq_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Acq_mode.setObjectName("label_Acq_mode")
        self.gridLayout_9.addWidget(self.label_Acq_mode, 0, 0, 1, 1)
        self.comboBox_Acq_mode = QtWidgets.QComboBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_Acq_mode.setFont(font)
        self.comboBox_Acq_mode.setObjectName("comboBox_Acq_mode")
        self.gridLayout_9.addWidget(self.comboBox_Acq_mode, 0, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 4, 1, 1, 3)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 0, 1, 1, 1)
        self.pushButton_Snap = QtWidgets.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Snap.setFont(font)
        self.pushButton_Snap.setObjectName("pushButton_Snap")
        self.gridLayout.addWidget(self.pushButton_Snap, 11, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 4, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_15.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_15.setSpacing(6)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.doubleSpinBox_Exp_Time = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_Exp_Time.setFont(font)
        self.doubleSpinBox_Exp_Time.setDecimals(3)
        self.doubleSpinBox_Exp_Time.setMinimum(0.0)
        self.doubleSpinBox_Exp_Time.setMaximum(5.0)
        self.doubleSpinBox_Exp_Time.setSingleStep(0.001)
        self.doubleSpinBox_Exp_Time.setObjectName("doubleSpinBox_Exp_Time")
        self.gridLayout_7.addWidget(self.doubleSpinBox_Exp_Time, 0, 1, 1, 1)
        self.label_Exp_time_disp = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Exp_time_disp.setFont(font)
        self.label_Exp_time_disp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Exp_time_disp.setObjectName("label_Exp_time_disp")
        self.gridLayout_7.addWidget(self.label_Exp_time_disp, 0, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 5, 1, 1, 3)
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_Trig_mode = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Trig_mode.setFont(font)
        self.label_Trig_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Trig_mode.setObjectName("label_Trig_mode")
        self.gridLayout_11.addWidget(self.label_Trig_mode, 0, 0, 1, 1)
        self.comboBox_trig_mode = QtWidgets.QComboBox(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_trig_mode.setFont(font)
        self.comboBox_trig_mode.setObjectName("comboBox_trig_mode")
        self.gridLayout_11.addWidget(self.comboBox_trig_mode, 0, 1, 1, 1)
        self.pushButton_trig_mode = QtWidgets.QPushButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_trig_mode.setFont(font)
        self.pushButton_trig_mode.setObjectName("pushButton_trig_mode")
        self.gridLayout_11.addWidget(self.pushButton_trig_mode, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_8, 10, 1, 1, 4)
        self.pushButton_soft_trigger = QtWidgets.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_soft_trigger.setFont(font)
        self.pushButton_soft_trigger.setObjectName("pushButton_soft_trigger")
        self.gridLayout.addWidget(self.pushButton_soft_trigger, 10, 5, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        cam_gui.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(cam_gui)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 863, 21))
        self.menuBar.setObjectName("menuBar")
        cam_gui.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(cam_gui)
        self.mainToolBar.setObjectName("mainToolBar")
        cam_gui.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(cam_gui)
        self.statusBar.setObjectName("statusBar")
        cam_gui.setStatusBar(self.statusBar)

        self.retranslateUi(cam_gui)
        QtCore.QMetaObject.connectSlotsByName(cam_gui)

    def retranslateUi(self, cam_gui):
        _translate = QtCore.QCoreApplication.translate
        cam_gui.setWindowTitle(_translate("cam_gui", "cam_gui"))
        self.pushButton_Save.setText(_translate("cam_gui", "Save"))
        self.groupBox_5.setTitle(_translate("cam_gui", "Read Mode"))
        self.label_Read_mode.setText(_translate("cam_gui", "N/A"))
        self.groupBox_3.setTitle(_translate("cam_gui", "EMCCD Gain"))
        self.label_EMCCDGain_disp.setText(_translate("cam_gui", "0"))
        self.pushButton_Cam_Off.setText(_translate("cam_gui", "Camera OFF"))
        self.groupBox_7.setTitle(_translate("cam_gui", "Image Area"))
        self.label_10.setText(_translate("cam_gui", "Start Row:"))
        self.label_End_col.setText(_translate("cam_gui", "512"))
        self.label_Start_row.setText(_translate("cam_gui", "1"))
        self.label_End_row.setText(_translate("cam_gui", "512"))
        self.label_9.setText(_translate("cam_gui", "End Column:"))
        self.label_11.setText(_translate("cam_gui", "End Row:"))
        self.label_4.setText(_translate("cam_gui", "Start Column:"))
        self.label_Start_col.setText(_translate("cam_gui", "1"))
        self.groupBox_6.setTitle(_translate("cam_gui", "Kinetic Settings"))
        self.label_8.setText(_translate("cam_gui", "Kinetic Cycle Time:"))
        self.label_7.setText(_translate("cam_gui", "Number in Kinetic Series:"))
        self.label_no_Kin.setText(_translate("cam_gui", "1"))
        self.label_Kin_time.setText(_translate("cam_gui", "0 s"))
        self.label_2.setText(_translate("cam_gui", "Number of Accumulations:"))
        self.label_Accum_time.setText(_translate("cam_gui", "0 s"))
        self.label_3.setText(_translate("cam_gui", "Accumulation Cycle Time:"))
        self.label_no_Accum.setText(_translate("cam_gui", "1"))
        self.label_6.setText(_translate("cam_gui", "Picture:"))
        self.pushButton_Cam_On.setText(_translate("cam_gui", "Camera ON"))
        self.pushButton_Browse.setText(_translate("cam_gui", "Browse"))
        self.label.setText(_translate("cam_gui", "Initialisation:"))
        self.groupBox.setTitle(_translate("cam_gui", "Temperature"))
        self.label_Cooler_OnOff.setText(_translate("cam_gui", "OFF"))
        self.label_Temp_disp.setText(_translate("cam_gui", "0 °C"))
        self.pushButton_Temp_set.setText(_translate("cam_gui", "Set"))
        self.label_Cam_OnOff.setText(_translate("cam_gui", "OFF"))
        self.groupBox_4.setTitle(_translate("cam_gui", "Acquisition Mode"))
        self.label_Acq_mode.setText(_translate("cam_gui", "N/A"))
        self.pushButton_Snap.setText(_translate("cam_gui", "Snap"))
        self.groupBox_2.setTitle(_translate("cam_gui", "Exposure Time"))
        self.label_Exp_time_disp.setText(_translate("cam_gui", "0 s"))
        self.groupBox_8.setTitle(_translate("cam_gui", "Trigger Mode"))
        self.label_Trig_mode.setText(_translate("cam_gui", "N/A"))
        self.pushButton_trig_mode.setText(_translate("cam_gui", "Set Trigger Mode"))
        self.pushButton_soft_trigger.setText(_translate("cam_gui", "Software Trigger"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cam_gui = QtWidgets.QMainWindow()
    ui = Ui_cam_gui()
    ui.setupUi(cam_gui)
    cam_gui.show()
    sys.exit(app.exec_())

