---
title: Python One-Liners to share files on lan
date: 2018-06-29
description: Oneliners to start a server to serve files over a local area network.
...

Files can be easily shared among multiple devices over a local network by starting a http server using tools provided by python standard library, the module http.server on python3.X or SimpleHTTPServer on python2.X

Twisted is a better option for performance, you have to install dependencies from <span style="color:blue">[Twistd](https://twistedmatrix.com/trac/wiki)</span>

Change working directory to required location

Type in the following in a Terminal

For Python 2.X

```bash
  $ python -m SimpleHTTPServer port_number(optional)
```
or

For Python 3.X

```bash
  $ python -m http.server port_number(optional)
```

Using Twisted

```bash
  $ twistd -n web --path .
```
