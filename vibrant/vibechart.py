import os
from ascii_seq import *


class Chart:
  def __init__(self):
    self.width, self.height = os.get_terminal_size(0)
    self.left_margin = 15
    self.title_posx = int(self.width / 2)
    self.title_posy = 0
    self.y_label_pos = self.left_margin + 10

  def set_title(self, title):
    print('\033[2J')
    print('\033[{0};{1}H{2}'.format(
    self.title_posy, self.title_posx, title), end='')
    print('\b')

class HBarChart(Chart):
  def __init__(self, color = fdefault):
    super(HBarChart, self).__init__()
    self.block = color + '█' + reset_

  def create_hbar(self, label, value, spacing):
    label_margin = spacing - len(label)
    return  label + (" " * label_margin) + (self.block * value) + str(value)

  def set_footer(self, y_label):
    print('\033[{0};{1}H{2}'.format(self.row_space,self.title_posx,fdefault + y_label))

  def label_difference(self, labels):
    return len(max(labels, key=len))

  def hbar(self, data, x_label, title="PlaceHolder", symbol=None):
    """
      @param1 data: dictionary
      @param2 x_label: x-axis label string
      @param2 title: string title of the bar chart
      @param3 symbol: a any valid unicode/ascii character the default symbol █
      return: prints a horizontal bar chart
    """
    self.spacing = self.label_difference(data)
    self.row_space = 2
    self.set_title(title)
    if not symbol:
      symbol = self.block
      for key, value in data.items():
        bar = self.create_hbar(key, value, self.spacing)
        print('\033[{0};{1}H{2}'.format(self.row_space+1, self.left_margin, bar))
        self.row_space += 2
        print('\b')
      self.set_footer(x_label)