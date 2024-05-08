## cartzy
```

import os
import csv
from PIL import Image, ImageDraw

csv_file = ("/home/ashritha-dasoju/Downloads/7622202030987_bounding_box.csv")
image_dir = ("/home/ashritha-dasoju/Downloads/7622202030987")
output_dir = ("/home/ashritha-dasoju/Downloads/7622202030987_with_boxes")

os.makedirs(output_dir, exist_ok=True)

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


with open(csv_file, 'r') as file:
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
```

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



## task
```

num = list(range(10))
previousNum = 0
for i in num:
    sum = previousNum + i
    print('Current Number '+ str(i) + 'Previous Number' + str(previousNum) + 'is ' + str(sum))
    previousNum=i
```

## video
```

# import the opencv library 
import cv2 


# define a video capture object 
vid = cv2.VideoCapture(0) 

while(True): 
	
	# Capture the video frame 
	# by frame 
	ret, frame = vid.read() 

	# Display the resulting frame 
	cv2.imshow('frame', frame) 
	
	# the 'q' button is set as the 
	# quitting button you may use any 
	# desired button of your choice 
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows()
```
