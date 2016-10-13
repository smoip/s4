from PIL import Image
import pytesseract
import os
import re
import random
import string
import base64
from IPython import embed

# Pre-reqs:
# brew install tesseract
# brew install imagemagick
# brew install ghostscript
# I think that's it

stuff = {
    "convert-opts" : [
        "-font", "Courier",
        "-size", "1920x1080",
        "xc:White",
        "-gravity", "Center",
        "-weight", "100",
        "-pointsize", "100",
        "-annotate", "0"
    ],
    "max-chars-per-line": 30,
    "target": "test.png"
}

base16_to_dumb16 = {
    "0": "G",
    "1": "H",
    "2": "J",
    "3": "K",
    "4": "L",
    "5": "M",
    "6": "N",
    "7": "P",
    "8": "Q",
    "9": "R",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F"
}

dumb16_to_base16 = dict((y,x) for x,y in base16_to_dumb16.iteritems())

def encode(message):
    return "".join([base16_to_dumb16[char] for char in base64.b16encode(message)])

def decode(message):
    return base64.b16decode("".join([dumb16_to_base16[char] for char in message]))

def frobulate(message):
    # Split the message
    line_length = stuff["max-chars-per-line"]
    split_message = "\n".join([message[i:i+line_length] for i in range(0, len(message), line_length)])

    # Create an image file from the text
    opts = stuff["convert-opts"]
    command = "convert " + " ".join(stuff["convert-opts"]) + " \"" + split_message + "\" " + stuff["target"]
    os.system(command)

    # Read the file
    read_message = pytesseract.image_to_string(Image.open(stuff["target"]))

    # Print and check consistency
    print(split_message)
    print(read_message)
    print(str(split_message == read_message))

def random_string(n):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(n))

frobulate(encode(random_string(180)))
