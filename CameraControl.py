import cv2


class Cam:
    def __init__(self, default_image_dir): #TODO add default dir if empty param
        self.cap = cv2.VideoCapture(2, cv2.CAP_V4L) # TODO add exception check
        self.default_image_dir = default_image_dir + "/testImage.png" # TODO replace it with os lib operation

    def __del__(self):
        del(self.cap)
        
    def getPhoto(self, image_dir_=None):
        _, image = self.cap.read()
        if image_dir_ is None: # TODO check dir existence
            image_dir = self.default_image_dir
        else:
            image_dir = image_dir_ + "/testImage.png" # TODO replace it with os lib operation
        cv2.imwrite(image_dir, image)
        return image_dir
