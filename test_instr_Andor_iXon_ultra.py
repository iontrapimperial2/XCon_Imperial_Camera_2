# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:37:04 2019

@author: IonTrap/JMHeinrich
"""

from time import time

from instr_Andor_iXon_ultra import Andor



#--- create an empty container for the cam object ----------------------------#
cam = Andor()



#--- check how many cameras are in the system and get their handles ----------#
cam.GetAvailableCameras() # saves num avail. cameras in camera.availablecamera

print('---> number available cameras: ' + str(cam.availablecamera))

if cam.availablecamera > 0:
    #--- get handle of camera 0 since only one is connected ------------------#
    cam.GetCameraHandle(0) # saves camera handle in camera.camerahandle
    
    print('---> camera handle of available camera: ' + str(cam.camerahandle))
    
    #--- choose current camera to be the one with the handle from above ------#
    cam.SetCurrentCamera(cam.camerahandle)
    
    print('---> camera with handle = ' + str(cam.camerahandle) + ' selected.')
else:
    print('PROBLEM: check connection and power of camera and try again.')



#--- Initialize the selected camera ------------------------------------------#
cam.Initialize()

#--- set the cooling temperature and start the cooling -----------------------#
cam.SetTemperature(-70)
cam.CoolerON()



#--- set the Read Mode, the image size, Aquisition Mode and Exp time ---------#
cam.SetShutterEx(1,1,27,27,1)
cam.SetEMCCDGain(300)
cam.SetReadMode(4)
cam.SetImage(1,1,1,500,1,500)
cam.SetAcquisitionMode(1)
cam.SetExposureTime(1)
#cam.SetKineticCycleTime(0.015)
#cam.SetNumberKinetics(10)



#--- start the aquisition ----------------------------------------------------#
cam.StartAcquisition()

#for i in range(1,11,1):
 #   print(i)
#cam.dll.WaitForAcquisition()
#cam.dll.WaitForAcquisition()
#cam.dll.WaitForAcquisition()
#cam.dll.WaitForAcquisition()
#cam.dll.WaitForAcquisition()
#cam.dll.WaitForAcquisition()
#cam.dll.WaitForAcquisition()
#cam.dll.WaitForAcquisition()
#cam.dll.WaitForAcquisition()
cam.dll.WaitForAcquisition()

#--- get the acquired data ---------------------------------------------------#
data_camera = []
cam.GetAcquiredData(data_camera)

#--- save the acquired data --------------------------------------------------#
#cam.SaveAsTxt2('test.txt')
print(data_camera)
print('Snap Complete!')

#--- cooler off --------------------------------------------------------------#
cam.CoolerOFF()      
cam.ShutDown()  















#
#camera.GetCameraSerialNumber()
#
#print(camera.serial)
#
#
#
#camera.SetSingleScan()
##camera.SetTriggerMode(0)
##camera.SetShutter(1,0,1,1)
##camera.SetPreAmpGain(None)
##camera.SetEMCCDGain(None)
#camera.SetExposureTime(10)
#camera.StartAcquisition()
#data_camera = []
#camera.GetAcquiredData(data_camera)
#
#
#camera.ShutDown()