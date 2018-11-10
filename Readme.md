# Vibrant

Vibrant was largely inspired by [fab](https://github.com/icyphox/fab). I enjoyed the idea of it being extremely simple and easy to use. While Vibrant is easy to use, it can be made even easier, which is my plan. So, feel free to use the current Vibrant if you wish, but it will be going through some changes to make the experience more enjoyable and extending the functionality. With the increase of functionality, you will always be able to use the core of Vibrant without having to worry about breaking changes.

## SHOWCASE![vibe](/home/emmett/Pictures/vibes.png)

### Easy Examples

Now time for some examples to help you get started. First let's print a partial and full question.

```python
from vibrant import *
print(question("This is my question")) # will only apply color to symbol.
print(question("This is my question",True)) # will print full text in color
```

Awesome, right?! I think so anyways, so that's all that matters. Next, let's get some colors going on!

```python
from vibrant import *
print(fblue + "This line of text will be blue" + reset)
"""Since acessing the data member directly, you'll have to handle the escape sequence yourself, which is easily achieved by typing reset after you done with your color, this applies to any direct access such as Text Styles, Background Colors, Text colors, etc.."""
```

If you don't feel like handling your own reset, there's the perfect solution for that as well!

```python
from vibrant import *
print(custom(fblue,"This line of text will be blue"))
"""Doing this gives you the exact same output as the example above, with a more precise manner, but that's not all custom allows you to do!"""
```

The custom parameters are in order Text Color, Text, Background Color, Style. The only expected parameters are Text Color and Text, you are free to leave the others set to their default state. Now let's use the all of the custom parameters.

```python
from vibrant import *
text = "Here's some example text for ya!"
print(custom(fblue,text,orange,underline))
"""While the the color combination leaves something to be desired, it is the expected output"""
print(custom(forange,text,blue))
```

## Chart

While chart is still a work in progress, feel free to try it out.  The only supported type of chart currently is horizontal bar chart and only text colors should be used with the charts. Also, you must have the base component of Vibrant installed.

```python
from vibechart import *
data = {'one': 1, 'two': 2, 'three': 3, 'twenty':20, 'Teena': 59}
bar_chart = HBarChart()
bar_chart.hbar(data, "my y label", "Clever Title")
```

The data set must always be a dictionary type with whole number values. If the values are **negative** or of **float** they will not be displayed or the program will **crash**. If these rules are followed though you can come out with a neat looking simple graph. Here's an example of the output from our above code.

![vibechart_showcase](/home/emmett/Pictures/vibechart_showcase.png)

The ability to change the color of the default graph data isn't supported yet, but it is easy to change it from the source code perspective. In the `vibechart.py`in the `create_hbar` method you can prefix the label with a Text Color to change it from the default. Such as `return forange + label + (" " * label_margin) + (self.block * value) + str(value)` will create the following output.

![orange_vibechart](/home/emmett/Pictures/orange_vibechart.png)

To change the color of the title or label simply prefix the desired color in your arguments list.

```python
from vibechart import *
data = {'one': 1, 'two': 2, 'three': 3, 'twenty':20, 'Teena': 59}
bar_chart = HBarChart()
bar_chart.hbar(data, fcyan + "my y label", fgreen + "Clever Title")
```

