import subprocess

###################################################################################################

def ShowTextOnLCDInThread(text):
    subprocess.call(["./rpi_cpu_infoscreen/test_bcm8544", text])

###################################################################################################

def ShowTextOnLCD(text):
    global lastText
    if(text == lastText):
        return

    t1 = threading.Thread(target=ShowTextOnLCDInThread, args=(text,))
    t1.start()
    lastText = text