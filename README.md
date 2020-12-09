image_to_c
----------

A command line tool for turning binary image files into C source code. The output is an array of unsigned chars and is sent to stdout. Included are comments detailing the image type, size and other details.<br>
<br>

### **What's the diffrent from master branch?**
It's rebuild with python.

### **HOW TO USE**
~~~bash
$ python3 convey.py [path_to_your_image]
~~~

### **NOTICE**
> if you input an video stream, the output will only show The first image  

> to develop more in/out types, you can add more `if` branch below
~~~python
for j in range(y):
        if array_format == "uint16_t":
            if color_format == "rgb565":
                res = (img[i][j][0]) * (2**8) + img[i][j][1]
                file.write('%#x'%res+",")
        elif array_format == "uint8_t":
            if color_format == "rgb565":
                file.write('%#x'%img[i][j][1]+",")
                file.write('%#x'%img[i][j][0]+",")
~~~

<b>What does the output look like?</b><br>
Here's an example of a before and after of what this new tool does:<br>

It turns this type of file:<br>
![Animated GIF](/badger.gif?raw=true "Animated GIF")

Into this type of file:<br>
![screenshot](/screenshot.png?raw=true "screenshot")

<b>What image file types does it support?</b><br>

PNG, JPEG, BMP, TIFF, GIF, PPM, TARGA, JEDMICS, CALS and PCX<br>

<b>What happens for unrecognized files?</b><br>
If the file type is not known, it will generate the same C output, but without additionl info.<br>

If you find this code useful, please consider sending a donation or becoming a Github sponsor.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=SR4F44J2UR8S4)

