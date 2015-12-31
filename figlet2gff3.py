#!/usr/bin/env python
import sys

data = sys.stdin.read()

line = {
    'source': 'Merlin',
    'exec': 'figlet2gff',
    'type': 'gene',
    'start': 20,
    'end': 50,
    'score': 1000,
    'strand': '+',
    'phase': '.',
    'attr': {}
}

def maxLineLength(data):
    q = 0
    for line in data.split('\n'):
        if len(line) > q:
            q = len(line)
    return q


offset = 20

with open('figlet.gff3', 'w') as handle:
    handle.write('##gff-version 3\n')

def pl(line):
    q = [
        line['source'],
        line['exec'],
        line['type'],
        line['start'] + offset,
        line['end'] + offset,
        line['score'],
        line['strand'],
        line['phase'],
        ';'.join(['%s=%s' % (k, v) for (k, v) in line['attr'].iteritems()])
    ]
    with open('figlet.gff3', 'a') as handle:
        handle.write('\t'.join(map(str, q)) + '\n')

mll = maxLineLength(data)
line.update({
    'attr': {'ID': 'test'},
    'start': 0,
    'end': mll
})

pl(line)

for idx, row in enumerate(data.split('\n')):
    if len(row.strip()) == 0: continue

    mRNAid = 'mRNA.%s' % idx
    line.update({
        'type': 'mRNA',
        'start': 0,
        'end': mll,
        'attr': {'Parent': 'test', 'ID': mRNAid}
    })
    pl(line)
    cols = row.split(' ')

    colidx = 0
    print '_'.join(cols)
    for col in cols:
        if col == '':
            colidx += 1
        else:
            # Add a CDS
            line.update({
                'type': 'CDS',
                'start': colidx,
                'end': colidx + len(col) - 1,
                'attr': {'Parent': mRNAid, 'ID': mRNAid + '.' + str(colidx)}
            })
            pl(line)
            colidx += len(col) + 1
