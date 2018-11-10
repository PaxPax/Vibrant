import re


fdefault = '\033[39m'
fblack = '\033[30m'
fred = '\033[31m'
fgreen = '\033[32m'
forange = '\033[33m'
fblue = '\033[34m'
fmegenta = '\033[35m'
fcyan = '\033[36m'
flgray = '\033[37m'
fdgray = '\033[90m'
flred = '\033[91m'
flgreen = '\033[92m'
flyellow = '\033[93m'
flblue = '\033[94m'
flmagenta = '\033[95'
flcyan = '\033[96m'
fwhite = '\033[97m'

#Background Color
default = '\033[49m'
black = '\033[40m'
red = '\033[41m'
green = '\033[42m'
yellow = '\033[43'
blue = '\033[44m'
magenta = '\033[45m'
cyan = '\033[46m'
lgray = '\033[47m'
dgray = '\033[100m'
lred = '\033[101m'
lgreen = '\033[102m'
lyellow = '\033[103m'
lblue = '\033[104m'
lmagenta = '\033[105m'
lcyan = '\033[106m'
white = '\033[107m'

#Symbols
_warning = '[!] '
_question = '[?] '
_error = '[-] '
_add = '[+] '
_check = '[✓] '

bold = '\033[1m'
dim = '\033[2m'
underline = '\033[4m'
reverse = '\033[7m'
hidden = '\033[8m'
reset = '\033[0m'

def esc_num(sequence):
  first_split = re.search(r'\[\d+', sequence).group(0)
  return first_split.split('[')[1]

def warning(text = "", _full = False):
  result = full(forange, _warning,text) if _full else \
  partial(forange, _warning) + text + reset
  return result

def error( text = "", _full = False):
  result = full(fred, _error, text) if _full else \
  partial(fred, _error) + text + reset
  return result

def question( text = "", _full = False):
  result = full(fcyan, _question, text) if _full else \
  partial(fcyan, _question) + text + reset
  return result

def add( text = "", _full = False):
  result = full(fgreen, _add, text) if _full else \
  partial(fgreen, _add) + text + reset
  return result

def check( text = "", _full = False):
  result = full(fmegenta, _check, text) if _full else \
  partial(fmegenta,_check) + text + reset
  return result

def full(color,symbol, text):
  return color + symbol + text + reset

def partial(color,symbol):
  return color + symbol + reset

def custom(text, fcolor, bcolor = default, fmt = default):
  f_num = esc_num(fcolor)
  fmt_num = esc_num(fmt)
  b_num = esc_num(bcolor)
  return "\033[" + f_num + ";" + fmt_num + ";" + b_num + "m" + text + reset