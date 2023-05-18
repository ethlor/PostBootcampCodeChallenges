import struct
from io import SEEK_CUR

def reading():
    bmp = open("FLAG_B242.BMP", 'rb+')

    filesize = readInt(bmp,2)
    start = readInt(bmp, 10)
    width = readInt(bmp, 18)
    height = readInt(bmp, 22)

    scanlineSize = width * 3
    if scanlineSize % 4 == 0:
        padding = 0
    else :
        padding = 4 - scanlineSize % 4


    bmp.seek(start)# Process the individual pixels.
    for row in range(height): #For each scan line
        for col in range(width): #For each pixel in the line
            processPixel(bmp)
        
        bmp.seek(padding, SEEK_CUR)


    bmp.close()



def processPixel(imgFile): #Read the pixel as individual bytes.
    theBytes = imgFile.read(3)
    blue = theBytes[0]
    green = theBytes[1]
    red = theBytes[2]

    # get new grayscale for picture
    gray = int((0.21 * red) + (0.72 * green) + (0.07* blue))

    # Process the pixel.
    newBlue = 255 - gray
    newGreen = 255 - gray
    newRed = 255 - gray

    # Write the pixel.
    imgFile.seek(-3, SEEK_CUR)# Go back 3 bytes to the start of the pixel.
    imgFile.write(bytearray([newBlue, newGreen, newRed]))

def readInt(imgFile, offset): #Move the file pointer to the given byte within the file.
    imgFile.seek(offset)

    # Read the 4 individual bytes and build an integer.
    theBytes = imgFile.read(4)
    result = 0
    base = 1
    for i in range(4):
        result = result + theBytes[i] * base
        base = base * 256

    return result# Start the program.

reading()

"""
check all the byte information of the image
bmp = open(imagefilename, 'rb+')
print('Type:', bmp.read(2).decode())
print('Size: %s' % struct.unpack('I', bmp.read(4))) 
print('Reserved 1: %s' % struct.unpack('H', bmp.read(2)))
print('Reserved 2: %s' % struct.unpack('H', bmp.read(2)))
print('Offset: %s' % struct.unpack('I', bmp.read(4)))

print('DIB Header Size: %s' % struct.unpack('I', bmp.read(4)))
print('Width: %s' % struct.unpack('I', bmp.read(4))) # 18
print('Height: %s' % struct.unpack('I', bmp.read(4))) # 22
print('Colour Planes: %s' % struct.unpack('H', bmp.read(2)))
print('Bits per Pixel: %s' % struct.unpack('H', bmp.read(2)))
print('Compression Method: %s' % struct.unpack('I', bmp.read(4)))
print('Raw Image Size: %s' % struct.unpack('I', bmp.read(4)))
print('Horizontal Resolution: %s' % struct.unpack('I', bmp.read(4)))
print('Vertical Resolution: %s' % struct.unpack('I', bmp.read(4)))
print('Number of Colours: %s' % struct.unpack('I', bmp.read(4)))
print('Important Colours: %s' % struct.unpack('I', bmp.read(4)))
bmp.close()
"""
