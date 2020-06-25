# Development Guide

Run the unit tests:

```
$ coverage run --branch --module pytest
```

Show the coverage report:

```
$ coverate report
```

Lint the sources:

```
$ pylint docker_env tests
$ flake8
```

Format the sources:

```
$ black docker_env tests
```
