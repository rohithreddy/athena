import sys
from urlparse import urljoin
from datetime import date, datetime
from flask import Flask, render_template, request
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from werkzeug.contrib.atom import AtomFeed

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'markdown.extensions.tables', 'markdown.extensions.footnotes']
FREEZER_REMOVE_EXTRA_FILES = False

athena = Flask(__name__)
athena.config.from_object(__name__)
pages = FlatPages(athena)
freezer = Freezer(athena)

def make_external(url):
  return urljoin(request.url_root, url)

@athena.route("/feed.atom")
def recent_feed():
  feed = AtomFeed("Athena",
    feed_url = request.url_root,
    url = request.url_root,
    subtitle="Athena Atom Feed")
  for page in pages:
    feed.add(page["title"],
      unicode(page.__html__()),
       content_type='html',
       url=make_external("/posts/"+page.path),
       author="Apostolos Papadopoulos",
       updated=datetime.combine(page["date"], datetime.min.time()),
       published=datetime.combine(page["date"], datetime.min.time()),
       summary=page["description"]
      )
  return feed.get_response()

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
