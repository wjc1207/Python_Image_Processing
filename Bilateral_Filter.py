import numpy as np

signal = np.zeros(100)
signal = np.append(signal, np.ones(100)*30)

# Add noise
noise = np.random.normal(0, 3, 200)
signal = signal + noise

origin_signal = signal

# Apply the Bilateral Filter
filtered = np.zeros(200)
for iter in range(40):
    for i in range(200):
        w_sum = 0
        for j in range(i-1, i+2):
            if j >= 0 and j < 200:
                a = (j-i)**2/100
                b = (signal[i]-signal[j])**2/100
                w = np.exp(-a-b)
                filtered[i] += w * signal[j]
                w_sum += w
            
        filtered[i] /= w_sum
    
    signal = filtered
    filtered = np.zeros(200)

# Display the results
import matplotlib.pyplot as plt
plt.plot(origin_signal)
plt.plot(signal)
plt.show()
