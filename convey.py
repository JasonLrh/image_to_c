from types import resolve_bases
import cv2 as cv
import sys

array_format = "uint16_t"
color_format = "rgb565"
single_array = False

file = open(r"out.c",'w')
img = cv.imread(sys.argv[1])
if img is None:
    cap = cv.VideoCapture(sys.argv[1])
    _,img = cap.read()
img=cv.cvtColor(img,cv.COLOR_BGR2BGR565)
print(img.shape)
x,y,deep=img.shape

if single_array is False:
    file.write(array_format+" out[]["+str(y)+"]=")
else:
    file.write(array_format+" out["+str(x*y)+"]=")
file.write("{\n")
for i in range(x):
    if single_array is False:
        file.write("{")
    for j in range(y):
        if array_format == "uint16_t":
            if color_format == "rgb565":
                res = (img[i][j][0]) * (2**8) + img[i][j][1]
                file.write('%#x'%res+",")
        elif array_format == "uint8_t":
            if color_format == "rgb565":
                file.write('%#x'%img[i][j][1]+",")
                file.write('%#x'%img[i][j][0]+",")
    if single_array is False:
        file.write("},\n")
file.write("}")