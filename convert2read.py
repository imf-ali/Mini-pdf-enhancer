# import module
from pdf2image import convert_from_path
from fpdf import FPDF
import cv2
import os

# Store Pdf with convert_from_path function
images = convert_from_path('Head_neck_face.pdf')

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('f/page'+ str(i) +'.jpg', 'JPEG')
	img = cv2.imread('f/page'+ str(i) +'.jpg', cv2.IMREAD_UNCHANGED)

	image_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	adaptive = cv2.adaptiveThreshold(image_grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 5)
	# thresh, image_black = cv2.threshold(image_grayscale, 180, 255, cv2.THRESH_BINARY)
	cv2.imwrite('f/page'+ str(i) +'.jpg', adaptive)


pdf = FPDF()
img_list = [x for x in os.listdir("f")]

for img in img_list:
	pdf.add_page()
	image = "f/" + img
	pdf.image(image,w=175,h=260)

pdf.output("out/Head_neck_face.pdf")
