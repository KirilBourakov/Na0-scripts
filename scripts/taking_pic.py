from naoqi import ALProxy
import cv2
import numpy as np
video_device = ALProxy("ALVideoDevice", "192.168.2.251", 9559)

id = video_device.subscribeCamera("python_GVM", 0, 2, 11, 30)

image_data = video_device.getImageRemote(id)

video_device.unsubscribe(id)

# Process the image data
image_width = image_data[0]
image_height = image_data[1]
image_array = image_data[6]

image = np.frombuffer(image_array, dtype=np.uint8).reshape(image_height, image_width, 3)

cv2.imwrite("C:\\Users\\alexb\\Desktop\\na0\\img.png", image)
