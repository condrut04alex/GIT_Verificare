import serial.tools.list_ports

def afiseaza_com_ports():

    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
    print("Connected COM ports: " + str(connected))
    print(str(connected[0]))
    
    return str(connected)
print(afiseaza_com_ports())