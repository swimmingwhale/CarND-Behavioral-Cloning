from readData import *
from keras.models import Sequential
from keras.layers import Dense, Flatten, Lambda,BatchNormalization,Conv2D, Cropping2D,MaxPooling2D,Dropout

model = Sequential()
model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape=(160, 320, 3)))
model.add(Cropping2D(cropping=((50, 20), (0, 0))))
model.add(Conv2D(24, (5, 5), strides=(2, 2), activation='relu'))
model.add(BatchNormalization())
model.add(Conv2D(36, (5, 5), strides=(2, 2), activation='relu'))
model.add(BatchNormalization())
model.add(Conv2D(48, (5, 5), strides=(2, 2), activation='relu'))
model.add(BatchNormalization())
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dropout(.2))
model.add(Dense(50, activation='relu'))
model.add(Dropout(.2))
model.add(Dense(10, activation='relu'))
model.add(Dropout(.2))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
history_object = model.fit_generator(
    train_generator,
    steps_per_epoch=int(len(train_samples)/32),
    validation_data=validation_generator,
    validation_steps=int(len(validation_samples)/32),
    epochs=5
)
model.save('model.h5')

import pickle

with open('history.pickle', 'wb') as f:
    pickle.dump(history_object.history, f, pickle.HIGHEST_PROTOCOL)
