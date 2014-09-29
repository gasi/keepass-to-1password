# KeePass XML to 1Password CSV converter

Migrate your KeePass(X) data to 1Password 4: Export your KeePass(X) data to XML,
use this script to convert it to a CSV, and then import the CSV into
1Password 4.

## Prerequisites

Install the following dependencies:

- `pip install beautifulsoup4`
- `pip install jinja2`

## Usage

- Export your KeePassX passwords to `./input/passwords.xml`.
- Run `./k1p.py`.
- Open *1Password* and go to *File > Import > Comma Delimited Text (.csv)* and
  pick `./output/passwords.csv`.
- Enjoy!

## Documentation

- [1Password 4.x CSV Documentation](https://learn2.agilebits.com/1Password4/Mac/en/KB/import.html#csv--comma-separated-values)

## License

This software is released under the [MIT License](http://opensource.org/licenses/MIT).

- Copyright (c) 2013–2014 [Vincent Stark](http://vstark.net)
- Copyright (c) 2014 [Daniel Gasienica](http://www.gasi.ch)
