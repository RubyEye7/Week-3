from PIL import Image
from PIL import ImageFilter
import wx

class Photoediter(wx.Frame)
      self.button6 = Button(self, bg = "#98DBC6", bd = 12,
        text = "Posterize",  padx = 33, pady = 25,
        command = lambda : self.buttonClick(6), font = ("Comic Sans", 20, "bold"))
        self.button6.grid(row = 3, column = 2, sticky = W)





"""
def posterizer(c):
    if c >= 0 and c <= 63:
        return 50
    elif c >= 64 and c <= 127:
        return 100
    elif c >= 128 and c <= 191:
        return 150
    elif c >= 192 and c <= 255:
        return 200

def solarizer(n):
    if n < 128:
        return 255 - n
    else:
        return n

def remove_red(name):
    img = Image.open(name)
    pixels = [(0,b,g) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("not_red_" + name)

def invert_color():
    img = Image.open(name)
    pixels = [(255-r,255-g,255-b) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("inverted_" + name)

def darken_color(name):
    img = Image.open(name)
    pixels = [(int(0.75 * r),int(0.75 * g),int(0.75 * b)) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("darkened_" + name)

def lighten_color(name):
    img = Image.open(name)
    pixels = [(int(1.25 * r),int(1.25 * g),int(1.25 * b)) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("lightened_" + name)

def greyscale(name):
    img = Image.open(name)
    pixels = [(int((r+g+b)/3),int((r+g+b)/3),int((r+g+b)/3)) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("grey_" + name)

def posterize(name):
    img = Image.open(name)
    pixels = [(posterizer(r),posterizer(g),posterizer(b)) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("posterized_" + name)

def solarize(name):
    img = Image.open(name)
    pixels = [(solarizer(r),solarizer(g),solarizer(b)) for (r,g,b) in img.getdata()]
    img.putdata(pixels)
    img.save("solarized_" + name)

def crop(name):
    start_x = int(input("Enter starting x value:  "))
    start_y = int(input("Enter starting y value:  "))
    end_x = int(input("Enter ending x value:  "))
    end_y = int(input("Enter ending y value:  "))
    img = Image.open(name)
    area = (start_x, start_y, end_x, end_y)
    cropped_img = img.crop(area)
    cropped_img.save("cropped_" + name)

def flip_horizontal(name):
    img = Image.open(name)
    flip_image_h = img.transpose(Image.FLIP_LEFT_RIGHT)
    flip_image_h.save("horizontal_flipped_" + name)

def flip_vertical(name):
    img = Image.open(name)
    flip_image_h = img.transpose(Image.FLIP_TOP_BOTTOM)
    flip_image_h.save("vertical_flipped_" + name)


def blur(name):
    blur_radius = int(input("Enter blur radius:  "))
    original_image = Image.open(name)
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=blur_radius))
    blurred_image.save("blurred_" + name)

def sharpen(name):
    sharpen_radius = int(input("Enter sharpen radius(1.0 - 3.0):  "))
    sharpen_percent = int(input("Enter sharpen percentage(100 - 300):  "))
    sharpen_threshold = int(input("Enter sharpening threshold(3 - 5):  "))
    sharper_image = Image.open(name)
    sharper_image = sharper_image.filter(ImageFilter.UnsharpMask(radius = sharpen_radius, percent = sharpen_percent, threshold = sharpen_threshold))
    sharper_image.save("sharpened_" + name)
"""
