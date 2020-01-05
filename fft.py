import numpy as np
from scipy import fftpack
import matplotlib.pylab as pl
import numpy.fft as fft
import time
import os

# 1:bci  2:sin  3:damped
mode = 1

def nr_inregistrari(file_name):
    #empty = False
    if os.path.isfile(file_name) ==False:
        return 0
    f = open(file_name)
    numline = len(f.readlines())
    #x`data = np.loadtxt(file)
    #if data.size == 0:
      #  empty = True
    #print (numline)
    return numline
    
def plot_fft(file_name):  
    file = file_name
    nr  = nr_inregistrari(file_name)    
    if nr>0: 
        #print("starting...")
        data = np.loadtxt(file)
        data1y = data   #[0:4000]
        timestep = 0.001953125
        data1x = np.arange(len(data1y))
        #print(len(data1y))
        data = data1y
        datax = data1x
        datay = data1y

    ## http://prancer.physics.louisville.edu/astrowiki/index.php/NumPy,_SciPy_and_SciKits#Fourier_Transforms_in_NumPy
    #
    # Use an FFT to calculate its spectrum
    spectrum = abs(np.fft.fft(data))
    # Find the positive frequencies
    frequency = np.fft.fftfreq( spectrum.size, d = timestep )
    index = np.where(frequency >= 0.)
    # Scale the real part of the FFT and clip the data
    clipped_spectrum = timestep*spectrum[index].real
    clipped_frequency = frequency[index]
    #
    ##

    x = clipped_frequency
    y = clipped_spectrum


    fig = pl.figure()
    fig.subplots_adjust(hspace=0.5)

    pl1 = fig.add_subplot(2,1,1)
    pl1.plot(datax,datay)

    pl2 = fig.add_subplot(2,1,2)
    pl2.plot(x,y)
    pl.xlabel('Frequency [Hz]')
    pl.ylabel('power')
    pl.xlim(0.,20.)
    
    pl.show()
    
   
#plot_fft(file_name)