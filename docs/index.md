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

Take for example the caesar cipher.  Let's encipher the string `'hello world'` using the standard +3 shift.

```python
>>> from cipher_tools import encode
>>> 
>>> encode.caesar('hello world')
'KHOOR ZRUOG'

```

Now lets see what happens when we try to encode `'HELLO WORLD'`.

```python
>>> encode.caesar('HELLO WORLD')
'HELLO WORLD'

```

This is because the encoder engine is already interpreting the string `'HELLO WORLD'` as CT, and thus doesn't need to be enciphered further.  This allows for partial enciphering/deciphering of a string and skipping over text for complicated "shift register" style cipher schemes.

If multi-layered enciphering is desired, simply convert the section in question back to the appropriate case.

```python
>>> from cipher_tools import encode, decode
>>> stage1 = encode.caesar('hello world')
>>> print(stage1)
KHOOR ZRUOG
>>> stage2 = encode.vigenere(stage1.tolower(), 'lemon')
>>> print(stage2)
VLACE KVGCT
>>> reverse1 = decode.vigenere(stage2, 'lemon')
>>> print(reverse1)
khoor zruog
>>> reverse2 = decode.caesar(reverse1.upper())
>>> print(reverse2)
hello world
```

