# figlet2gff3

I don't think this ever needed to exist, but now it does. Whee. Turn the output
of figlet/toilet into a gff3 file compatible with JBrowse.

## Usage

```console
$ echo '2016!' | figlet | python figlet2gff3.py
```

![](http://i.imgur.com/vOS1EXI.png)

## TODO

- [ ] Configurable landmark (currently hardcoded to 'Merlin' from the test dataset I used)
- [ ] Support the --gay/--metal flags
- [ ] Support the full charset and use opacity for the mapping

## LICENSE

GPLv3
