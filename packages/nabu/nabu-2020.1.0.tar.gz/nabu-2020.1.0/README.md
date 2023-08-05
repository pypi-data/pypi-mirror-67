# Nabu

ESRF tomography processing software.

## Installation

For installing the development version:

```bash
pip install [--user] git+https://gitlab.esrf.fr/tomotools/nabu.git
```
The above command should automatically install the following nabu Python dependencies:

- numpy, distributed, pytest
- For computations acceleration: pycuda, pyopencl
- [silx](http://www.silx.org/)
- [tomoscan](https://gitlab.esrf.fr/tomotools/tomoscan)

All of them can be installed with `pip`.

Please note that Nabu supports Python >= 3.5.

## Usage

Nabu can be used in several ways:
  - As a Python library, by features like `Backprojector`, `FlatField`, etc
  - As a standalone application with the command line interface
  - Through [Tomwer](https://gitlab.esrf.fr/tomotools/tomwer/)

For getting started quickly, just do:
```bash
nabu-config --bootstrap
```
Edit the generated configuration file (`nabu.conf`). Then:

```bash
nabu nabu.conf --slice 500-600
```

will reconstruct the slices 500 to 600, with processing steps depending on `nabu.conf` contents.

## Documentation

The documentation can be found on the [silx.org page](http://www.silx.org/pub/nabu/doc).

The latest documentation built by continuous integration can be found on [ESRF gitlab](https://paleo.gitlab-pages.esrf.fr/nabu/). 

## Running the tests

Once nabu installed, running

```bash
nabu-test
```
will execute all the tests. You can also specify specific module(s) to test, for example:
```bash
nabu-test preproc misc
```
You can also provide more `pytest` options, for example increase verbosity with `-v`, exit at the first fail with `-x`, etc. Use `nabu-test --help` for displaying the complete options list.



## Nabu - what's in a name ?

Nabu was the Mesopotamian god of literacy, rational arts, scribes and wisdom.
