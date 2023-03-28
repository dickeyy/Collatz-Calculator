import matplotlib.pyplot as plt
import numpy as np
import json

dictionary = json.load(open('RGPoints.json', 'r'))
x = [key for key, value in dictionary.items()]
y = [value for key, value in dictionary.items()]

plt.xlabel('Number tested')
plt.ylabel('Numbers until loop')
plt.title('Runs Correlation')
plt.plot(x,y)
plt.show()