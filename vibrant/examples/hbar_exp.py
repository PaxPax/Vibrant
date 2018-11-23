import sys
sys.path.append('../')
from vibechart import *

#while still a work in progress it is useable for simple data
#the hbar method expects a dictionary of numeric non negative values
#you can also specify the x label and title. Also, you choose which symbol
#you would like to represent your data, the default is a █
values = {'pigs': 32, 'cows': 54, 'chicken': 44, 'fish': 10}
person_hbar = HBarChart()
person_hbar.hbar(values,"Animals Eaten Per American", "domestic animals")

#if you want to change the color of the bar chart, it's a simple matter
changed_hbar = HBarChart(flred)
changed_hbar.hbar(values, "Animals Eaten Per American","domestic animals")
#Note that adding the reset_ in the constructor is not needed

#now if you wanted change the color of the title or label is just as easy
#there are two ways to do it, you can either import vibrant use use the build in helper
#font color functions or you can use ascii_seq
another_hbar = HBarChart(fblue)
another_hbar.hbar(values, forange + "Animals Eaten Per American" + reset_, flred + "domestic animals" + reset_)
#While it doesn't look pretty, it does work and that's what matters
#Here's the other version where we use the imported methods from vibrant
from vibrant import *
last_hbar = HBarChart(fgreen)
last_hbar.hbar(values,orange("Animals Etern Per American"), "domestic animals")