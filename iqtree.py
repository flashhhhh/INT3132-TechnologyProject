import numpy as np
import matplotlib.pyplot as plt
import sys

argv1 = sys.argv[1]
argv2 = sys.argv[2]

# Load data
with open(argv1) as f:
    data = f.readlines()
    data = [x.strip() for x in data]

    for i in range (0, len(data)):
        data[i] = data[i].split()
    
    data = np.array(data)
    data[:, 0] = data[:, 0].astype(int)
    data[:, 1] = data[:, 1].astype(float)
    
    X = int(data[0, 0])
    y = float(data[0, 1])

    for i in range(1, len(data)):
        X = np.append(X, int(data[i, 0]) - 1)
        y = np.append(y, float(data[i - 1, 1]))
        
        X = np.append(X, int(data[i, 0]))
        y = np.append(y, float(data[i, 1]))

    # Plot data
    plt.plot(X, y, color='red')


with open(argv2) as f:
    data = f.readlines()
    data = [x.strip() for x in data]

    for i in range (0, len(data)):
        data[i] = data[i].split()
    
    data = np.array(data)
    data[:, 0] = data[:, 0].astype(int)
    data[:, 1] = data[:, 1].astype(float)
    
    X = int(data[0, 0])
    y = float(data[0, 1])

    for i in range(1, len(data)):
        X = np.append(X, int(data[i, 0]) - 1)
        y = np.append(y, float(data[i - 1, 1]))
        
        X = np.append(X, int(data[i, 0]))
        y = np.append(y, float(data[i, 1]))

    # Plot data
    plt.plot(X, y, color='blue')

plt.show()