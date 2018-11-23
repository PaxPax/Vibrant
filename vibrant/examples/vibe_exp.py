import sys
sys.path.append('../')
from vibrant import *

#If you check out the raw ascii example there was a lot of typing for little gain
#because you had to keep track of reset will when using vibe, it'll take care of it for you
#here's an example how to print the color cyan
print(cyan("This will be cyan"))
#As you can see it's a lot simpler than typing cyan + "this will be cyan" + reset
#Also, it's a lot cleanr so you don't get hung up on unnessceary distractions.
#If you wanted the text to be bold and as as a color then that's simple as well
print(bold(cyan("This will be bold and cyan")))
#As long as you understand how you want it to look, you can chain method calls
print(underline(bold(green("Hello!"))))
#A quick tip is to have your text color in the inner most method call and expand outward
#Vibrant also has some easy to use built in symbols that may come in handy for your usage
print(error("This is a error!"))
#If you want the whole text to have the error code that's trivial as well
print(error("This is a full colored error!",True))
#Now what if you wanted the error color to be a different color?
#You might expect the ability to do something like
#blue(error("This is a blue error")), but if you try it it actually doesn't work
#That's ok, because Vibrant does have a built in custom that will suit your need
# custom(fcolor, text, bcolor = bdefault, fmt = bdefault)
example_error = custom(fblue,"[-]")
example_error += " This is my error code"
print(example_error)
#And for a full error colored example
full_error_color = custom(fgreen, "[-] This will be my full colored error")
print(full_error_color)
#Hopefully this comas as a somewhat intuitive way of coloring text
#Vibrant is still a work in progress, but if you're use case is relativly simple
#then maybe Vibrant is the right use case for you