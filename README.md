# figlet2gff3

I don't think this ever needed to exist, but now it does. Whee. Turn the output
of figlet/toilet into a gff3 file compatible with JBrowse.

## Usage

```console
$ echo '2016!' | figlet | python figlet2gff3.py
```

![](http://i.imgur.com/vOS1EXI.png)

Okay that's a lie. After the first pass through figlet I usually save to a temporary file,
then manually kern the letters a bit and touch them up for nicer display. In the above
picture I did a crappy job with the 2 and the 6 looks weird, but this was for a one-off
release annoucement and I'm *way* too lazy to fix it

## TODO

- [ ] Configurable landmark (currently hardcoded to 'Merlin' from the test dataset I used)
- [ ] Support the --gay/--metal flags
- [ ] Support the full charset and use opacity for the mapping
- [ ] Add a jp2a2gff3
- [ ] Hell, just paint pixel by pixel
- [ ] City-Skyline2bigwig? Lol.

## LICENSE

GPLv3
