import serial
import datetime
import codecs
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import style


style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):

    start = datetime.datetime.now()
    tmp_current1 = datetime.datetime.now()
    xs = []
    ys = []

    try:
        '''
        ser = serial.Serial(
          port="COM3",
          baudrate=57600,
          bytesize=serial.EIGHTBITS,
          parity=serial.PARITY_ODD,
          stopbits=serial.STOPBITS_TWO
      )'''
        ser = serial.Serial('COM9',57600,timeout=.1)
        ser.isOpen() # try to open port, if possible print message and proceed with 'while True:'
        print ("port is opened!")

    except IOError: # if port is already opened, close it and open it again and print message
        ser.close()
        ser.open()
        print ("port was already open, was closed and opened again!")
        line = ser.readline();
        #line = line.decode("utf-8") #ser.readline returns a binary, convert to string
        print(line)
    while (tmp_current1 - start).total_seconds() < 5:
        tmp_current1 = datetime.datetime.now()
        #print(k)
        line = ser.readline();
        print("byte stream...",line)
        for i in range(len(line)):
            if line[i]==170 and line[i+1]==170:
                for j in range(i+4,line[i+3]):
                    file = open("date3.txt", "a")
                    if line[j]!=2:
                        print(line[j])  
                        file.write(str(line[j]))
                        file.write("\n")
                        tmp_current = datetime.datetime.now()
                        xs.append((tmp_current - start).total_seconds())
                        ys.append(line[j])
                    file.close()
                ax1.clear()
                ax1.plot(xs,ys)                    
                    
    #print("byte to int....",type(list(line)),list(line))
    #print(list(line))
    
    
    
	#writeFile.close()
#pip install pyserial


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()