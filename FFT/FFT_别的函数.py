import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft

up = 128
#x = np.linspace(0, 2*np.pi, 200) # 采样频率为 200Hz
x = np.linspace(1, 128, 128)
#x = np.linspace(0, 3, 4)

#y = np.cos(5*x) + 0.5*np.sin(25*x) + 0.3*np.cos(75*x) # 根据采样定理，信号中不能包含超过 100Hz 的频率成分
y = 255*(np.sin(3.14*x*2/25)+np.sin(3.14*x*2*0.4))
#y = np.sin(3.14*x/2+3.14/4)

plt.figure(figsize=(10,12))
ax1 = plt.subplot(311)
ax1.plot(x, y, 'r')    #r 是红色
ax1.set_title('456original signal in time domain')

Y = fft(y) # 快速傅里叶变换，得到频域
ax2 = plt.subplot(323)
ax2.plot(x, abs(Y))
ax2.set_title('original signal in frequency domain')

Y[10:-9] = 0 # 滤波
ax3 = plt.subplot(324)
ax3.plot(x, abs(Y))
ax3.set_title('filtered signal in frequency domain')

filtered = ifft(Y).real # 逆变换，得到滤波后的时域信号
ax4 = plt.subplot(313)
ax4.plot(x, filtered, 'g')
ax4.set_title('filtered signal in time domain')

plt.show()