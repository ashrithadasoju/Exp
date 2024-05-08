## bounding box

In this The bounding box is a made-up square that serves as a guideline point for object recognition and creates a collision box for that element. Data annotators create these rectangles over pictures, defining the X, Y item coordinates of interest inside each image.

## uses of bounding box

1.Bounding boxes are used to label data for computer vision tasks

2.Object Detection

3.allowing machine learning models to identify and localize objects within an image.

## Example program for bounding boxes

1.import the libraries:The import keyword lets you import entire libraries or specific library functions into your code.

import os

import csv

from PIL import Image, ImageDraw

2.Reading the file:A CSV (Comma Separated Values) file is a form of plain text document that uses a particular format to organize tabular information.

csv_file = ("/home/ashritha-dasoju/Downloads/7622202030987_bounding_box.csv")

image_dir = ("/home/ashritha-dasoju/Downloads/7622202030987")

output_dir = ("/home/ashritha-dasoju/Downloads/7622202030987_with_boxes")

os.makedirs(output_dir, exist_ok=True)

3.Defines two functions:

draw_boxes(image, boxes): This function takes an image and a list of bounding boxes as input and draws rectangles around the bounding boxes on the image using the ImageDraw module

crop_image(image, boxes): This function takes an image and a list of bounding boxes as input and crops the image according to the bounding box coordinates, returning a list of cropped images.

def draw_boxes(image, boxes):

    draw = ImageDraw.Draw(image)
    
    for box in boxes:
    
        left = int(box['left'])
	
        top = int(box['top'])
	
        right = int(box['right'])
	
        bottom = int(box['bottom'])
	
        draw.rectangle([left, top, right, bottom], outline="red")
	
    return image


def crop_image(image, boxes):

    cropped_images = []
    
    for box in boxes:
    
        left = int(box['left'])
	
        top = int(box['top'])
	
        right = int(box['right'])
	
        bottom = int(box['bottom'])
	
        cropped_img = image.crop((left, top, right, bottom))
	
        cropped_images.append(cropped_img)
	
    return cropped_images
    
4.Opens the CSV file using a context manager (with open(csv_file, 'r') as file) and reads its contents using csv.DictReader, which reads each row of the CSV file as a dictionary where column headers are keys.

with open(csv_file, 'r') as file:

5.Iterates over each row in the CSV file. For each row:

    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
    
        image_name = row['filename']
	
        image_path = os.path.join(image_dir, image_name)
	
        output_path = os.path.join(output_dir, image_name)
	
        image = Image.open(image_path)
	
        boxes = [{'left': row['xmin'], 'top': row['ymin'], 'right': row['xmax'], 'bottom': row['ymax']}]
	
        cropped_images = crop_image(image, boxes)
	
        for i, cropped_img in enumerate(cropped_images):
	
            cropped_img.save(os.path.join(output_dir, f"{i}_{image_name}"))
	    
        full_image_with_boxes = draw_boxes(image, boxes)
	
        full_image_with_boxes.save(os.path.join(output_dir, f"full_{image_name}"))
	
## input

 ![7622202030987_f306535d741c9148dc458acbbc887243_L_487](https://github.com/ashrithadasoju/Exp/assets/169047414/d27f00f4-5fae-4b44-a281-f7d5c628bae6)


## output 1


![full_7622202030987_f306535d741c9148dc458acbbc887243_L_487](https://github.com/ashrithadasoju/Exp/assets/169047414/f02bd02f-19b6-43c9-9952-beffe612e07d)

## output 2

![0_7622202030987_f306535d741c9148dc458acbbc887243_L_519](https://github.com/ashrithadasoju/Exp/assets/169047414/4f885f1e-ac4a-40fd-b446-6bddc80f26e2)


## histogram
A histogram is a chart that plots the distribution of a numeric variable's values as a series of bars

## uses of histogram

1.An histogram image is a graphical representation of the distribution of pixel intensities in an image.

2. It helps you understand the brightness, contrast, and overall tonal range of an image.

3. It's useful for image processing, editing, and analyzing the characteristics of an image.

## Example program of histogram

1.importing the libraries:The import keyword lets you import entire libraries or specific library functions into your code.

import numpy as np

import cv2 as cv

from matplotlib import pyplot as plt

2.Reading the image:function is used to read an image from the specified path
 
img = cv.imread('/home/ashritha-dasoju/Desktop/my_folder/tom_jerry.jpg')

3.Saving the Image:function is used to save the read image (img) to a file path 

cv.imwrite("/home/ashritha-dasoju/Desktop/tom.jpg",img)

4.Error Handling:An assert statement is used to ensure that the image (img) is not None, i.e., the image has been successfully read. If the condition evaluates to False, it raises an assertion error with the message

assert img is not None, "file could not be read, check with os.path.exists()"

5.Calculating and Plotting Histogram:

color = ('b','g','r')

for i,col in enumerate(color):

 histr = cv.calcHist([img],[i],None,[256],[0,256])
 
 plt.plot(histr,color = col)
 
 plt.xlim([0,256])

 plt.show()

 ## Input

![tom](https://github.com/ashrithadasoju/Exp/assets/169047414/4bcb3bce-30cb-4a57-851e-0b4d24d32c33)

## output

![Figure_1](https://github.com/ashrithadasoju/Exp/assets/169047414/87ec0753-faa6-43ac-abf3-04b11b78f088)

## Iterating the first 10 numbers

This code initializes a list num containing numbers from 0 to 9. Then, it iterates through each element in num using a for loop. Within each iteration

1.It calculates the sum of the current number i and the previousNum.

num = list(range(10))

previousNum = 0

for i in num:

    sum = previousNum + i

2.Print a message indicating the current number, the previous number, and the sum.

    print('Current Number '+ str(i) + 'Previous Number' + str(previousNum) + 'is ' + str(sum))
    
3.Update the previousNum variable to the current number i.
    
    previousNum=i

## output

Current Number 0Previous Number0is 0

Current Number 1Previous Number0is 1

Current Number 2Previous Number1is 3

Current Number 3Previous Number2is 5

Current Number 4Previous Number3is 7

Current Number 5Previous Number4is 9

Current Number 6Previous Number5is 11

Current Number 7Previous Number6is 13

Current Number 8Previous Number7is 15

Current Number 9Previous Number8is 17


## Webcam

1.Import the OpenCV library:

import cv2 

2.Define a video capture object (vid) by calling cv2.VideoCapture(0)

vid = cv2.VideoCapture(0)

3.Start an infinite loop (while(True)) to continuously capture frames from the video:

while(True): 
	
4.the function vid.read() captures a frame from the video and returns two values: ret, a boolean indicating whether a frame was successfully captured, and frame, the captured frame.
 
	ret, frame = vid.read() 


 5.cv2.imshow('frame', frame) displays the captured frame in a window named 'frame'.
 
	cv2.imshow('frame', frame) 
	
6.The loop waits for a key press with cv2.waitKey(1). If the pressed key is 'q', the loop breaks and the program ends.
 
	if cv2.waitKey(1) & 0xFF == ord('q'):
 
		break
  
7.vid.release() releases the video capture object, freeing the camera resources.

vid.release()

8.cv2.destroyAllWindows() closes all OpenCV windows.


cv2.destroyAllWindows()

## output



