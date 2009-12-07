
from pygr import worldbase, annotation, mapping, seqdb

def main():
    """This function returns the argument.
    Example:
    >>> main()
    isoform 0: cctcagtaatccgaaaagccgggatcgaccgccccttgcttgcagccgggcactacaggacccgcttgctcacggtgctgtgccagggcgccccctgctggcgactagggcaactgcagggctctcttgcttagagtggtggccagcgccccctgctggcgccggggcactgcagggccctcttgcttactgtatagtggtggcacgccgcctgctggcagctagggacattgcagggtcctcttgctcaaggtgtagtggcagcacgcccacctgctggcagctggggacactgccgggTACCTGAGGCTGAGGAAGGAGAAGGGGATGCACTGTTGGGGAGGCAGCTGTAACTCAAAGCCTTAGCCTCTGTTCCCACGAAGGCAGGGCCATCAGGCACCAAAGGGATTCTGCCAGCATAGTGCTCCTGGACCAGTGATACACCCGGCACCCTGTCCTGGACACGCTGTTGGCCTGGATCTGAGCCCTGGTGGAGGTCAAAGCCACCTTTGGTTCTGCCATTGCTGCTGTGTGGAAGTTCACTCCTGCCTTTTCCTTTCCCTAGAGCCTCCACCACCCCGAGATCACATTTCTCACTGCCTTTTGTCTGCCCAGTTTCACCAGAAGTAGGCCTCTTCCTGACAGGCAGCTGCACCACTGCCTGGCGCTGTGCCCTTCCTTTGCTCTGCCCGCTGGAGACGGTGTTTGTCATGGGCCTGGTCTGCAGGGATCCTGCTACAAAGGTGAAACCCAGGAGAGTGTGGAGTCCAGAGTGTTGCCAGGACCCAGGCACAGGCATTAGTGCCCGTTGGAGAAAACAGGGGAATCCCGAAGAAATGGTGGGTCCTGGCCATCCGTGAGATCTTCCCAGGGCAGCTCCCCTCTGTGGAATCCAATCTG
    isoform 1: cctcagtaatccgaaaagccgggatcgaccgccccttgcttgcagccgggcactacaggacccgcttgctcacggtgctgtgccagggcgccccctgctggcgactagggcaactgcagggctctcttgcttagagtggtggccagcgccccctgctggcgccggggcactgcagggccctcttgcttactgtatagtggtggcacgccgcctgctggcagctagggacattgcagggtcctcttgctcaaggtgtagtggcagcacgcccacctgctggcagctggggacactgccgggCTGCATGTAACTTAATACCACAACCAGGCATAGGGGAAAGATTGGAGGAAAGATGAGTGAGAGCATCAACTTCTCTCACAACCTAGGCCAGTAAGTAGTTACCTGAGGCTGAGGAAGGAGAAGGGGATGCACTGTTGGGGAGGCAGCTGTAACTCAAAGCCTTAGCCTCTGTTCCCACGAAGGCAGGGCCATCAGGCACCAAAGGGATTCTGCCAGCATAGTGCTCCTGGACCAGTGATACACCCGGCACCCTGTCCTGGACACGCTGTTGGCCTGGATCTGAGCCCTGGTGGAGGTCAAAGCCACCTTTGGTTCTGCCATTGCTGCTGTGTGGAAGTTCACTCCTGCCTTTTCCTTTCCCTAGAGCCTCCACCACCCCGAGATCACATTTCTCACTGCCTTTTGTCTGCCCAGTTTCACCAGAAGTAGGCCTCTTCCTGACAGGCAGCTGCACCACTGCCTGGCGCTGTGCCCTTCCTTTGCTCTGCCCGCTGGAGACGGTGTTTGTCATGGGCCTGGTCTGCAGGGATCCTGCTACAAAGGTGAAACCCAGGAGAGTGTGGAGTCCAGAGTGTTGCCAGGACCCAGGCACAGGCATTAGTGCCCGTTGGAGAAAACAGGGGAATCCCGAAGAAATGGTGGGTCCTGGCCATCCGTGAGATCTTCCCAGGGCAGCTCCCCTCTGTGGAATCCAATCTG
    """
    hg17 = worldbase.Bio.Seq.Genome.HUMAN.hg17()

    exonSlices = {1:('chr1', 1000, 1300), 2:('chr1', 2000, 2099), 3:('chr1', 3000, 3600)}

    exons = annotation.AnnotationDB(exonSlices, hg17, sliceAttrDict=dict(id=0, start=1, stop=2))

    spliceGraph = {exons[1]:{exons[2]:None, exons[3]:None}, exons[2]:{exons[3]:None}}

    def walk_graph(graph, node, results, path=()):
        try:
            for node2 in graph[node]:
                walk_graph(graph, node2, results, path + (node,))
        except KeyError: # end node, so save complete path
            results.append(path + (node,))

    isoforms = []

    walk_graph(spliceGraph, exons[1], isoforms) # generate isoforms

    for i,transcript in enumerate(isoforms):
        s = ''.join([str(exon.sequence) for exon in transcript])
        print 'isoform %d: %s' % (i, s)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


