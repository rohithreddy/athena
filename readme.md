# athena

**athena** is an elegant, minimalist, light-weight static blog generator
written in Python. It is based on Flask, Pandoc, and Tufte CSS.

![athena screenshot](/static/athena.png)

You can browse the [live demo here][demo].

## Why athena?

Because it is the simplest, yet aesthetically pure, static blog generator with
paramount focus on the reading experience. As a WordPress user since 2007, I
think it's time for a change. Other static blog generators are too feature
heavy and bloated. athena just works.

### Tufte CSS

Edward Tufte’s style is known for its simplicity, extensive use of sidenotes,
tight integration of graphics with text, and carefully chosen typography.
[More about ET][et].

## Installation

1. `git clone https://github.com/apas/athena.git`
1. `brew install pandoc`
1. `brew install pandoc-citeproc`
1. `brew install pandoc-crossref`
1. `brew install jez/formulae/pandoc-sidenote`
1. `virtualenv --python=/usr/bin/python env` or Python 2.7 equivalent path
1. `source env/bin/activate`
1. `pip install -r requirements.txt`

## Usage

### Post structure

athena reads Markdown files from the `pages/` directory and builds static HTML
files. Posts must start with the following YAML structure:

    ---
    title: Title of the post
    date: 2016-03-12
    description: A short description of the post.
    ...

Title and date values are extracted for the index loop and the post's
permalink. Both the author and description values are used in the post's HTML
meta tags and are optional. The name of the Markdown file can by anything.

### Tufte CSS-specific elements

athena uses the beautiful Tufte CSS layout. Markdown is automatically rendered
to proper HTML and corresponding Tufte rules.

I highlight all relevant syntax in the [elements][elems] file. However, a
brief summary of the most frequent elements is provided below.

**Image**

    ![Hackers and painters; by Pieter Bruegel.]( {{
    url_for('static', filename='img/bruegel.jpg') }}){#fig:bruegel}

A relevant directory to host and serve from all your image assets is
`static/img`. The image caption is used as the image's margin note.

**Side note** (Numbered footnote in the right margin)

    Etiam ut arcu nec massa bibendum lobortis ac eu justo. Proin sit amet
    sagittis est. [^note]

    [^note]: A note.

**Margin note** (Unnumbered footnote in the right margin)

    They're not doing research per se, though if in the course of
    trying to make good things they discover some new technique, so much the
    better. [^mn]

    [^mn]:
      {-} This is a margin note. Notice there isn't a number preceding
      the note.

**Code**

You can write inline code by enclosing text in single backticks.
Alternatively, for blocks use three backticks. athena supports code
highlighting via Pygmentize. 

    ``` {.python}
    # a code block with syntax highlighting
    def hello():
        print "world"
    ```

**Table**

When including a table element align the first column to the left for maximum
Tufte enjoyment.

    | Tables   |      Are      |  Cool |
    |:---------|---------------|-------|
    | col 1 is |  left-aligned |  Foo  |
    : A demo table. {#tbl:demo}

**Bib citations**

Simply create a `.bib` file in the `/pages` directory and populate it
accordingly. At build time, athena creates a new `.bib` index out of all
`.bib` files. Then, simply reference your citation as such:

    At one end you have people who are really mathematicians, but call
    what they're doing computer science so they can get
    DARPA grants. [@clark1988design]

It is recommended to end your Markdown files which reference a `.bib` citation
with a `# References` element in order to properly highlight them.

**Math**

You can write inline math by enclosing text in single dollar signs.
Alternatively, for blocks use double dollar signs and a space. Math is
rendered via [MathML][mml].

    See [@eq:euler].

    $$ e^{i\pi} - 1 = 0 $$ {#eq:euler}

**Cross-references**

You might have observed that for image, table, and math references
athena also relies on `{#fig:xxx}` and `[@fig:xxx]` (`tbl` and `eq`
respectively) elements. These are optional and are used by `pandoc-crossref`
to automatically generate numbered captions and references in the generated
text. For the complete cross-reference documentation please visit the
`pandoc-crossref` [repository][pdcf].

### Atom feed

athena generates an Atom feed at the `/feed.atom` endpoint.

### Remove boilerplate

Inside `templates/` edit various instances of default athena labeling in
`about.html`, `index.html`, and `page.html`. In `page.html` edit lines 19 and
24 (Facebook and Twitter image meta tags) and point both to a proper image
link inside `static/img/`. In `athena.py` amend lines 25, 28, 34 with your
blog and author name in order to appropriately generate the Atom feed.

### Try as you write

You can start local Flask server with `$ python athena.py` at
`127.0.0.1:5000`. This allows you to test everything locally before committing
and deploying to your remote server. If you're using Sublime Text I recommend
installing the LiveReload plugin for Safari or Google Chrome.

### Deploy

athena works out of the box with any server capable of serving HTML content.
If you do not want to pay for or own a server you can use GitHub Pages. It's
where the cool kids hang out nowadays, anyway. You can generate your static
blog with `$ python athena.py build`. A new `build/` directory will be created
(it's automatically ignored by git.) For subsequent builds, athena
rebuilds only the updated files, rather than the entire codebase.

If you're using your own hosting solution you know what to do now. Happy
blogging!

For GitHub pages a nice deployment workflow is the following:

1. Create a `username.github.io` repo.
1. `$ mkdir build` manually and `cd` in.
1. `$ git init` (athena's git ignores the `build/` directory; this is fine)
1. `$ git remote add origin git@github.com:username/username.github.io.git`
1. `$ cd ..`
1. `$ python athena.py build`
1. `$ cd build/`
1. `$ git add .`
1. `$ git commit -m "deploys athena"`
1. `$ git push origin master`

Wait a few moments and browse `username.github.io`. Happy blogging!

## License

MIT

[et]: https://en.wikipedia.org/wiki/Edward_Tufte
[demo]: https://apas.github.io/athena/
[elems]: https://raw.githubusercontent.com/apas/athena/pandoc/pages/elements.md
[mml]: https://www.w3.org/Math/whatIsMathML.html
[pdcf]: https://github.com/lierdakil/pandoc-crossref
