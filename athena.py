import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'markdown.extensions.tables']

athena = Flask(__name__)
athena.config.from_object(__name__)
pages = FlatPages(athena)
freezer = Freezer(athena)

@athena.route("/")
def index():
  return render_template("index.html", pages=pages)

@athena.route("/about/")
def about():
  return render_template("about.html")

@athena.route("/posts/<path:path>/")
def page(path):
  page = pages.get_or_404(path)
  return render_template("page.html", page=page)

if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == "build":
    freezer.freeze()
  else:
    athena.run()
