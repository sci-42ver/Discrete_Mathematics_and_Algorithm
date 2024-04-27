"""
I didn't use this script because character-by-character diff is not easy to implement from scratch.
Although we can use icdiff by `system()` here.
"""
# use pdf2txt.py to convert to text https://pdfminersix.readthedocs.io/en/latest/
import difflib,re

## https://stackoverflow.com/a/64404008/21294350
# red = lambda text: f"\033[38;2;255;0;0m{text}\033[38;2;255;255;255m"
# green = lambda text: f"\033[38;2;0;255;0m{text}\033[38;2;255;255;255m"
# blue = lambda text: f"\033[38;2;0;0;255m{text}\033[38;2;255;255;255m"
# white = lambda text: f"\033[38;2;255;255;255m{text}\033[38;2;255;255;255m"

# https://chezsoi.org/lucas/blog/colored-diff-output-with-python.html
try:
    from colorama import Fore, Back, Style, init
    # https://stackoverflow.com/questions/60155499/how-to-preserve-python-colorama-color-output-when-using-tee-on-windows#comment106417183_60155499
    init(strip=False)
except ImportError:  # fallback so that the imported classes always exist
    class ColorFallback():
        __getattr__ = lambda self, name: ''
    Fore = Back = Style = ColorFallback()
def color_diff(line):
  if line.startswith('+'):
    return Fore.GREEN + line + Fore.RESET
  elif line.startswith('-'):
    return Fore.RED + line + Fore.RESET
  elif line.startswith('^'):
    print("blue line")
    return Fore.BLUE + line + Fore.RESET
  else:
    return line

file_1_name="mcs_2018-unlocked.txt"
file_2_name="mcs-unlocked.txt"
file_1=open(file_1_name,'r').read().splitlines()
file_2=open(file_2_name,'r').read().splitlines()
exclusion_list=["mcs"]
find_problem=False
block=""
skip_line="SKIP-------------------------------------------\n"
show_skip=False
skip_Contents_list=True
# check_diff_pattern=lambda pattern,line:re.search("^ "+pattern,line) or \
#                     re.search("^"+Fore.GREEN+"\+"+pattern,line) or \
#                     re.search("^"+Fore.RED+"\-"+pattern,line)
for line in difflib.unified_diff(file_1, file_2, fromfile=file_1_name, tofile=file_2_name, lineterm=''):
  skip=False
  for pattern in exclusion_list:
    if pattern in line:
      skip=True
  # if check_diff_pattern("Problem [0-9]",line):
  if re.search("^[ \+\-]?Problem [0-9]",line):
    print("find problem:"+line)
    find_problem=True
  if re.search("^@@",line):
    if block!="" and not find_problem:
      print(block)
    elif show_skip:
      print(skip_line+block+skip_line)
    else:
      pass
    block=color_diff(line)
    find_problem=False
    # The above if must be the last one before 'if not skip' to avoid continue unnecessarily.
    continue
  if not skip:
    block+='\n'+color_diff(line)
