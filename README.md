# Container Env

<p>
  <a href="https://lkummer.github.io/container-env/">
    <img src="assets/banner.svg" align="center">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/pypi/v/container_env">
  <img src="https://img.shields.io/github/workflow/status/lkummer/container-env/Integration?label=integration">
  <img src="https://img.shields.io/github/workflow/status/lkummer/container-env/Delivery?label=delivery">
  <img src="https://img.shields.io/github/license/lkummer/container-env">
</p>

Environment variables are the _easiest_ way to manage options in containers.
Especially when using Docker Swarm or Kubernetes.
Container Env makes it _easy_ to create applications with environment based
configuration.

*[Visit the website](https://lkummer.github.io/container-env/)* for more information.

## Motivation

Container Env encourages proper handling of secrets. It strives to:

* Make any option usable with secrets.
* Work easily with any kind of secrets.
* Be simple to integrate with Django, Flask and others.
* Provide a high quality solution.

## Usage

**[See the quick start guide](https://lkummer.github.io/container-env/guide/quickstart/)
for more details.**

Install from PyPI:

```s
$ pip install container_env
```

Import and use the [`get_environment()`](https://lkummer.github.io/container-env/guide/api/#get_environment)
function:

```python
from container_env import get_environment

# Look for DATABASE_USER and DATABASE_USER_FILE environment variables.
get_environment("DATABASE_USER", default="postgres")
# If DATABASE_USER exists it's value is returned.
# If DATABASE_USER_FILE exists and points to a file, the content of the
# file is returned.
# If neither exist, "postgres" is returned.
```

*[See the documentation](https://lkummer.github.io/container-env/guide/)*
to learn more about Container Env.

## Contributing

Please [check existing issues](https://github.com/LKummer/container-env/issues)
before opening a new one.

[See the development guide](https://lkummer.github.io/container-env/guide/development/)
to learn about the development setup.
