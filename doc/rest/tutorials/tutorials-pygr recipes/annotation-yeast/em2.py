
from pygr import worldbase, annotation, mapping, seqdb

yeast = seqdb.BlastDB('sacCer1')

import motility

matches = motility.find_iupac(chr1, 'GCANTGC')

overlaps = []

for (start, stop, _, _) in matches:
    
    match = yeast['chr1'][start:stop]
    
    upstream_hits = upstream_map[match]
    
    if len(upstream_hits):
        overlaps.append(upstream_hits)   1

def main():
    """This function does something.
    Example:
    >>> main()
    1
    """
    print len(overlaps)


if __name__ == '__main__':
    import doctest
    doctest.testmod()


