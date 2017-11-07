import sys
import os
import subprocess as proc

athena = "athena.py"
version = "python" + sys.version[:3]
activate_env_path = os.path.join("env", "bin", "activate_this.py")
activate_env = activate_env_path

def has_colours(stream):
  if not hasattr(stream, "isatty"):
    return False
  if not stream.isatty():
    return False
  try:
    import curses
    curses.setupterm()
    return curses.tigetnum("colors") > 2
  except:
    return False

has_colours = has_colours(sys.stdout)

def print_color(text, color = 7):
  if has_colours:
    seq = "\x1b[1;%dm" % (30 + color) + text + "\x1b[0m"
    sys.stdout.write(seq+"\n")
  else:
    sys.stdout.write(text+"\n")

print_color("==> Creating the virtual environment", 4)
proc.call(["virtualenv", "env"])

print_color("==> Activating the virtual environment", 4)
execfile(activate_env, dict(__file__=activate_env))

print_color("==> Installing pip dependencies", 4)
proc.call(["pip", "install", "-r", "requirements.txt"])

print_color("==> Installation complete", 4)
