# from PIL import Image, ImageFilter,ImageEnhance
import cv2
import numpy as np
from pyzbar.pyzbar import decode,ZBarSymbol
# from PIL.ImageFilter import (
#    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
#    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
# )

# def cv2_to_pil(img): #Since you want to be able to use Pillow (PIL)
#     return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# def pil_to_cv2(img):
#     return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

vid = cv2.VideoCapture(0) #Define the camera, 0 is which camera, if you have more than 1

while True:
    ret_val, frame = vid.read() #cam.read() returns ret (0/1 if the camera is working) and img, 
    #the actual image of the camera in a numpy array

    cv2.imshow('frame', frame)

    # pil_img = cv2_to_pil(frame) #convert the image to PIL so you can use it that way.

    # img = pil_img.filter(EDGE_ENHANCE_MORE)
    decoded_list = decode(frame) 

    # print(type(decoded_list))
    # # <class 'list'>

    # print(len(decoded_list))

    if len(decoded_list) == 0:
        # print("No code found or could not read")
        pass

    else:
        with open("data.txt", 'a') as file:
            for item in decoded_list:
                print(item)
                file.write(f"{item.data.decode('utf-8')}\n")

    if cv2.waitKey(1) & 0xFF == ord('q'): #the q button is the quit button upon pressing which the loop will break
        break


vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
