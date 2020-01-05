import serial
import datetime
import csv
from fft import nr_inregistrari,plot_fft
import os
import time


try:
    ser = serial.Serial('COM10',57600,timeout=.1)
    ser.isOpen() # try to open port, if possible print message and proceed with 'while True:'
    print ("port is opened!")

except IOError: # if port is already opened, close it and open it again and print message
    ser.close()
    ser.open()
    print ("port was already open, was closed and opened again!")
    line = ser.read()
    #print(line)
    
#x1 = ser.read(1)   
while True:
    x1 = ser.read(1)
    file_name = 'a5.csv'
    nume_save = "primul_test_bun"
    save_raw_value = nume_save + ".csv"
    save_wave_magnitude = save_raw_value + "magnitude.csv"
    
    #print('bitisori x1',x1)
    #print('bitisori',x1)
    if x1==0xaa or x1==b'\xaa' or x1==170:
        x2=ser.read(1)
        #print("x2..",x2)
        if x2==0xaa or x1==b'\xaa' or x2==170:
            length = ser.read(1)
            if length[0]!=0:
                data = ser.read(length[0])
         #       print("data==",data,"length==",length[0])
                chks = ser.read(1)
                code = data[0]
                if code==0x80 or code ==b'\x80' or code==128 : 
                    #print("code 0x80 ??..",code)
                    if os.path.isfile(file_name) ==False:
                        file = open(file_name , "a", newline='')
                    else:
                        k= nr_inregistrari(file_name)
                        if k>=200000 :
                            #plot_fft()
                            k = 0
                            plot_fft(file_name)
                            f = open(file_name , "w+")
                            f.close()
                        
                            
                        k = k+1 
                        #print("nr de valori==>>",k)
                    #print("RAW_VALUE")
                    vlength = data[1]
                    if vlength==2:
                        val = data[2]*256+data[3]
                        if val>=32768:
                            val=val-65536
                        #print("va==>>",val," ",str(val))
                        
                        file = open(file_name , "a", newline='')
                        writer = csv.writer(file)
                        writer.writerow([str(val)])
                        file.close()
                elif code==0x02 or code==b'\x02' or code==2:
                    print("POOR_SIGNAL ",code)
                   
                    with open(file_name, "r", newline='') as file:
                        lines=file.readlines()
                        for line in lines:
                            line=str(line).replace('"', '')
                        #print(lines)
                    
                    with open(file_name, "w+") as file:   
                        lines=lines[:-1]
                        writer = csv.writer(file,quotechar = " ")
                        for line in lines:
                            #l=str(line).replace('"', '')
                            #print("line==>>",line)
                            l=str(line).replace('"', '')   
                            #print("line noua==>>",l)
                            writer.writerow([str(l)])
                    #file.close()
                   
                    
                elif code==0x83 or code==b'\x83' or code==131:
                    print("EEG_power",code)
                    vlength = data[1]
                    
                    if vlength==24:
                        delta = data[2]*65536+data[3]*256+data[4]
                        teta = data[5]*65536+data[6]*256+data[6]
                        alphalow = data[7]*65536+data[8]*256+data[9]
                        alphahigh = data[10]*65536+data[11]*256+data[12]
                        betalow = data[13]*65536+data[14]*256+data[15]
                        betahigh = data[16]*65536+data[17]*256+data[18]
                        gamalow = data[19]*65536+data[20]*256+data[21]
                        gamahigh = data[22]*65536+data[23]*256+data[24]
                        print("delta==>>",delta)
                        
                else:
                    print("unknown code",code)
    #else:
       # x1 = ser.read(1)
       # print("x1==>>",x1)
        