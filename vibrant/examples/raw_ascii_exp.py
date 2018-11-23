import sys
sys.path.append('../')
from vibrant import *
#If you just want the ascii escape sequences and symbols you just have
#to import from ascii_seq and either pick what you need or import everything
#In this example we are importing everything but you can do something like
#from ascii_seq import fblue and just be able to use the blue font color
print(fblue + "this text will be blue" + reset_)
#As you see I've concated an addition sign with the word reset to the end of the string
#This is to change the text color back to default otherwise all of our text color would be blue
#So you if you don't want it to go back to default omit the reset_

print(fblue + "This will be blue")
print("This will be blue as well")
#The good thing is we can reset the color whenever we want just by printing the raw reset_
print(reset_,end="")
print("this is the default color of your terminal")

#Now what if we want to do styles with colors?
#First we want the style first then the color we want to apply
#make sure to add the reset when you want it to end
print(underline_ + forange + "This text will be orange and underline" + reset_)
#While raq sequences are helpful when you want absolute control over how it looks,
#most of the time I don't believe it's needed.

#Here's a fun function to print out zebra pattern
#While it is basic feel free to expand on it

def zebra(text):
    index = 0
    new_zebra_text = ""
    for char in text:
        if index % 2 == 0:
            new_zebra_text += bblack + char + bdefault
        else:
            new_zebra_text += char
        index += 1
    return new_zebra_text

print(zebra("This is some text"))