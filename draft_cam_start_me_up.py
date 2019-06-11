# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:24:30 2019

@author: IonTrap/YWu
"""
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
from time import time
import threading
from cam_gui import Ui_cam_gui
from instr_Andor_iXon_ultra import Andor



class window_camera(Ui_cam_gui):
    def __init__(self, dialog):
        Ui_cam_gui.__init__(self)
        self.setupUi(dialog)

        #--- flags -----------------------------------------------------------#
        self.cam_flag = False
        self.cooler_flag = False
        
        #--- data ------------------------------------------------------------#
        self.data_camera = []

        #--- the object with all the functions within instr_Andor_iXon_ultra
        self.cam = Andor()
        

       
        #-- Push Buttons -----------------------------------------------------#
#        self.pushButton_Cam_OnOff.clicked.connect(self.initialise_cam)
        self.pushButton_Cam_OnOff.clicked.connect(self.initialise_thread)
        self.pushButton_Temp_set.clicked.connect(self.set_temp)
#        self.pushButton_Exp_Time.clicked.connect(self.set_exp_time)
        self.pushButton_Snap.clicked.connect(self.snap_pic)
        self.pushButton_Save.clicked.connect(self.save_pic)
           
#    def initialise_cam(self):
#        if self.cam_flag == False:
#            self.cam.GetAvailableCameras()
#            if self.cam.availablecamera > 0:
#                #--- get handle of camera 0 since only one is connected ------------------#
#                self.cam.GetCameraHandle(0) # saves camera handle in camera.camerahandle
#                
#                print('---> camera handle of available camera: ' + str(self.cam.camerahandle))
#                
#                #--- choose current camera to be the one with the handle from above ------#
#                self.cam.SetCurrentCamera(self.cam.camerahandle)
#                
#                print('---> camera with handle = ' + str(self.cam.camerahandle) + ' selected.')
#            else:
#                print('PROBLEM: check connection and power of camera and try again.')
#            
#            self.cam.Initialize()
#            self.label_Cam_OnOff.setText('ON')
#            self.label_Cam_OnOff.setStyleSheet('color: green')
#            self.cam_flag = True
#        
#        elif self.cam_flag == True:
#            self.cam.CoolerOFF()
#            self.cam.ShutDown()
#            self.label_Cam_OnOff.setText('OFF')
#            self.label_Cam_OnOff.setStyleSheet('color: red')
#            self.cam_flag = False

    def initialise_cam(self):
        if self.cam_flag == False:
            self.cam.GetAvailableCameras()
            if self.cam.availablecamera > 0:
                #--- get handle of camera 0 since only one is connected ------------------#
                self.cam.GetCameraHandle(0) # saves camera handle in camera.camerahandle
                
                print('---> camera handle of available camera: ' + str(self.cam.camerahandle))
                
                #--- choose current camera to be the one with the handle from above ------#
                self.cam.SetCurrentCamera(self.cam.camerahandle)
                
                print('---> camera with handle = ' + str(self.cam.camerahandle) + ' selected.')
                
                self.cam_flag = True
                self.cam.Initialize()
                print('---> camera with handle = ' + str(self.cam.camerahandle) + ' initialized.')
                self.label_Cam_OnOff.setText('ON')
                self.label_Cam_OnOff.setStyleSheet('color: green')
                
                while self.cam_flag == True:
                    self.cam.GetTemperature()
                    time.sleep(3)
                    
                print('Camera Shutdown')
                self.cam.CoolerOFF()
                self.cam.ShutDown()
                self.label_Cam_OnOff.setText('OFF')
                self.label_Cam_OnOff.setStyleSheet('color: red')
                self.cam_flag = False                
            else:
                print('PROBLEM: check connection and power of camera and try again.')
     
        elif self.cam_flag == True:
            print('Camera Shutdown')
            self.cam.CoolerOFF()
            self.cam.ShutDown()
            self.label_Cam_OnOff.setText('OFF')
            self.label_Cam_OnOff.setStyleSheet('color: red')
            self.cam_flag = False
        
    def initialise_thread(self):
        init_thread = threading.Thread(target =self.initialise_cam)
        init_thread.start()         
        
    def set_temp(self):
        temp = self.doubleSpinBox_Temp_set.value()
        if self.cooler_flag == False:
            print(round(temp))
            self.cam.SetTemperature(round(temp))
            self.cam.CoolerON()
            self.label_Cooler_OnOff.setText('ON')
            self.label_Cooler_OnOff.setStyleSheet('color: green')
            self.cam.GetTemperature()
            temp1 = self.cam.temperature
            print(temp1)
            self.label_Temp_disp.setText(str(temp1) + '°C')
            self.cooler_flag = True
            
        elif self.cooler_flag == True:
            self.cam.CoolerOFF()
            self.label_Cooler_OnOff.setText('OFF')
            self.label_Cooler_OnOff.setStyleSheet('color: red')
            self.cam.GetTemperature()
            temp2 = self.cam.temperature
            self.label_Temp_disp.setText(str(temp2))
            self.cooler_flag = False
    
    def snap_pic(self):
        exp_time = self.doubleSpinBox_Exp_Time.value()
        EMCCD_gain = self.doubleSpinBox_EMCCD_Gain.value()
        print(exp_time)
        print(EMCCD_gain)
        self.cam.SetReadMode(4)
        self.cam.SetImage(1,1,1,512,1,512)
        self.cam.SetAcquisitionMode(1)
        self.cam.SetExposureTime(exp_time)
        self.cam.setEMCCDGain(round(EMCCD_gain))
        self.cam.StartAcquisition()

        time.sleep(5)
        data_camera = []
        self.cam.GetAcquiredData(data_camera)
        self.data_camera = data_camera
        print(self.data_camera)
    
    def save_pic(self):
        print(self.data_camera)
        self.cam.SaveAsTxt2('test.txt')
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    dialog = QtWidgets.QMainWindow()
    
    programm = window_camera(dialog)
    dialog.show()
    
    sys.exit(app.exec_())