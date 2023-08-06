# rfile

[![PyPI version](https://badge.fury.io/py/rfile.svg)](https://badge.fury.io/py/rfile)

## Overview

`rfile` generates an `Rfile` to make your R package set reproducable, similar to
how `Gemfile` and `Brewfile` work. This file is text, with prefixes indicating
the source, followed by the package name. This allows for easy versioning, and
portability.

```none
cran askpass
cran assertthat
cran backports
cran base
...
cran xml2
cran xopen
cran yaml
cran zoo
github bbc/bbplot
```

## Installing `rfile`

`pip install rfile`

## Backstory

I'm not in the trenches every day with R, sometimes taking breaks of months at a
time from the language. When I arrive back, I'm often looking at previous code,
and trying to get back up to speed as quickly as possible. If I've updated all
of my package via `brew` in the interim, I'm going to have a bad time with
missing R packages. Having an `Rfile` that knows about all the packages that I
previously had installed in R enables a quick recovery, and gets me back to
stumbling my way through the `tidyverse` again!

## Current Functionality

Currently, only reading and writing from the current directory is supported. The
default mirror for CRAN is `http://cran.us.r-project.org`, which can be changed
by specifying `-m/--mirror`.

## Usage

```none
rfile -h
usage: rfile [-h] [-m MIRROR]

Generate an Rfile for your packages

optional arguments:
  -h, --help            show this help message and exit
  -m MIRROR, --mirror MIRROR
                        Enter a mirror to use for CRAN (default:
                        http://cran.us.r-project.org)
```

### Generate an `Rfile`

`rfile` will create an `Rfile` with a list of installed packages in the currnet
working directory. This will cover both CRAN and Github packages. You can then
include this file in something similar to a "dotfiles" repository for easy
portability.

### Install packages from an `Rfile`

Run `rfile` in the same directory as the `Rfile`. That's it.
