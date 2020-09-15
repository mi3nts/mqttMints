

# import serial
# ser = serial.Serial('/dev/ttyACM3')
import serial
import datetime
import os
import csv
import deepdish as dd
import time
import json

from mintsXU4 import mintsDefinitions as mD
import paho.mqtt.publish as publish

dataFolder      = mD.dataFolder
latestDisplayOn = mD.latestDisplayOn
macAddress      = mD.macAddress

def writeJSONLatest(sensorDictionary,sensorName):
    directoryIn  = dataFolder+"/"+macAddress+"/"+sensorName+".json"
    print(directoryIn)
    try:
        with open(directoryIn,'w') as fp:
            json.dump(sensorDictionary, fp)

    except:
        print("Json Data Not Written")


def writeMQTTLatest(sensorDictionary,sensorName):
    try:
        publish.single(macAddress+"/"+sensorName,json.dumps(sensorDictionary), hostname="10.173.44.186")

    except:
        print("MQTT Data not Published")        



def readJSONLatestAll(sensorName):
    try:
        directoryIn  = dataFolder+"/"+macAddress+"/"+sensorName+".json"
        with open(directoryIn, 'r') as myfile:
            # dataRead=myfile.read()
            dataRead=json.load(myfile)

        time.sleep(0.01)
        return dataRead, True;
    except:
        print("Data Conflict!")
        return "NaN", False




# def writeHDF5Latest(writePath,sensorDictionary,sensorName):
#     try:
#         dd.io.save(dataFolder+sensorName+".h5", sensorDictionary)
#     except:
#         print("Data Conflict!")

# def readHDF5LatestAll(sensorName):
#     try:
#         d = dd.io.load(dataFolder+sensorName+".h5")
#         # print("-------------------------------------")
#         # # print(sensorName)
#         # # print(d)
#         time.sleep(0.01)
#         return d, True
#     except:
#         print("Data Conflict!")
#         return "NaN", False
#
# def readHDF5LatestData(sensorName,keyIn):
#     try:
#         d = dd.io.load(dataFolder+sensorName+".h5")
#         # print("-------------------------------------")
#         # print(sensorName)
#         # print(d[keyIn])
#         time.sleep(0.01)
#         return str(d[keyIn]),True
#     except:
#         print("Data Conflict!")
#         return {}, False



# def writeJSONLatestUnpublished(sensorDictionary,sensorName):
#     # print(writePath)
#     if(latestDisplayOn):
#         directoryIn  = dataFolderUnpublished+"/"+macAddress+"/"+sensorName+".json"
#         # print(directoryIn)
#         try:
#         	with open(directoryIn,'w') as fp:
#         	    json.dump(sensorDictionary, fp)
#         except:
#             print("Data Conflict!")
