import serial
import serial.tools.list_ports
import re
import json
from random import randint


def getPorts():
    allPorts = serial.tools.list_ports.comports()
    ports = []
    for (port, desc, hwid) in sorted(allPorts):
        ports.append(port)
    return ports

"""
def begin():
    ports = getPorts()
    json_data = []

    for port in ports:
        ser = serial.Serial(port, 9600)
        lineCount = 0
        while True:
            if lineCount < 2:
                data = ser.readline()
                data = data.decode().strip()
                if lineCount == 0 and 'L/hour' not in data:
                    continue

                if 'L/hour' in data:
                    data = re.sub(' L/hour', '', data)

                if 'cm' in data:
                    data = re.sub('[0-9]in, ', '', data)
                    data = re.sub('cm', '', data)
                
                json_data.append(data)
            else:
                break
            lineCount = lineCount + 1

        break

    return json.dumps(json_data)
"""

def begin():
    data = [
        randint(0, 15),
        randint(5,254)
    ]
    return json.dumps(data)