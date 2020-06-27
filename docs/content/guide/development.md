---
title: 'Development Guide'
description: 'Development instructions for contribution'
categories:
  - Development
---

Everything you should know when working on this project.

## Installing Dependencies

Container Env uses [Poetry](https://python-poetry.org/) for dependency management. If you do not have it installed, download it from PyPI:

```s
$ pip install poetry
```

Using Poetry, install the development dependencies:

```s
$ poetry install
```

## Testing, Linting and Formatting

Run the unit tests check coverate:

```s
$ coverage run --branch --omit tests* --module pytest
```

Show the coverage report:

```s
$ coverage report
```

Lint the sources:

```s
$ pylint container_env tests
$ flake8
```

Format the sources:

```s
$ black container_env tests
```

## Documentation

Container Env uses [Hugo](https://gohugo.io/) to build the documentation. The CD pipeline uses version [`0.73.0`](https://github.com/gohugoio/hugo/releases/tag/v0.73.0). It is not managed through Poetry and needs to be installed manually.

Start a hot reload server on `localhost:1313/container-env`:

```s
$ hugo serve --source docs
```

Build the documentation to `dist/docs`:

```s
$ hugo --source docs --destination ../dist/docs
```
