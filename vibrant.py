import re
from ascii_seq import *

#Color convience methods
def red(text):
  return partial(fred,text)

def black(text):
  return partial(fblack,text)

def green(text):
  return partial(fgreen, text)

def orange(text):
  return partial(forange, text)

def blue(text):
  return partial(fblue, text)

def magenta(text):
  return partial(fmegenta, text)

def cyan(text):
  return partial(fcyan, text)

def lgray(text):
  return partial(lgray, text)

def dgray(text):
  return partial(fdgray, text)

def lred(text):
  return partial(flred, text)

def lgreen(text):
  return partial(flgreen, text)

def lyellow(text):
  return partial(flyellow, text)

def lblue(text):
  return partial(flblue, text)

def lmagenta(text):
  return partial(flmagenta, text)

def lcyan(text):
  return partial(flcyan, text)

def white(text):
  return partial(fwhite, text)
#End font color convience method

#Background Color
def _black(text):
  return partial(bblack, text)

def _red(text):
  return partial(bred, text)

def _green(text):
  return partial(bgreen, text)

def _yellow(text):
  return partial(byellow, text)

def _blue(text):
  return partial(bblue, text)

def _magenta(text):
  return partial(bmagenta, text)

def _cyan(text):
  return partial(bcyan, text)

def _lgray(text):
  return partial(blgray, text)

def _dgray(text):
  return partial(bdgray, text)

def _lred(text):
  return partial(blred, text)

def _lgreen(text):
  return partial(blgreen, text)

def _lyellow(text):
  return partial(blyellow, text)

def _lblue(text):
  return partial(blblue, text)

def _lmagenta(text):
  return partial(blmagenta, text)

def _lcyan(text):
  return partial(blcyan, text)

def _white(text):
  return partial(bwhite, text)
#End background colors

#Style convience methods
def bold(text):
  return bold_ + text + reset_

def dim(text):
  return dim_ + text + reset_

def underline(text):
  return underline_ + text + reset_

def invert(text):
  return reverse_ + text + reset_

def hidden(text):
  return hidden_ + text + reset_
#End Style Convience methods

#Symbol convience methods
def esc_num(sequence):
  first_split = re.search(r'\[\d+', sequence).group(0)
  return first_split.split('[')[1]

def warning(text = "", _full = False):
  result = full(forange, warning_,text) if _full else \
  partial(forange, warning_) + text + reset_
  return result

def error( text = "", _full = False):
  result = full(fred, error_, text) if _full else \
  partial(fred, error_) + text + reset_
  return result

def question( text = "", _full = False):
  result = full(fcyan, question_, text) if _full else \
  partial(fcyan, question_) + text + reset_
  return result

def add( text = "", _full = False):
  result = full(fgreen, add_, text) if _full else \
  partial(fgreen, add_) + text + reset_
  return result

def check( text = "", _full = False):
  result = full(fmegenta, check_, text) if _full else \
  partial(fmegenta,check_) + text + reset_
  return result
#End Symbol Convience methods

def full(color,symbol, text):
  return color + symbol + text + reset_

def partial(color,symbol):
  return color + symbol + reset_

def custom(fcolor, text, bcolor = bdefault, fmt = bdefault):
  f_num = esc_num(fcolor)
  fmt_num = esc_num(fmt)
  b_num = esc_num(bcolor)
  return "\033[" + f_num + ";" + fmt_num + ";" + b_num + "m" + text + reset_