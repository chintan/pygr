
from pygr import worldbase, annotation, mapping, seqdb

import motility

yeast = seqdb.BlastDB('sacCer1')

matches = motility.find_iupac(chr1, 'GCANTGC')

def main():
    """This function does something.
    Example:
    >>> main()
    43
    """
    print len(matches)

if __name__ == '__main__':
    import doctest
    doctest.testmod()


