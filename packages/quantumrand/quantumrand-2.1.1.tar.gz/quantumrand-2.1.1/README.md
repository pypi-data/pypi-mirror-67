# QuantumRand

[![PyPI version](https://badge.fury.io/py/quantumrand.svg)](https://pypi.org/project/quantumrand/) [![PyPI - License](https://img.shields.io/pypi/l/quantumrand)](https://pypi.org/project/quantumrand/) [![Bitcoin](https://img.shields.io/badge/BTC-143TbUxTB9XPqBKu565acFXCHWSdsRLnKK-blue)](https://www.blockchain.com/btc/address/143TbUxTB9XPqBKu565acFXCHWSdsRLnKK)

### maintained fork of [lmacken/quantumrandom](https://github.com/lmacken/quantumrandom)

This project provides tools for interacting with The ANU Quantum Random Number Generator ([qrng.anu.edu.au](http://qrng.anu.edu.au>`)). It communicates with their JSON API and provides a Python API, ~~a `qrand` command-line tool, and a Linux `/dev/qrand` character device.~~ (This has to be fixed).

QuantumRand was made to work with Python 3. Python 2 support has been dropped as it is now reached End of Life.

> As of 2.0, QuantumRand has had to adapt to ANU's SSL certificate expiring. QuantumRand is still able to connect via SSL by default, but please be aware that QuantumRand cannot securely validate ANU's SSL authenticity until they update their certificate.

## Installation

`pip install quantumrand`

## Python API

### Low Level API Examples

The QuantumRand Python module contains a low-level `get_data`
function, which is modelled after the ANU Quantum Random Number
Generator's JSON API. It returns variable-length lists of either
`uint16` or `hex16` data.

Valid `data_type` values are `uint16` and `hex16`.

The `array_length` and `block_size` cannot be larger than `1024`.

If for some reason the API call is not successful, or the incorrect amount of data is returned from the server, this function will raise an exception.

* `quantumrand.get_data()`

```
[26646]
```

* `quantumrand.get_data(data_type='uint16', array_length=5)`

```
[42796, 32457, 9242, 11316, 21078]
```

* `quantumrand.get_data(data_type='hex16', array_length=5, block_size=2)`

```
['f1d5', '0eb3', '1119', '7cfd', '64ce']
```

### High Level API Examples

Based on the above `get_data` function, quantumrand also provides a bunch
of higher-level helper functions that make easy to perform a variety of
tasks.

#### Generate a random intger

* `quantumrand.randfloat(0, 20)`

```
18.936751354238194
```

* `quantumrand.randint(0, 20)`

```
5
```

#### Generate random HEX as a string

* `quantumrand.hex()[:10]`

```
'8272613343'
```

#### Generate random binary formatted string

* `quantumrand.binary()[:3]`

```
'\xa5\x0d\x1e'
```

#### The previous `binary()` function returns 10000 bytes

* `len(quantumrand.binary())`

```
10000
```

#### Generate uint16 values as a Numpy array

* `quantumrand.uint16()`

```
numpy.array([24094, 13944, 22109, 22908, 34878, 33797, 47221, 21485, 37930, ...], dtype=numpy.uint16)
```

#### Randomly select an item from a list

* `quantumrand.list_picker(["Mary", "Bill", "Chad", "Nicole"])`

```
"Nicole"
```

#### Dice rolling

The two main methods are `dice_roll()` and `quick_dice()`

Both methods can take 3 optional arguments:
* `n` is the number of dice to roll (default is `1`)
* `d` is the number of sides on each die (default is `6`)
* `min` is the lowest number on the die (default is `1`)

`dice_roll()` returns a tuple where the first value is a list of individual dice rolls, and the second value is the total of the dice rolls.

`quick_dice()` returns an integer with the total dice rolls. This is best for single die rolls and dice rolls you don't need to know the individual rolls of.

* Roll a single d6 (a standard 6 sided die) and show results
  * `quantumrand.dice_roll()`

```
([3], 3)
```

* Roll a single d20 and show results
  * `quantumrand.dice_roll(d=20)`

```
([19], 19)
```

* Roll two d9 (0-9) and show results
  * `quantumrand.dice_roll(d=9, n=2, min=0)`

```
([0,3], 3)
```

* Roll three d8 and show results
  * `quantumrand.dice_roll(d=8, n=3)`

```
([4,8,3], 15)
```

* Roll three d9 (0-9) and show only the total.
  * `quantumrand.quick_dice(d=9, n=3, min=0)`

```
24
```

* You can roll a die with any number of sides
  * `quantumrand.quick_dice(d=67)`

```
1
```

## Using the Command Line Tool

### Currently still being fixed!

Getting a random integer within a range:

* `qrand --int --min 5 --max 15`

```
7
```

Getting random binary values:

* `qrand --binary`

```
���I�%��e(�1��c��Ee�4�������j�Կ��=�^H�c�u
oq��G��Z�^���fK�0_��h��s�b��AE=�rR~���(�^Q�)4��{c�������X{f��a�Bk�N%#W
+a�a̙�IB�,S�!ꀔd�2H~�X�Z����R��.f
```

Getting random hex values:

* `qrand --hex`

```
1dc59fde43b5045120453186d45653dd455bd8e6fc7d8c591f0018fa9261ab2835eb210e8
e267cf35a54c02ce2a93b3ec448c4c7aa84fdedb61c7b0d87c9e7acf8e9fdadc8d68bcaa5a
```

## Creating /dev/qrand

This will have to be updated, as it is not working for any supported version of Python currently.
