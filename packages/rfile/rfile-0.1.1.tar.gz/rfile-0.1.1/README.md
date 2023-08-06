# rfile

`rfile` generates an `Rfile` to make your R package set reproducable, similar to
how `Gemfile` and `Brewfile` work.

## Current Functionality

Currently, only reading and writing from the current directory is supported. The
current mirror for CRAN is hardcoded to `http://cran.us.r-project.org`.

## Usage

### Generate an `Rfile`

`rfile` will create an `Rfile` with a list of installed packages in the currnet
working directory. This will cover both CRAN and Github packages. You can then
include this file in something similar to a "dotfiles" repository for easy
portability.

### Install packages from an `Rfile`

Run `rfile` in the same directory as the `Rfile`. That's it.
