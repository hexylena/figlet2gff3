#!/usr/bin/env python
import sys
import argparse

class colourChar:
    def __init__(self, chr, colour):
        self.chr = chr
        self.colour = colour

    def __str__(self):
        return self.chr

class colourString:
    def __init__(self, data):
        if '\x1b' in data:
            inCC = False
            curCC = ""
            chr = None
            for i in range(len(data)):
                if data[i] == '\x1b':
                    inCC = True
                elif inCC and data[i] != 'm':
                    curCC += data[i]
                elif inCC and data[i] == 'm':
                    inCC =False
                elif:
                    chr = data[i]

            pass
        else:
            self.chrs = data.split('')

    def __len__(self):
        return len(self.chrs)

    def __str__(self):
        return ''.join(self.chrs)

class fig2gff3:

    def __init__(self, chrId, sparse=False):
        self.chrId = chrId
        self.sparse = sparse
        self.wroteHeader = False

        self.offset = 20
        self.line = {
            'source': self.chrId,
            'exec': 'figlet2gff',
            'type': 'gene',
            'start': self.offset,
            'end': 50,
            'score': 1000,
            'strand': '+',
            'phase': '.',
            'attr': {}
        }

    def maxLineLength(self):
        q = 0
        for line in self.lines:
            if len(line) > q:
                q = len(line)
        return q

    def writeLine(self, line, handle=sys.stdout):
        if not self.wroteHeader:
            handle.write('##gff-version 3\n')
        if isinstance(line, list):
            handle.write('\t'.join(line) + '\n')
        else:
            handle.write(line + '\n')

    def pl(self, line):
        q = [
            line['source'],
            line['exec'],
            line['type'],
            line['start'] + self.offset,
            line['end'] + self.offset,
            line['score'],
            line['strand'],
            line['phase'],
            ';'.join(['%s=%s' % (k, v) for (k, v) in line['attr'].iteritems()])
        ]
        self.writeLine(map(str, q))

    def process(self, data):
        self.lines = [colourString(x) for x in data.split('\n')]
        self.hasColors = '\x1b' in data

        mll = self.maxLineLength()
        self.line.update({
            'attr': {'ID': 'test'},
            'start': 0,
            'end': mll
        })
        self.pl(self.line)

        # for idx, row in enumerate(data.split('\n')):
            # if len(row.strip()) == 0: continue

            # mRNAid = 'mRNA.%s' % idx
            # line.update({
                # 'type': 'mRNA',
                # 'start': 0,
                # 'end': mll,
                # 'attr': {'Parent': 'test', 'ID': mRNAid}
            # })
            # pl(line)
            # cols = row.split(' ')

            # colidx = 0
            # print '_'.join(cols)
            # for col in cols:
                # if col == '':
                    # colidx += 1
                # else:
                    # # Add a CDS
                    # line.update({
                        # 'type': 'CDS',
                        # 'start': colidx,
                        # 'end': colidx + len(col) - 1,
                        # 'attr': {'Parent': mRNAid, 'ID': mRNAid + '.' + str(colidx)}
                    # })
                    # pl(line)
                    # colidx += len(col) + 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='figlet2gff3')
    parser.add_argument('--source', default='-', help='Data source. - defaults to stdin')
    parser.add_argument('--chrId', default='Test', help='Landmark ID')
    parser.add_argument('--sparse', action='store_true', help='Sparse image, do not fill in every pixel')
    args = parser.parse_args()

    if args.source == '-':
        data = sys.stdin.read()
    else:
        data = open(args.source, 'r').read()

    kw = vars(args)
    del kw['source']
    fig = fig2gff3(**kw)
    fig.process(data)
