---
title: 'API Documentation'
description: 'Learn about everything available in Container Env'
categories:
  - User Guides
---

Detailed documentation of the Container Env Python module.

## `get_environment()`

`get_environment(variable, default=None, encoding="utf-8")`

Returns the value of an environment variable if it exists.
If it does not exist and a {variable}_FILE variable exists, the content of
the file it points to will be returned.
If neither exist, it returns the supplied default argument.

### Arguments

* `name (str)`: Name of the environment variable based option.
* `default (str)`: Default option, returned when the variable does not exist.
* `encoding (str)`: Encoding used for reading files. [See the Python documentation for the possible values.](https://docs.python.org/3/library/codecs.html#standard-encodings)

### Returns

`str`: Value of the environment variable, or content of {name}_FILE file.

### Examples

Given an environment variable `DATABASE_USER` with the value `my_awesome_app`:

```python
from container_env import get_environment
print(get_environment('DATABASE_USER'))
```

Produces the output:

```sh
my_awesome_app
```

Given a file `/secrets/db_pass` containing `my_secret_password` and an environment variable `DATABASE_PASSWORD_FILE` with the value `/secrets/db_pass`:

```python
from container_env import get_environment
print(get_environment('DATABASE_PASSWORD'))
```

Produces the output:

```sh
my_secret_password
```