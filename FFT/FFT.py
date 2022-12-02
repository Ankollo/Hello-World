import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft

x = np.linspace(0, 2*np.pi, 200) # 采样频率为 200Hz
y = np.cos(5*x) + 0.5*np.sin(25*x) + 0.3*np.cos(75*x) # 根据采样定理，信号中不能包含超过 100Hz 的频率成分

plt.figure(figsize=(10,12))
ax1 = plt.subplot(311)
ax1.plot(x, y, 'r')
ax1.set_title('123original signal in time domain')

Y = fft(y) # 快速傅里叶变换，得到频域
ax2 = plt.subplot(323)
ax2.plot(range(200), abs(Y))
ax2.set_title('original signal in frequency domain')

Y[10:-9] = 0 # 滤波  将第10个数到倒数第9个数之间的数全部置零
ax3 = plt.subplot(324)
ax3.plot(range(200), abs(Y))
ax3.set_title('filtered signal in frequency domain')

filtered = ifft(Y).real # 逆变换，得到滤波后的时域信号
ax4 = plt.subplot(313)
ax4.plot(x, filtered, 'g')
ax4.set_title('filtered signal in time domain')


plt.show()
