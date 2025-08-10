# fetchy-cli

Fetch strings from your terminal!

# Usage
Create an entry with `fet -n MyNewEntry "This is my new entry"`. This will create a new entry named "MyNewEntry" with the value of "This is my new entry". To fetch your entry, simply run `fet MyNewEntry`. This will print the value to the consol.<br>

*Pro-Tip: fetchy uses fuzzy matching so you don't need to match case*

## Warning
Do **not** use fetchy to store sensitive information. The values are stored as plain text. Think of this program as virtual sticky notes.


## Options
```
usage: fet [Name] [-n Name Value] [-c Name] [-d Name1 ...] [-r OldName NewName] [-l] [-?] 

positional arguments:
  name                  Name of entry to fetch. (Case sensitive)

options:
  -?, --help            Show this help message and exit.
  -v, --version         Show package version and exit.
  -c N, --copy N        Copy the value of [N] to the clipboard.
  -l, --list            List saved entry names and values.
  -n N V, --new N V     Create [N] with the value of [V]. (Overwrite existing)
  -d N1 [N2 ...], --delete N1 [N2 ...]
                        Delete [N1] etc.
  -r O N, --rename O N  Rename [O] to [N].
  -e N, --edit N        Edit the value of [N] in a text editor.

(fet with no arguments will list entries)
```

# Example

What is that excel number formatting that finance likes? <br>
`fet -n FinanceNums '[Green]#,##0,"K";[Red]-#,##0,"K";General'`<br>
Now just fetch it with `fet -c FinanceNums` (`-c` copies to the clipboard)<br>
Paste to excel :)









