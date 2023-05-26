from CameraControl import Cam
import cv2


# cam = Cam("/home/orangepi/PythonProjects/test")
cam = Cam("D:\PycharmProjects\GarbageClassifier_OPi")
cam.getPhoto()
_, image = cap.read()
cv2.imwrite(image_dir, image)

