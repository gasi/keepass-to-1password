# KeePass XML to 1Password CSV converter

Migrate your KeePass(X) data to 1Password 4: Export your KeePass(X) data to XML,
use this script to convert it to a CSV, and then import the CSV into
1Password 4.

## Usage

- Export your KeePassX passwords to `./input/passwords.xml`.
- Run `./k1p.py`.
- Open *1Password* and go to *File > Import > Comma Delimited Text (.csv)* and
  pick `./output/passwords.csv`.
- Enjoy!

## License

This software is released under the [MIT License](http://opensource.org/licenses/MIT).

Copyright (c) 2013 [Vincent Stark](http://vstark.net)
