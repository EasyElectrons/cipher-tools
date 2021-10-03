# Introduction

This is a Python module that provides tools to encode, decode, and analyze ciphers.

# Installation

This package is not yet on `pip`, and so must be installed manually.

1. `git clone git@github.com:EasyElectrons/cipher-tools.git`
2. Either symlink, copy, or move the package into your Python `dist-packages` directory.

# Usage

This package uses a standard notation to represent ciphertext (CT) and plaintext (PT).

* PT should always be entered/represented as `lowercase`.
* CT should always be entered/represented as `UPPERCASE`.

Take for example the caesar cipher.  Let's encipher the string `hello world` using the standard +3 shift.

```python3
>>> from cipher_tools import encode
>>> 
>>> encode.caesar('hello world')
'KHOOR ZRUOG'

```

