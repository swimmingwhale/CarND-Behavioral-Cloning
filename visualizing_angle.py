import matplotlib.pyplot as plt
import csv
import numpy as np

samples = []
with open('./driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        samples.append(line)

correction = 0.2
angles = []
for sample in samples:
    angle_center = float(sample[3])
    angle_left = angle_center + correction
    angle_right = angle_center - correction

    angles.extend([angle_center, angle_left, angle_right])

x,y = np.unique(angles,return_counts=True)

plt.bar(x, y, width= 0.005,facecolor='#9999ff', edgecolor='white')
plt.xlim(-0.75,+0.75)
plt.show()
