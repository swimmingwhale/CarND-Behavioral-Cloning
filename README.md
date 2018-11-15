# **Behavioral Cloning** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* train.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup_report.md or writeup_report.pdf summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable

The train.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

My model consists of a convolution neural network with 3x3 5x5 filter sizes and depths between 24 and 64 (train.py lines 5-25)

The model includes RELU layers to introduce nonlinearity (code line 8,10,12,14,16,19,21,23), and the data is normalized in the model using a Keras lambda layer (code line 6).

#### 2. Attempts to reduce overfitting in the model

The model contains dropout layers in order to reduce overfitting (train.py lines 20,22,24).

The model was trained and validated on different data sets to ensure that the model was not overfitting (code line 28-34). The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (train.py line 27).

#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I keep driving car in the center of the lane and format one circle data.

For details about how I created the training data, see the next section. 

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

The overall strategy for deriving a model architecture was to do more experiments to see which results are optimal.

My first step was to use a convolution neural network model similar to the LeNet I thought this model might be appropriate because this model very popular.

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. I found that my first model had a low mean squared error on the training set but a high mean squared error on the validation set. This implied that the model was overfitting. 

To combat the overfitting, I modified the model so that I add some drop layers.

Then I print lost line charts to see verification loss and training loss.

The final step was to run the simulator to see how well the car was driving around track one. There were a few spots where the vehicle fell off the track was the first corner,bridgehead and the second corner to improve the driving behavior in these cases, I multiple test models and increase training data.At most, even 10 laps of training data were used.But the effect is still not ideal,finally I find cv2.imread() return data in a BGR format,I convert BGR format to RGB format and try again,it's amazing,just use one lap of data to run perfectly.

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The final model architecture (train.py lines 5-25) consisted of a convolution neural network with the following layers and layer sizes.First,three 5x5 convolution layers and two 3x3 convolution layersm,next, a flatten layer and three full connect layers.

#### 3. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded two laps on track one using center lane driving. Here is an example image of center lane driving:

![alt text](examples/1.jpg)

I then recorded the vehicle recovering from the left side and right sides of the road back to center so that the vehicle would learn to from the left side and right sides of the road back to center These images show what a recovery looks like starting from right sides back to center:

![alt text](examples/2.jpg)
![alt text](examples/3.jpg)

Then I repeated this process on track two in order to get more data points.

To augment the data sat, I also flipped images and angles thinking that this would balance the weight of the left turn and right turn. For example, here is an image that has then been flipped:

![alt text](examples/flip1.jpg)
![alt text](examples/flip2.jpg)


After the collection process, I had X number of data points. I then preprocessed this data by ...


I finally randomly shuffled the data set and put 20% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was 5 as evidenced by visualizing loss line charts I used an adam optimizer so that manually training the learning rate wasn't necessary.

![alt text](examples/Figure_1.png)