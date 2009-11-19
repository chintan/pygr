
from pygr import worldbase

def main():
    """This function returns the argument.
    Example:
    >>> main()
    49
    247249719
    cctcggcctcccaaagtgctgggattacaggcgtgagccaccgcgcagccccaactagactttaaaagccctggaggtgggcgggtttaggctgccttgctctccgctgtgtgcccagccccagggactgtgcctagcacttgcaggtgctcaaaagaagcacttaatgaatggatctctttcccctagcaaccctgtgaaatttcatcacacccactctgaaggagaggaaaccgaggctcaggtccagacaatgcagaagccacagagctaatgagtgccagagctagggcatgaatcatcgtggcctcagaagctgttgcccttaCTCCCAGTGAAGACAATCTAGGGTTATGGGAGGAAAAGGTACCGACGGGGGTCAGAGACCAGCATCCCAGCTCAGAGCCTGGGACTCACGCACCTGTGAAATGTTCCTTCCTTCATCTGCTCATCTCCCCACTGGCCAATCAGGACCAAGAAGGGCAGCTCtacccacccat
    """
    hg18 = worldbase.Bio.Seq.Genome.HUMAN.hg18()

    print len(hg18)

    chr1 = hg18['chr1']

    print len(chr1)

    ival = chr1[20000000:20000500]

    print ival
 
if __name__ == '__main__':
        import doctest
        doctest.testmod()



