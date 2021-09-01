import os
import PIL
import cv2
from PIL import Image

folder_location = "C:\\Users\\Admin\\Intern_Images\\Apr-512-clahe"
# Give your folder location to var folder_location
return_list = []

for filenames in os.walk(folder_location):
    for file_list in filenames:
        for file_name in file_list:
            if file_name.endswith((".jpg")):
                fp = filenames[0] + "\\" + file_name
                print(fp)
                image = cv2.imread(fp)
                lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

                lab_planes = cv2.split(lab)

                clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

                lab_planes[0] = clahe.apply(lab_planes[0])

                lab = cv2.merge(lab_planes)

                bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
                cv2.imwrite(fp, bgr)

                img = Image.open(fp)
                img = img.resize((512, 512))
                img.save(fp)

                return_list.append(fp)

print(len(return_list))