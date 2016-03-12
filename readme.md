# athena

**athena** is an elegant, minimalist, light-weight static blog generator written in Python. It is based on Flask and Tufte CSS.

![Athena screenshot](/static/athena.png)

## Why Athena?

Because it is the simplest, yet aesthetically pure static blog generator with paramount focus on the reading experience. As a WordPress user since 2007, I think it's time for a change. Other static blog generators are too feature-heavy for my taste. athena just works.

## Installation

1. Git clone this repo and `cd` in.
1. `$ virtualenv env`
1. `$ source env/bin/activate`
1. `$ pip install -r requirements.txt`

## Modifications

In order for the Tables Markdown extension to properly render tables according to the custom Tufte CSS rules you need to modify `tables.py`. Open `env/lib/python2.7/site-packages/markdown/extensions/tables.py` and edit line 57 to:

    table = etree.SubElement(parent, 'table', {"class":"table-wrapper"})

## Usage

### Post structure

Athena reads Markdown files from the `pages/` directory and builds static HTML files. Posts must start with the following YAML-like structure:

    title: Title of the post
    date: 2016-03-12
    description: A short description of the post.

Title and date values are extracted for both the index loop and the post's permalink. The description value is used in the post's HTML meta tags.

### Tufte CSS-specific elements

Athena uses the beautiful Tufte CSS layout. Most Markdown elements are automatically rendered to the proper HTML element and corresponding Tufte treatment. However, in order to fully utilize Tufte CSS, it is recommended you include images and margin notes the following way.

    <figcaption>Figure 1: A margin note about the image.</figcaption>
    ![An image.](/static/img/an-image.png "An image.")

In the end of the paragraph you want to the margin note to refer to add:

    <label for="sn-anything" class="margin-toggle sidenote-number"><input type="checkbox" id="sn-anything" class="margin-toggle"><span class="sidenote">Write your margin note here.</span>

When including a table element align the first column to the left for maximum Tufte enjoyment.

    | Tables   |      Are      |  Cool |
    |:---------|---------------|-------|
    | col 1 is |  left-aligned |  Foo  |

### Remove boilerplate

Inside `templates/` edit various instances of foobar Athena labeling in `about.html`, `index.html`, and `page.html`. In `page.html` edit lines 19 and 24 (Facebook and Twitter image meta tags) and point them to a proper image link inside `static/img/`. 

### Try as you write

Upon successfully installing athena you can start a local Flask server with `$ python athena.py`. Then visit `127.0.0.1:5000` from your browser. This allows you to test everything locally before committing and deploying to your remote server. If you're using Sublime Text and Google Chrome, I recommend installing the LiveReload plugins so that you don't have to manually refresh upon save.

### Deploy

athena works out of the box with any server capable of serving HTML content. If you do not want to pay for or own a server you can use GitHub pages. It's where the cool kids hang out nowadays, anyway. You can generate your static blog with `$ python athena.py build`. A new `build/` directory will be created by athena (it's automatically ignored by git.) For subsequent builds, athena doesn't rebuild the entire codebase, rather than only the updated files.

If you're using your own hosting solution you know what to do now. Happy blogging!

For GitHub pages deployment a nice workflow is the following:

1. Create a `your-username.github.io` repo.
1. `$ mkdir build` manually and `cd` in.
1. `$ git init` (Since athena's git ignores the `build/` directory this is fine)
1. `$ git remote add origin git@github.com:your-username/your-username.github.io.git
1. `$ cd ..`
1. `$ python athena.py build`
1. `$ cd build/`
1. `$ git add .`
1. `$ git commit -m "deploys athena"
1. `$ git push origin master`

Wait a few moments and browse `your-username.github.io`. Happy blogging!

**Tip**: for future builds and new posts you can automate this process with [this simple bash function][bash] in your `.bash_profile`.

⚠️ **Warning**: after building athena with `$ python athena.py build` you may encounter the following error in your terminal.

    ValueError: Unexpected status '404 NOT FOUND' on URL /static/

Don't worry about it. The `build/` directory and all `static/` resources are successfully generated in spite of this URL mismatch.

[bash]: https://gist.github.com/apas/dd4632a5ce372e75adec
