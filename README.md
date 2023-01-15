# faker-web3

Web3-related fake data provider for Python Faker

![PyPI](https://img.shields.io/pypi/v/faker-web3)
![PyPI - Format](https://img.shields.io/pypi/format/faker-web3)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/faker-web3)
![GitHub](https://img.shields.io/github/license/rcstanciu/faker-web3)

## Installation

```
pip install faker-web3
```

## Usage:

```python
from faker import Faker

from faker_web3 import Web3Provider

fake = Faker()
fake.add_provider(Web3Provider)
```

### Private keys

```python
fake.web3_private_key()
# 0x1db498f960c133fd83351160687c91b6e41340959c9f03a810e8078f062562d1
```
