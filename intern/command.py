import time
import sys
import ibmiotf.application
import ibmiotf.device

# Provide your IBM Watson Device Credentials
organization = "o9hvpe"  #  organization ID
deviceType = "controllerdata"  # device type
deviceId = "0001"  #  device id
authMethod = "token"
authToken = "8072958226"  #  token


def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data)
    if cmd.data['command'] == 'motor_on':
        print("MOTOR ON")
    elif cmd.data['command'] == 'motor_off':
        print("MOTOR OFF")


try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod,
                     "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)


except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()

deviceCli.connect()

while True:
    T = 34;
    H = 27;
    O = 29;


    data = {'d':{'temperature': T, 'humidity': H,'objectTemp':O,}}


   
    def myOnPublishCallback():
        print("Published Temperature = %s C" % T, "Humidity = %s %%" % H, "objectTemp = %s C" %O ,"to IBM Watson")


    success = deviceCli.publishEvent("event", "json", data, qos=0, on_publish=myOnPublishCallback)
    if not success:
        print("Not connected to IoTF")
    time.sleep(1)

    deviceCli.commandCallback = myCommandCallback


deviceCli.disconnect()