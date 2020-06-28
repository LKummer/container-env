---
title: 'Quick Start Guide'
description: 'Get started with Container Env quickly and easily'
categories:
  - Application
---

All you need to know to get started with Container Env.

## Prerequisites

Python `3.8` or higher is required.

## Installation

Container Env is available on PyPI as `container-env`.

```s
$ pip install container-env
```

## Usage

Container Env helps create environment variable based configuration.
When using Docker Compose or Kubernetes, the easiest way to manage options is
through environment variables.

The [`get_environment()`]({{< ref "api.md#get_environment" >}})
function helps read options from the environment.
It has a special twist, it can also read files.
Making integration with different ways to store secrets seamless.

Consider the following snippet from a Django `settings.py` file:

```python
from container_env import get_environment

SECRET_KEY = get_environment("DJANGO_KEY")
```

If a `DJANGO_KEY` environment variable exists, it's value will be used.

If a `DJANGO_KEY_FILE` environment variable exists and contains a path to a
file, the content of the file will be used.

This enables great flexibility. Options can be managed using environment
variables. Any option can be used with secrets.
Making your Python containers easy to manage with any container orchestration
tool.

To learn more [see the full API documentation.]({{< ref "api.md" >}})
