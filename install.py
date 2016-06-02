import sys
import os
import subprocess as proc
import requests

athena = "athena.py"
version = "python" + sys.version[:3]
activate_env_path = os.path.join("env", "bin", "activate_this.py")
activate_env = activate_env_path
table_file_path = os.path.join("env", "lib", version,
                    "site-packages",
                    "markdown",
                    "extensions",
                    "tables.py")
table_oldline = "        table = etree.SubElement(parent, 'table')"
table_newline = "        table = etree.SubElement(parent," \
        " 'table', {\"class\":\"table-wrapper\"})"
footnote_file_path = os.path.join("env", "lib", version,
                      "site-packages",
                      "markdown",
                      "extensions",
                      "footnotes.py")
new_footnote_file_path = "https://gist.githubusercontent.com/" \
        "apas/fbdcc1617be4b9dbcab8895ad028b285/raw/" \
        "010c3602dfc6ddf284ac54fed6b39868b312954c/footnotes.py"

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

print_color("==> Install pip dependencies", 4)
proc.call(["pip", "install", "-r", "requirements.txt"])

print_color("==> Initiating custom markdown extensions" \
            " modifications", 4)
print_color("     -- tables.py", 4)
fin = open(table_file_path, "r")
table_file = fin.read()
fin.close()
new_table_file = table_file.replace(table_oldline, table_newline)
fout = open(table_file_path, "w")
fout.write(new_table_file)
fout.close()

print_color("     -- footnotes.py", 4)
new_footnote_file = requests.get(new_footnote_file_path)
fout = open(footnote_file_path, "w")
fout.write(new_footnote_file.text)
fout.close()

print_color("==> Installation complete", 4)

print_color("==> Running athena", 4)
try:
  proc.call(["python", athena])
except KeyboardInterrupt as e:
  print_color("\n==> Shutting down athena", 4)
  sys.exit(0)
