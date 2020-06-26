# Development Guide

Install the development dependencies:

```
poetry install
```

## Testing, Linting and Formatting

Run the unit tests:

```
$ coverage run --branch --omit tests* --module pytest
```

Show the coverage report:

```
$ coverage report
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

## Documentation

Start hot reload server:

```
$ hugo serve --source docs
```

Build the documentation:

```
$ hugo --source docs --destination ../build/docs
```
