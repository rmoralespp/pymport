# pymport

[![CI](https://github.com/rmoralespp/pymport/workflows/CI/badge.svg)](https://github.com/rmoralespp/pymport/actions?query=event%3Arelease+workflow%3ACI)
[![versions](https://img.shields.io/pypi/pyversions/pymport.svg)](https://github.com/rmoralespp/pymport)
[![codecov](https://codecov.io/gh/rmoralespp/pymport/branch/main/graph/badge.svg)](https://app.codecov.io/gh/rmoralespp/pymport)
[![license](https://img.shields.io/github/license/rmoralespp/pymport.svg)](https://github.com/rmoralespp/pymport/blob/main/LICENSE)
[![Linter: ruff](https://img.shields.io/badge/linter-_ruff-orange)](https://github.com/charliermarsh/ruff)

## About

A lightweight Python linter for checking unused imports

### Features

TODO: Add features list

## Installation

TODO: Add installation instructions


## Development

To contribute to the project, you can run the following commands for testing and documentation:

First, ensure you have the latest version of `pip`:

```python -m pip install --upgrade pip```

### Running Unit Tests

```
pip install --group=test  # Install test dependencies, skip if already installed
python -m pytest tests/ # Run all tests
python -m pytest tests/ --cov # Run tests with coverage
```

### Running Linter

```
pip install --group=lint  # Install linter dependencies, skip if already installed
ruff check . # Run linter
```


## License

This project is licensed under the [MIT license](LICENSE).
