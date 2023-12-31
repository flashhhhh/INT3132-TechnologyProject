import numpy as np
import matplotlib.pyplot as plt
import sys

argv = sys.argv[1]
#masterColor = ['', 'red', 'orange', 'violet', 'pink', 'purple']
masterColor = ['', 'red', 'orange', 'red', 'red', 'red']
#mpiColor = ['', 'blue', 'green', 'black', 'brown', 'gray']
mpiColor = ['', 'blue', 'purple', 'blue', 'blue', 'blue']

hoangColor = ['', 'green', 'lightgreen', 'green', 'green', 'green']

plt.figure(figsize=(24, 13.5))
numData = 2

for suffix in range(1, numData + 1):
    with open("master/" + argv + "/" + argv + "_" + str(suffix) + ".data") as f:
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
        plt.plot(X, y, color=masterColor[suffix], label="master " + str(suffix))

for suffix in range(1, numData + 1):
    with open("minhmpi/" + argv + '/' + argv + '_' + str(suffix) + '.data') as f:
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
        plt.plot(X, y, color=mpiColor[suffix], label="minhmpi " + str(suffix))

for suffix in range(1, numData + 1):
    with open("hoangmpi/" + argv + '/' + argv + '_' + str(suffix) + '.data') as f:
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
        plt.plot(X, y, color=hoangColor[suffix], label="hoangmpi " + str(suffix))

plt.legend()
plt.savefig("graph/" + argv + ".png")
# plt.show()

"""
Command is:
    python3 iqtree.py <name of file>
    
For example:
    python3 iqtree.py M7929
"""