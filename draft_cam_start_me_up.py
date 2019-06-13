# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:24:30 2019

@author: IonTrap/YWu
"""
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
import time
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
        self.temp_flag = False
        
        #--- data ------------------------------------------------------------#
        self.data_camera = []

        #--- the object with all the functions within instr_Andor_iXon_ultra
        self.cam = Andor()
        
        #---camera monitoring variables ------------------------------------------------------------#

        self.acquistion_mode = None
        self.read_mode = None
        self.exp_time = None
        self.EMCCD_Gain= None

       
        #-- Push Buttons -----------------------------------------------------#
        self.pushButton_Cam_On.clicked.connect(self.initialise_thread)
        self.pushButton_Cam_Off.clicked.connect(self.cam_off)
        self.pushButton_Temp_set.clicked.connect(self.temp_thread)
        self.pushButton_Snap.clicked.connect(self.snap_thread)
        self.pushButton_Save.clicked.connect(self.save_pic)


#-- Initialise camera -----------------------------------------------------#
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
                
                
                self.cam.Initialize()
                print('---> camera with handle = ' + str(self.cam.camerahandle) + ' initialized.')
                self.label_Cam_OnOff.setText('ON')
                self.label_Cam_OnOff.setStyleSheet('color: green')
                self.cam.GetTemperature()
                self.label_Temp_disp.setText(str(self.cam.temperature) + ' °C')
                self.cam_flag = True

                print('Camera ON!!')
             
            else:
                print('PROBLEM: check connection and power of camera and try again.')
        
        elif self.cam_flag == True:
            print('camera already on')
            None


#-- shuts down camera and cooler-----------------------------------------------------#    
    def cam_off(self):
        if self.cam_flag == True:
            print('Camera Shutdown')
            self.cam_flag = False
            self.cooler_flag = False
            self.cam.CoolerOFF()
            self.cam.ShutDown()            
            self.label_Cam_OnOff.setText('OFF')
            self.label_Cam_OnOff.setStyleSheet('color: red')
            self.label_Cooler_OnOff.setText('OFF')
            self.label_Cooler_OnOff.setStyleSheet('color: red')
            
        
        elif self.cam_flag == False:
            print("camera already off")
            
#-- starts thread which initialises camera -----------------------------------------------------#    
    def initialise_thread(self):
        init_thread = threading.Thread(target =self.initialise_cam)
        init_thread.start()

#-- retrieves temperature data every 3 seconds -----------------------------------------------------#            
    def temp_update(self):
        while self.cam_flag == True:
            self.cam.GetTemperature()
            time.sleep(3)
            

#-- turns cooler on and off and starts live display of temperature monitoring-----------------------#        
    def set_temp(self):
        if self.cam_flag == True:
            if self.cooler_flag == False:
                
                self.cooler_on()            
                self.cooler_flag = True
    
                temp_thread = threading.Thread(target = self.temp_disp)
                temp_thread.start()
                
            elif self.cooler_flag == True:
                self.cooler_off()
                self.cooler_flag = False
                self.temp_flag = False
        
        elif self.cam_flag == False:
            print('camera not on')
            None
            

#-- starts thread for self.temp_update and calls self.self_temp -----------------------------------------------------#     
    def temp_thread(self):
        temp_thread = threading.Thread(target = self.temp_update)
        temp_thread.start()
        self.set_temp()
        

#-- turns cooler on -----------------------------------------------------#      
    def cooler_on(self):
        temp = self.doubleSpinBox_Temp_set.value()
        self.cam.SetTemperature(round(temp))
        self.cam.CoolerON()
        self.label_Cooler_OnOff.setText('ON')
        self.label_Cooler_OnOff.setStyleSheet('color: green')


#-- turns cooler off and displays final temperature -----------------------------------------------------#          
    def cooler_off(self):
        self.cam.CoolerOFF()
        self.label_Cooler_OnOff.setText('OFF')
        self.label_Cooler_OnOff.setStyleSheet('color: red')
        self.cam.GetTemperature()
        temp2 = self.cam.temperature
        self.label_Temp_disp.setText(str(temp2) + ' °C')
        

#-- live temperature display -----------------------------------------------------#      
    def temp_disp(self):
        while self.cooler_flag == True:
            self.label_Temp_disp.setText(str(self.cam.temperature) + ' °C')
            time.sleep(4)
            
                        
#-- sets modes, exposure time, EMCCD gain and snaps pic -----------------------------------------------------#      
    def snap_pic(self):
        exp_time = self.doubleSpinBox_Exp_Time.value()
        EMCCD_gain = self.doubleSpinBox_EMCCD_Gain.value()
        self.set_Read_mode()
        self.cam.SetImage(1,1,1,512,1,512)
        self.set_Acq_mode()
        self.cam.SetExposureTime(exp_time)
        self.cam.SetEMCCDGain(round(EMCCD_gain))
        self.snap_setting_disp()
        self.Acq_mode_disp()
        self.Read_mode_disp()
        self.cam.StartAcquisition()

        time.sleep(5)
        data_camera = []
        self.cam.GetAcquiredData(data_camera)
        self.data_camera = data_camera
        print('Snap Complete!')


#-- starts thread which calls self.snap_pic -----------------------------------------------------#          
    def snap_thread(self):
        snap = threading.Thread(target = self.snap_pic)
        snap.start()
        
        
#-- saves picture as .txt file -----------------------------------------------------#          
    def save_pic(self):
        self.cam.SaveAsTxt2('test.txt')
        print('Save Complete!')
        

#-- displays the camera setting of previous snap -----------------------------------------------------#              
    def snap_setting_disp(self):
        #print(self.exp_time)
        #print(self.EMCCD_Gain)
        self.cam.GetEMCCDGain()
        self.EMCCD_Gain = self.cam.gain
        self.exp_time = self.cam.exposure
        self.label_Exp_time_disp.setText(str(self.exp_time)[:5]+ ' s')
        self.label_EMCCDGain_disp.setText(str(self.EMCCD_Gain))
        

#-- sets Acquisition mode from user input -----------------------------------------------------#            
    def set_Acq_mode(self):
        Acq = str(self.lineEdit_acq_mode.text())
        if Acq.casefold() == 'Single Scan'.casefold():       #makes it case insensitive
            self.cam.SetAcquisitionMode(1)
        elif Acq.casefold() == 'Kinetic Scan'.casefold():
            self.cam.SetAcquisitionMode(3)
        else:
            print('Invalid Acquisition Mode: ' + str(self.lineEdit_acq_mode.text()))
            print('Available Acquisition Modes: Single Scan, Kinetic Scan')
            if str(self.label_Acq_mode.text()) != 'N/A':
                print('previous Acquisition mode used')
                

#-- displays Acquisition mode from previous snap-----------------------------------------------------#            
    def Acq_mode_disp(self):
        self.acquistion_mode = self.cam.AcquisitionMode
        
        if self.acquistion_mode == 1:
            self.label_Acq_mode.setText('Single Scan')
        elif self.acquistion_mode == 3:
            self.label_Acq_mode.setText('Kinetic Scan')
        else:
            self.label_Acq_mode.setText('N/A')
            
    
#-- sets Read mode from user input -----------------------------------------------------#        
    def set_Read_mode(self):
        Read = str(self.lineEdit_read_mode.text()).casefold() 
        if Read.casefold() == 'Full vertical binning'.casefold():    #makes it case insensitive
            self.cam.SetReadMode(0)
        elif Read.casefold() == 'Multi track'.casefold():
            self.cam.SetReadMode(1)
        elif Read.casefold() == 'Random track'.casefold():
            self.cam.SetReadMode(2)
        elif Read.casefold() == 'Single track'.casefold():
            self.cam.SetReadMode(3)
        elif Read.casefold() == 'Image'.casefold():
            self.cam.SetReadMode(4)
        else:
            print('Invalid Read Mode: ' + str(self.lineEdit_read_mode.text()))
            
            if str(self.label_Read_mode.text()) != 'N/A':
                print('Available Read Modes: Full vertical binning, Multi track, Single track, Image'  )
                print('previous Read mode used' + '\n')
            else:
                print('Available Read Modes: Full vertical binning, Multi track, Single track, Image' + '\n' )
                

#-- displays Read mode from previous snap -----------------------------------------------------#       
    def Read_mode_disp(self):
        self.read_mode = self.cam.ReadMode
        if self.read_mode == 0:
            self.label_Read_mode.setText('Full vertical binning')
        elif self.read_mode == 1:
            self.label_Read_mode.setText('Multi track')
        elif self.read_mode == 2:
            self.label_Read_mode.setText('Random track')
        elif self.read_mode == 3:
            self.label_Read_mode.setText('Single track')
        elif self.read_mode == 4:
            self.label_Read_mode.setText('Image')
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    dialog = QtWidgets.QMainWindow()
    
    programm = window_camera(dialog)
    dialog.show()
    
    sys.exit(app.exec_())