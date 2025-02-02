import cv2
import numpy as np

def pencil_sketch(image_path, output_path):
    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    inverted_gray_image = cv2.bitwise_not(gray_image)

    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

    inverted_blurred_image = cv2.bitwise_not(blurred_image)

    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    
    cv2.imwrite(output_path, pencil_sketch_image)

    cv2.imshow('Pencil Sketch', pencil_sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

input_image_path = r'C:\Users\xps\Pictures\WhatsApp Image 2024-08-16 at 08.38.23_2fc7db5c.jpg'
output_image_path = r'C:\Users\xps\Pictures\WhatsApp_Image_Sketch.jpg'
pencil_sketch(input_image_path, output_image_path)
