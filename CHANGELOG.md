# CHANGELOG

## 2014-09-28

- Used fixed CSV columns as documented in
  [1Password CSV Import File Format][1password-csv].
- Remove first line of CSV template with column names as they (incorrectly)
  get imported as an item in 1Password.
- Escape `"` in all fields.
- Add support for converting multiline KeePass comments into 1Password
  notes.

[1password-csv]: https://learn2.agilebits.com/1Password4/Mac/en/KB/import.html#csv--comma-separated-values
