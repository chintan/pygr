
from pygr import seqdb

from pygr import blast

from pygr import cnestedlist

def main():
    """This function returns argument
    Example:
    >>> main()
    VHLTDAEKAA frame 1
    """

    dna_db = seqdb.SequenceFileDB('data/hbb1_mouse.fa')

    dna_seq = dna_db['gi|171854975|dbj|AB364477.1|']

    prot_db = seqdb.SequenceFileDB('data/sp_all_hbb')

    blastmap = blast.BlastxMapping(prot_db)

    results = blastmap[dna_seq]

    results = list(results)

    match = results[0]

    print match.seq[0:10], 'frame', match.seq.frame

if __name__ == '__main__':
    import doctest
    doctest.testmod()










