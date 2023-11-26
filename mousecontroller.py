#!/usr/bin/env python
import subprocess
from logging import config,getLogger


command = "system_profiler SPUSBDataType"
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

config.dictConfig({
    'version': 1,
    'formatters': {
        'Formatter':{
            'format': '%(asctime)s %(name)-10s %(levelname)-8s %(message)s'}
    },
    'handlers': {
        'testHandler': {
            'class': 'logging.FileHandler',
            'formatter': 'Formatter',
            'level': "INFO",
            'filename': 'test.log',
        }
    },
    'root': {
        'handlers': ['testHandler'],
        'level': "WARNING"
    },
    'loggers': {
        'Logger': {
            'handlers': ['testHandler'],
            'level': "INFO",
            'propagate': 0
        }
    }
})
Logger = getLogger("Logger")

if result.stderr == "":
    
    output = result.stdout
    if "Mouse" in output:
        
        command2 = "defaults read -g com.apple.swipescrolldirection"
        result2 = subprocess.run(command2,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True,text=True)
        output2 = result2.stdout
        
        if int(output2) != 0:
            command3 = "defaults write -g com.apple.swipescrolldirection -bool false"
            Logger.info("Natrual scroll off")
            subprocess.run(command3,shell=True)
            command4 = "sudo pkill loginwindow"
            Logger.info("Log off")
            subprocess.run(command4,shell=True)    
        else:
            exit()
    
    else:
        command5 = "defaults read -g com.apple.swipescrolldirection"
        result3 = subprocess.run(command5,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True,text=True)
        output3 = result3.stdout

        if int(output3) != 1:
            command6 = "defaults write -g com.apple.swipescrolldirection -bool true"
            Logger.info("Natrual scroll on")
            subprocess.run(command6,shell=True)
            command7 = "sudo pkill loginwindow"
            Logger.info("Log off")
            subprocess.run(command7,shell=True) 
        else:
            exit()

else:
    Logger.error(result.stderr)



