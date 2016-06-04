# athena

**athena** is an elegant, minimalist, light-weight static blog generator written in Python. It is based on Flask and Tufte CSS.

![athena screenshot](/static/athena.png)

You can browse the [live demo here][demo].

## Why athena?

Because it is the simplest, yet aesthetically pure, static blog generator with paramount focus on the reading experience. As a WordPress user since 2007, I think it's time for a change. Other static blog generators are too feature-heavy for my taste. athena just works.

### Tufte CSS

Edward Tufte’s style is known for its simplicity, extensive use of sidenotes, tight integration of graphics with text, and carefully chosen typography. [More about ET][et].

## Installation

1. Git clone this repo and `cd` in.
1. `python install.py`

### Modifications

:bulb: As of [commit `91cfe00`][commit] the following necessary modifications are performed automatically by way of the installer script.

In order for the Tables Markdown extension to properly render tables according to the custom Tufte CSS rules you need to modify `tables.py`. Open `env/lib/python2.7/site-packages/markdown/extensions/tables.py` and edit line 57 to:

    table = etree.SubElement(parent, 'table', {"class":"table-wrapper"})

In order for the Footnotes Markdown extension to properly render footnotes according to the custom Tufte CSS rules you need to modify `footnotes.py`. Open `env/lib/python2.7/site-packages/markdown/extensions/footnotes.py` and replace all its contents with [the following `footnotes.py` version.](https://gist.github.com/apas/fbdcc1617be4b9dbcab8895ad028b285)

## Usage

### Post structure

athena reads Markdown files from the `pages/` directory and builds static HTML files. Posts must start with the following YAML-like structure:

    title: Title of the post
    date: 2016-03-12
    description: A short description of the post.

Title and date values are extracted for both the index loop and the post's permalink. The description value is used in the post's HTML meta tags.

### Tufte CSS-specific elements

athena uses the beautiful Tufte CSS layout. Markdown is automatically rendered to proper HTML and corresponding Tufte rules. However, in order to fully utilize Tufte CSS, it is recommended you include images with a caption (i.e., a margin note in Tufte parlance) the following way: write an additional `<figcaption>` tag a line above or below the Markdown image reference.

    <figcaption>Figure 1: A margin note about the image.</figcaption>
    ![An image.](/static/img/an-image.png "An image.")

A relevant directory to host and serve from all your image assets is `static/img`.

In the end of the paragraph (or even inline) you want to the margin note to refer to, add:

    [^footnote]

and subsequently, at the end of the file add:

    [^footnote]: Text for the margin note.

When including a table element align the first column to the left for maximum Tufte enjoyment.

    | Tables   |      Are      |  Cool |
    |:---------|---------------|-------|
    | col 1 is |  left-aligned |  Foo  |

### Remove boilerplate

Inside `templates/` edit various instances of foobar athena labeling in `about.html`, `index.html`, and `page.html`. In `page.html` edit lines 19 and 24 (Facebook and Twitter image meta tags) and point them to a proper image link inside `static/img/`.

### Try as you write

Upon successfully installing athena, a local Flask server starts automatically. Now, just visit `127.0.0.1:5000` from your browser. Generally, you can start a local Flask server with `$ python athena.py`. This allows you to test everything locally before committing and deploying to your remote server. If you're using Sublime Text and Google Chrome, I recommend installing the LiveReload plugins so that you don't have to manually refresh upon save.

### Deploy

athena works out of the box with any server capable of serving HTML content. If you do not want to pay for or own a server you can use GitHub Pages. It's where the cool kids hang out nowadays, anyway. You can generate your static blog with `$ python athena.py build`. A new `build/` directory will be created by athena (it's automatically ignored by git.) For subsequent builds, athena doesn't rebuild the entire codebase, rather than only the updated files.

If you're using your own hosting solution you know what to do now. Happy blogging!

For GitHub pages deployment a nice workflow is the following:

1. Create a `your-username.github.io` repo.
1. `$ mkdir build` manually and `cd` in.
1. `$ git init` (Since athena's git ignores the `build/` directory this is fine)
1. `$ git remote add origin git@github.com:your-username/your-username.github.io.git`
1. `$ cd ..`
1. `$ python athena.py build`
1. `$ cd build/`
1. `$ git add .`
1. `$ git commit -m "deploys athena"`
1. `$ git push origin master`

Wait a few moments and browse `your-username.github.io`. Happy blogging!

:bulb: **Tip**: install athena as executable in your `$PATH`. Start the local server and build your site from anywhere. Create a file named `athena` in `/usr/local/bin/` or your `$PATH` equivalent with the following content:

    #!/bin/bash

    if [[ $# -eq 1 ]]; then
      cd /directory/where/athena/is && source env/bin/activate && python athena.py build
    else
      cd /directory/where/athena/is && source env/bin/activate && python athena.py
    fi

Then make it executable:

    $ chmod +x /usr/local/bin/athena

## License

MIT

[et]: https://en.wikipedia.org/wiki/Edward_Tufte
[demo]: https://apas.github.io/athena/
[commit]: https://github.com/apas/athena/commit/91cfe00224b08f02bddf6aad4a7039aa54a3cd9e
