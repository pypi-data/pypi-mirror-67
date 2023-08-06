![build and deploy](https://github.com/nmhnmh/sitekicker/workflows/build%20and%20deploy/badge.svg?branch=master)

This is my **personal** static site generator, it lacks testings and documents at the moment.
If you need a static site generator, find one [here](https://www.staticgen.com/) with good community support.

**SiteKicker** is yet another static site builder written in **Python3**(no support for python2).

Current Project Status: **Beta, usable, but no testing and documentation**

# Local development

We use [poetry](https://python-poetry.org/) to manage dependencies and virtual environments, make sure you have poetry installed, then in root directory of the project, run `poetry install` first to install all the dependencies and create the virtual environment, then run `poetry shell` to activate the virtual environment.

# Dependencies: what and why

* PyYAML: parse configurations(`site.yml` `folder.yml`) and entry front matters
* Pygments: code highlighter
* beautifulsoup4: working with html
* markdown: markdown compiler
* pymdown-extensions: markdown compiler extensions
* Jinja2: a template engine
* watchdog: local folder/file activity watcher

## site.yml(or sitekicker.yml)

```yml
# Name of the site
name: An Awesome Site
# Base URL for the site, will be used to generate absolute urls
base_url: https://example.org
# Directory where build output will be saved, could be relative path or absolute path
output_dir: .dist
# Directory that contains layout/templates, default: templates, optional, supported template format is jinja2
template_dir: templates
# Directories that will be copied, such as folders with assets or binary files
copy_dirs:
  - assets
```

## folder.yml

```yml
# The options set in this file will be applied to all entries inside the folder where this file is found,
# we refer to these entries as 'affected items of this file' below.
# This is a good place to set some common options and flags.
# You could also add any custom options below, prefix and tags are special because they has special meaning

# The prefix will be prepended to all items affected by this file, 'article.html' will be 'abc/article.html'
# if multiple prefix specified along the way, they will be concatenated and prefixed to the final url,
# so if two prefix 'a' and 'b' specified, then the final url will be '/a/b/article.html'
prefix: abc
# The tags listed here will be added to all items affected by this file, tags specified at different places
# will be merged, duplicate tags will be removed, original order of tags will be maintained
tags:
  - global tag 1
  - global tag 2
```

## Entry Front Matter

```yml
# In this file your specified options for the entry, beside some predefined ones like 'id', 'title', 'date'
# you can add your own custom options, and use it inside your templates, options specified here will override
# options specified in meta.yml in parent folder, except 'prefix' and 'tags', the former will be concatenated,
# the later will be merged

# A unique id to identify the entry, no special chars, space will be substituted with hyphens, optional
# when not set, will try to use file name as id, will emit an error when it is not possible
id: some-thing-as-name
# Title of the entry, mandatory, may contain any characters
title: Sitekicker is another Static Site Generator
# Date of the writing, mandatory, in the format of YYYY-MM-DD
date: 2016-10-20
# Date of update, optional
update_date: 2016-11-20
# Tags that applies to this entry, optional
# current entry will inherit all tags in its parent folders,
# if folder 'a' contains tag 'a', folder 'a/b' contains tag 'b'
# entry 'a/b/entry.md' contains tag 'c', then eventually the entry will
# have there tags: 'a', 'b', 'c'
tags:
  - tag1
  - tag2
  - tag3
```
