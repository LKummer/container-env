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

Container Env is [available on PyPI](https://pypi.org/project/container-env/)
as `container-env`.

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

Lets have a look at it's functionality.

```python
from container_env import get_environment

print(get_environment("DATABASE_USER"))
```

If a `DATABASE_USER` environment variable exists, it's value will be printed.

If a `DATABASE_USER_FILE` environment variable exists and contains a path to a
file, the content of the file will be printed.

This enables great flexibility. Options can be managed using environment
variables. Any option can be used with secrets.
Making your Python containers easy to manage with any container orchestration
tool.

To learn more [see the full API documentation.]({{< ref "api.md" >}})
