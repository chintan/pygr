
from pygr import seqdb

from pygr import blast

from pygr import cnestedlist

def main():
    """This function returns argument
    Example:
    >>> main()
    MVHLTDAEKA annotgi|171854975|dbj|AB364477.1|:0[0:52]
    MVHWTQEERD HBB_MUSGR[0:52]
    --
    VHLTDAEKAA annotgi|171854975|dbj|AB364477.1|:0[1:53]
    VHWTGEEKAL HBB_SQUAC[0:52]
    --
    VHLTDAEKAA annotgi|171854975|dbj|AB364477.1|:0[1:53]
    VSLTDEEKHL HBB2_TORMA[0:52]
    --
    """

    dna_db = seqdb.SequenceFileDB('data/hbb1_mouse.fa')

    dna_seq = dna_db['gi|171854975|dbj|AB364477.1|']

    prot_db = seqdb.SequenceFileDB('data/sp_all_hbb')

    blastmap = blast.BlastxMapping(prot_db)

    results = blastmap[dna_seq]

    results = list(results)

    match = results[0]

    for n, (src, dest, edge) in enumerate(match.edges()):

        print src[0:10], repr(src)

        print dest[:10], repr(dest)

        print '--'

        if n == 2: break


if __name__ == '__main__':
    import doctest
    doctest.testmod()










