

# adrpy - Simple management of Architecture Decision Records

## Installation

`adrpy` is pip installable:

- clone this repository

- in the base folder use:

  ```python
  >pip install -e .
  ```

  (NOTE: by using the `-e` option, edits you make in the repos will be reflected in your installed version)

Coming soon - hosting on PyPI.org

## Usage

```
usage: adrpy [-h] [-d ADR_DIR] [-f ADR_DIR_FILE] <command> [params [params ...]]

Manage Architecture Design Records - ADR's.

positional arguments:
  <command>        init <directory to init> - inits (creates if necessary) new directory,
                   new <description of new ADR> - creates new ADR using description for title,
                   accept <ADR number or prefix> - marks ADR as Accepted,
                   reject <ADR number or prefix> - marks ADR as Rejected,
                   supercede <old ADR number or prefix> <new ADR number or prefix> - marks old ADR
                                as superceded by new one,
                   link  <ADR number or prefix>  <ADR number or prefix> - marks two ADR's as related,
                   related  <ADR number or prefix> <description of new ADR> - creates a new ADR and
                                marks it as related to other one,
                   list [full|status|filename [<ADR number or prefix>]> - prints listings of either
                                all ADR's or specified ADR to stdout in requested format.
                                No params = status format, all ADR's
  params           description of the ADR or additional params

optional arguments:
  -h, --help       show this help message and exit
  -d ADR_DIR       path to directory of ADR files
  -f ADR_DIR_FILE  path of .adr-dir file
```



## 

## 

## 

## 