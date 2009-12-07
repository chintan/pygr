
from pygr import worldbase, annotation, mapping, seqdb

def main():
    """This function returns the argument.
    Example:
    >>> main()
    annot1[0:300] chr1[1000:1300] cctcagtaatccgaaaagccgggatcgaccgccccttgcttgcagccgggcactacaggacccgcttgctcacggtgctgtgccagggcgccccctgctggcgactagggcaactgcagggctctcttgcttagagtggtggccagcgccccctgctggcgccggggcactgcagggccctcttgcttactgtatagtggtggcacgccgcctgctggcagctagggacattgcagggtcctcttgctcaaggtgtagtggcagcacgcccacctgctggcagctggggacactgccggg        **********************************************************************
    """
    hg17 = worldbase.Bio.Seq.Genome.HUMAN.hg17()

    exonSlices = {1:('chr1', 1000, 1300), 2:('chr1', 2000, 2099), 3:('chr1', 3000, 3600)}

    exons = annotation.AnnotationDB(exonSlices, hg17, sliceAttrDict=dict(id=0, start=1, stop=2))

    exon = exons[1]

    print repr(exon), repr(exon.sequence), exon.sequence

if __name__ == "__main__":
    import doctest
    doctest.testmod()
