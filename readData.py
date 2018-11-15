import csv
import cv2
import numpy as np

samples = []
with open('./driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        samples.append(line)

from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

train_samples, validation_samples = train_test_split(samples, test_size=0.2)


def generator(samples, batch_size=32):
    num_samples = len(samples)
    while 1:
        shuffle(samples)
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset + batch_size]
            correction = 0.2
            images = []
            angles = []
            for batch_sample in batch_samples:
                img_center_bgr = cv2.imread('IMG/' + batch_sample[0])
                img_left_bgr = cv2.imread('IMG/' + batch_sample[1])
                img_right_bgr = cv2.imread('IMG/' + batch_sample[2])

                img_center = cv2.cvtColor(img_center_bgr,cv2.COLOR_BGR2RGB)
                img_left = cv2.cvtColor(img_left_bgr,cv2.COLOR_BGR2RGB)
                img_right = cv2.cvtColor(img_right_bgr,cv2.COLOR_BGR2RGB)

                angle_center = float(batch_sample[3])
                angle_left = angle_center + correction
                angle_right = angle_center - correction

                images.extend([img_center, img_left, img_right])
                angles.extend([angle_center, angle_left, angle_right])

                images.extend([cv2.flip(img_center, 1), cv2.flip(img_left, 1), cv2.flip(img_right, 1)])
                angles.extend([angle_center * -1.0, angle_left * -1.0, angle_right * -1.0])

            X_train = np.array(images)
            y_train = np.array(angles)
            yield shuffle(X_train, y_train)


train_generator = generator(train_samples, batch_size=32)
validation_generator = generator(validation_samples, batch_size=32)
