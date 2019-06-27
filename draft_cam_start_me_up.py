# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:24:30 2019

@author: IonTrap/YWu
"""
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
import time
from datetime import datetime
import threading
from cam_gui import Ui_cam_gui
from instr_Andor_iXon_ultra import Andor



class window_camera(Ui_cam_gui):
    def __init__(self, dialog):
        Ui_cam_gui.__init__(self)
        self.setupUi(dialog)
        
        self.start_col = self.doubleSpinBox_Start_col.value()
        self.end_col = self.doubleSpinBox_End_col.value()
        self.start_row = self.doubleSpinBox_Start_row.value()
        self.end_row = self.doubleSpinBox_End_row.value()

        #--- flags -----------------------------------------------------------#
        self.cam_flag = False
        self.cooler_flag = False
        self.temp_flag = False
        self.snap_flag = False
        self.abort_flag = False
        
        #--available read modes, acquisition modes, trigger modes, EM gain modes and pre-amp gains-----------------------------------------------------#
        self.list_read_modes = ['Image', 'Full vertical binning','Multi track', 'Random track', 'Single track']
        self.list_Acq_modes = ['Single Scan', 'Kinetic Scan']
        self.list_trig_modes = ['Internal', 'External', 'External Start', 'External Exposure']
        self.list_preamp_gain = ['1','2','3']
        self.list_EM_gain_mode = ['0','1','2','3']
        self.list_Shutter = ['Fully Auto', 'Permanently Open', 'Permanently Closed']
        
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
        self.pushButton_Browse.clicked.connect(self.Browse_data)
        self.pushButton_Save.clicked.connect(self.save_pic)
        self.pushButton_trig_mode.clicked.connect(self.set_trig_mode)
        self.pushButton_VSAmp.clicked.connect(self.setVSAmp)
        self.pushButton_preamp_gain.clicked.connect(self.set_preamp_gain)
        self.pushButton_EM_gain_mode.clicked.connect(self.set_EM_gain_mode)
        self.pushButton_set_shutter.clicked.connect(self.set_shutter)
        self.pushButton_Abort.clicked.connect(self.Abort_snap)
        

        #-- combo boxes-----------------------------------------------------#
        self.comboBox_Read_mode.addItems(self.list_read_modes )
        self.comboBox_Acq_mode.addItems(self.list_Acq_modes)
        self.comboBox_trig_mode.addItems(self.list_trig_modes)
        self.comboBox_preamp_gain.addItems(self.list_preamp_gain)
        self.comboBox_EM_gain_mode.addItems(self.list_EM_gain_mode)
        self.comboBox_set_shutter.addItems(self.list_Shutter)

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
            self.snap_flag = False
            self.abort_flag = False
            self.cam.CoolerOFF()
            self.cam.ShutDown()            
            self.label_Cam_OnOff.setText('OFF')
            self.label_Cam_OnOff.setStyleSheet('color: red')
            self.label_Cooler_OnOff.setText('OFF')
            self.label_Cooler_OnOff.setStyleSheet('color: red')
            self.label_Accum_time.setText('0.000 s')
            self.label_Acq_mode.setText('N/A')
            self.label_EM_gain_mode.setText('0')
            self.label_EMCCDGain_disp.setText('0')
            self.label_Exp_time_disp.setText('0 s')
            self.label_Start_col.setText('1')
            self.label_Start_row.setText('1')
            self.label_End_col.setText('512')
            self.label_End_row.setText('512')
            self.label_Kin_time.setText('0 s')
            self.label_no_Accum.setText('1')
            self.label_no_Kin.setText('1')
            self.label_preamp_gain.setText('1')
            self.label_Read_mode.setText('N/A')
            self.label_set_shutter.setText('N/A')
            self.label_Trig_mode.setText('N/A')
            self.label_VSAmp.setText('0 V')
            
            
        
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
            
            
#-- sets Vertical Clock Voltage Amplitude -----------------------------------------------------#      
    def setVSAmp(self):
        v = int(self.doubleSpinBox_VSAmp.value())
        self.cam.SetVSAmplitude(v)
        self.label_VSAmp.setText(str(v) + ' V')


#-- sets EM gain mode -----------------------------------------------------#     
    def set_EM_gain_mode(self):
        mode = int(self.comboBox_EM_gain_mode.currentText())
        self.label_EM_gain_mode.setText(str(mode))
        self.cam.SetEMCCDGainMode(mode)
        

#-- sets shutter mode -----------------------------------------------------#      
    def set_shutter(self):
        if str(self.comboBox_set_shutter.currentText()) == 'Fully Auto':
            self.cam.SetShutterEx(1,0,27,27,1)
        elif str(self.comboBox_set_shutter.currentText()) == 'Permanently Open':
            self.cam.SetShutterEx(1,1,27,27,1)
        elif str(self.comboBox_set_shutter.currentText()) == 'Permanently Closed':
            self.cam.SetShutterEx(1,2,27,27,2)
        self.label_set_shutter.setText(str(self.comboBox_set_shutter.currentText()))
            
                        
#-- sets modes, exposure time, EMCCD gain, image area and snaps pic -----------------------------------------------------#      
    def snap_pic(self):    
        
        exp_time = self.doubleSpinBox_Exp_Time.value()
        EMCCD_gain = self.doubleSpinBox_EMCCD_Gain.value()
        self.cam.SetExposureTime(exp_time)
        self.cam.SetEMCCDGain(int(EMCCD_gain))
        self.set_Read_mode()
        self.set_Acq_mode()        
        
        self.set_img_area()
        self.snap_setting_disp()
        self.Read_mode_disp()
        self.Acq_mode_disp()
        self.img_area_disp()
        if str(self.label_Acq_mode.text()).casefold() == 'kinetic Scan'.casefold():
            accum_time = self.doubleSpinBox_Accum_time.value()
            accum_no = self.doubleSpinBox_no_Accum.value()
            Kin_time = self.doubleSpinBox_Kin_time.value()
            Kin_no = self.doubleSpinBox_no_Kin.value()
            self.cam.SetAccumulationCycleTime(accum_time)
            self.cam.SetNumberAccumulations(round(accum_no))
            self.cam.SetKineticCycleTime(Kin_time)
            self.cam.SetNumberKinetics(round(Kin_no))
            self.Kin_disp() 
            self.cam.StartAcquisition()     
            
            for i in range(1,int(Kin_no)+1,1): 
                if self.abort_flag == False:
                    for i in range(1, int(accum_no)+1, 1):
                        if self.abort_flag == False:
                            self.cam.dll.WaitForAcquisition()
                            
                        elif self.abort_flag == True:
                            break
                        print(i)
                elif self.abort_flag == True:
                    break
                
                #time.sleep((accum_time*accum_no+Kin_time)*Kin_no*1.1) #make sure sleep time longer than acquisition time            
        else:
            self.cam.StartAcquisition()
            self.cam.dll.WaitForAcquisition()

        if self.abort_flag == False:
            data_camera = []
            self.cam.GetAcquiredData(data_camera)
            self.data_camera = data_camera
            print(self.data_camera)
            print('Snap Complete!')
            if self.checkBox_AutoSave.isChecked():
                self.save_pic()
                if str(self.lineEdit_Browse.text()) == '':
                    None
                else:
                    print('Autosave complete!' + '\n' + "Don't forget to set new file name for next autosave! :D")
            else:
                None
        elif self.abort_flag == True:
            print('Snap Aborted')
        self.snap_flag = False
        
        """
        if str(self.label_Trig_mode.text()) == 'External':
            if self.abort_flag == False:
                self.snap_thread()
                
            else:
                None
                """
        self.abort_flag = False

#-- starts thread which calls self.snap_pic -----------------------------------------------------#          
    def snap_thread(self):
        if self.snap_flag == False:
            snap = threading.Thread(target = self.snap_pic)
            snap.start()
            self.snap_flag = True
            print('yo')
        else:
            None


#-- aborts acquisition -----------------------------------------------------#          
    def Abort_snap(self):
        if self.snap_flag == True:
            self.abort_flag = True
            self.cam.AbortAcquisition()
            self.snap_flag = False
        else:
            None


#-- displays kinetic scan settings-----------------------------------------------------#                 
    def Kin_disp(self):
        self.label_Accum_time.setText(str(self.doubleSpinBox_Accum_time.text()) + ' s')
        self.label_no_Accum.setText(str(self.doubleSpinBox_no_Accum.text()))
        self.label_Kin_time.setText(str(self.doubleSpinBox_Kin_time.text())+ ' s')
        self.label_no_Kin.setText(str(self.doubleSpinBox_no_Kin.text()))


#-- sets image area-----------------------------------------------------#         
    def set_img_area(self):
        self.start_col = self.doubleSpinBox_Start_col.value()
        self.end_col = self.doubleSpinBox_End_col.value()
        self.start_row = self.doubleSpinBox_Start_row.value()
        self.end_row = self.doubleSpinBox_End_row.value()
        self.cam.width = int(self.end_col) - int(self.start_col) +1
        self.cam.height = int(self.end_row) - int(self.start_row) +1
        self.cam.SetImage(1,1,int(self.start_col),int(self.end_col),int(self.start_row),int(self.end_row))
        
        
#-- displays image area settings-----------------------------------------------------#         
    def img_area_disp(self):
        self.label_Start_col.setText(str(self.doubleSpinBox_Start_col.text()))
        self.label_End_col.setText(str(self.doubleSpinBox_End_col.text()))
        self.label_Start_row.setText(str(self.doubleSpinBox_Start_row.text()))
        self.label_End_row.setText(str(self.doubleSpinBox_End_row.text()))
        
        
#-- set preamplifier gain-----------------------------------------------------#           
    def set_preamp_gain(self):
        preamp_gain = int(self.comboBox_preamp_gain.currentText())
        self.cam.SetPreAmpGain(preamp_gain-1)
        self.label_preamp_gain.setText(str(preamp_gain))
        
        
        
#-- Browse save directory-----------------------------------------------------#               
    def Browse_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog    
        self.filename_pic, _ = QFileDialog.getSaveFileName(None,"save data", "","all files (*);; asc files (*.asc);; txt files (*.txt)", options=options)
        
        if self.filename_pic:
            self.lineEdit_Browse.setText(self.filename_pic) 
            
            
#-- saves picture as .txt file -----------------------------------------------------#          
    def save_pic(self):
        if str(self.lineEdit_Browse.text()) == '':
            print('Please set file name and location before saving!')
        
        else:
            print(self.start_col)
            print(self.end_col)
            print(self.start_row)
            print(self.end_row)
            width = self.end_col - self.start_col + 1
            height = self.end_row - self.start_row + 1
            print(int(width))
            print(int(height))
            if str(self.label_Acq_mode.text()) == 'Single Scan':
                self.cam.SaveAsTxt2(str(self.lineEdit_Browse.text()) + '.txt', 1, int(width), int(height))
            
            elif str(self.label_Acq_mode.text()) == 'Kinetic Scan':
                self.cam.SaveAsTxt2(str(self.lineEdit_Browse.text()) + '.txt', self.label_no_Kin.text(), int(width), int(height))
                
            self.save_cam_settings()
            print('Save Complete!')


#-- saves cam setting of snap as .txt file -----------------------------------------------------#                
    def save_cam_settings(self):
        a = self.label_Acq_mode.text()
        b = self.label_Read_mode.text()
        c = self.label_Temp_disp.text()
        d = self.label_Exp_time_disp.text()
        e = self.label_EMCCDGain_disp.text()
        f = self.label_no_Accum.text()
        g = self.label_Accum_time.text()
        h = self.label_no_Kin.text()
        i = self.label_Kin_time.text()
        j = self.label_Start_col.text()
        k = self.label_End_col.text()
        l = self.label_Start_row.text()
        m = self.label_End_row.text()
        n = self.label_Trig_mode.text()
        o = self.label_VSAmp.text()
        current_time = datetime.today()
        data_file = open(str(self.lineEdit_Browse.text()) + '_cam_settings.txt', 'a+') 
        if str(self.label_Acq_mode.text()).casefold() == 'Single Scan'.casefold():
            data_file.write('\n ' + '\n ' + str(current_time) + '\n ' + 'Acquisition Mode: ' + str(a)
                            + '\n ' + 'Read Mode: ' + str(b) + '\n ' + 'Temperature: ' + str(c)
                            + '\n ' + 'Exposure Time: ' + str(d) + '\n ' + 'EMCCD Gain: ' + str(e) 
                            + '\n ' + 'Start Column: ' + str(j) + '\n ' + 'End Column: ' + str(k) 
                            + '\n ' + 'Start Row: ' + str(l) + '\n ' + 'End Row: ' + str(m)
                            + '\n ' + 'Trigger Mode: ' + str(n) + '\n ' + 'Vertical Clock Voltage Amplitude: ' + str(o))
            data_file.close()
        elif str(self.label_Acq_mode.text()).casefold() == 'Kinetic Scan'.casefold():
            data_file.write('\n ' + '\n ' + str(current_time) + '\n ' + 'Acquisition Mode: ' + str(a)
                            + '\n ' + 'Read Mode: ' + str(b) + '\n ' + 'Temperature: ' + str(c)
                            + '\n ' + 'Exposure Time: ' + str(d) + '\n ' + 'EMCCD Gain: ' + str(e)
                            + '\n ' + 'No. of Accumulations: ' + str(f) + '\n ' + 'Accumulate Cycle Time: ' + str(g)
                            + '\n ' + 'No. of Kinetic Series: ' + str(h) + '\n ' + 'Kinetic Cycle Time: ' + str(i)
                            + '\n ' + 'Start Column: ' + str(j) + '\n ' + 'End Column: ' + str(k) 
                            + '\n ' + 'Start Row: ' + str(l) + '\n ' + 'End Row: ' + str(m)
                            + '\n ' + 'Trigger Mode: ' + str(n) + '\n ' + 'Vertical Clock Voltage Amplitude: ' + str(o))
            data_file.close()

#-- displays the camera setting of previous snap -----------------------------------------------------#              
    def snap_setting_disp(self):
        self.cam.GetEMCCDGain()
        self.EMCCD_Gain = self.cam.gain
        self.exp_time = self.cam.exposure
        self.label_Exp_time_disp.setText(str(self.exp_time)[:5]+ ' s')
        self.label_EMCCDGain_disp.setText(str(self.EMCCD_Gain))
        

#-- sets Acquisition mode from user input -----------------------------------------------------#            
    def set_Acq_mode(self):
        Acq = str(self.comboBox_Acq_mode.currentText())
        if Acq == 'Single Scan':
            self.cam.SetAcquisitionMode(1)
        elif Acq == 'Kinetic Scan':
            self.cam.SetAcquisitionMode(3)

                

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
        Read = str(self.comboBox_Read_mode.currentText())
        if Read == 'Full vertical binning':    
            self.cam.SetReadMode(0)
        elif Read == 'Multi track':
            self.cam.SetReadMode(1)
        elif Read == 'Random track':
            self.cam.SetReadMode(2)
        elif Read == 'Single track':
            self.cam.SetReadMode(3)
        elif Read == 'Image':
            self.cam.SetReadMode(4)


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
            
            
#-- sets Trigger mode from user input and displays trigger mode on label -----------------------------------------------------#        
    def set_trig_mode(self):
        trig = str(self.comboBox_trig_mode.currentText())
        self.label_Trig_mode.setText(trig)
        if trig == 'Internal':    
            self.cam.SetTriggerMode(0)
        elif trig == 'External':
            self.cam.SetTriggerMode(1)
        elif trig == 'External Start':
            self.cam.SetTriggerMode(6)
        elif trig == 'External Exposure':
            self.cam.SetTriggerMode(7)
        elif trig == 'Software':
            self.cam.SetTriggerMode(10)
        

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    dialog = QtWidgets.QMainWindow()
    
    programm = window_camera(dialog)
    dialog.show()
    
    sys.exit(app.exec_())