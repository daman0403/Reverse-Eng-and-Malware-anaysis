
# Standard
import sys
import os
import math

# Third Party
from PIL import Image

# Original


def main(arg_values, arg_length):
    """Main routine"""

    if arg_length != 2:
        help(os.path.splitext(os.path.basename(sys.argv[0]))[0])
        return

    input_file_name = arg_values[1]
    input_file = open(input_file_name, "rb")
    input_data = bytearray(input_file.read())
    if len(input_data) == 0:
        print ("Empty file.")
        return

    IMAGE_WIDTH = 128
    image_size = (IMAGE_WIDTH,
        int(math.ceil(len(input_data) / (IMAGE_WIDTH * 1.0))))
    image = Image.new("RGB", image_size, "white")


    def convert_color(byte):
        """Decides a pixel color according to the rule of Stirling."""

        if   byte >= 0x80:
            return 0x000000
        elif byte >= 0x20:
            return 0x0000ff
        elif byte >= 0x01:
            return 0xffff00
        else:
            return 0xffffff


    def fill_image(input_data, image, image_size):
        """Puts color pixels on an image with color conversion"""

        y_range = range(image_size[1])
        x_range = range(IMAGE_WIDTH)
        d_range = len(input_data)
        pix = image.load()
        index = 0
        for y in y_range:
            for x in x_range:
                pix[x, y] = convert_color(input_data[index])
                index += 1
                if index >= d_range:
                    return
        return


    fill_image(input_data, image, image_size)
    image.convert("P").save(input_file_name + ".png", "PNG")
    return


if __name__ == "__main__":
    main(sys.argv, len(sys.argv))