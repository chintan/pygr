
from pygr import worldbase

def main():
    """This function returns the argument.
    Example:
    >>> main()
    46
    ['chr6_random', 'chr19_random', 'chr8_random', 'chrY', 'chrX', 'chr13', 'chr12', 'chr11', 'chr15_random', 'chr17', 'chr16', 'chr15', 'chr14', 'chr19', 'chr18', 'chrM', 'chr1_random', 'chr13_random', 'chr3_random', 'chr6_hla_hap2', 'chr9_random', 'chr22_random', 'chr10', 'chr4_random', 'chr18_random', 'chr2_random', 'chr22', 'chr20', 'chr21', 'chr10_random', 'chr6_hla_hap1', 'chr7', 'chr6', 'chr5', 'chr4', 'chr3', 'chr2', 'chr1', 'chr7_random', 'chrX_random', 'chr9', 'chr8', 'chr16_random', 'chr5_random', 'chr17_random', 'chr12_random']
    245522847
    1000  
    chr1[100000000:100001000]
    ATTCAGGCAATGTTGACTTCATTAGTGTTGACAGAAAATAAGCATAAAAATGCAAAACATTGTTGGCTTAACCTGAATATACCTGCATTACCTATTATTAACCAGTTTGTGTTGCCAAAAGACTTATTCCTTGGCATTAAAATGGAGCACTTAAAAATATTTCTAAAAAGCAAATGCCCACACGCTGGTCTTTGCAGCAAATAAGGGTATTTATACTTTTAAAATATTTTAAGTCCATAATTGGATTAATATACACACCTTCTTATGTATAAGGAGTTCAGATCATATAAACACCGTACAATCCAAAAAACCCTACTGAGAATAAAACTAAATAGGCTTATGATAAGAAATACAGATATTCCCATGTATTTACAAATATCATAGACACACAAATTTGGTCAAATACTGTAAAGAAAGAAGAAGtacctgtacctctacctctacctctacctcctctacctcctctacctcctctacctcctctacctcctctacctcctcttcctctacctctacctctacctctacctctacccacggtctccctttccctctctttccacggtctccctctgatgccgagccgaagctggactgtactgctgccatctcggctcactgcaacctccctgcctgattctcctgcctcaacctgccgagtgcctgcgattgcaggcgcgcgccgccacgcctgactggttttcgtatttttttggtggagacggggtttcgctgtgttggccgggctggtctccagctcctaacctcgagtgatccgccagcctcggcctcccgaggtgccgggtttgcagaggagtctcattcactcagtgctcaatggtgcccaggctggagtgcagtggcgtgatctcggctcgctacaacctccacctcccagcagcctgccttggcctcccaaagtgccgagattgcagtctccgcccggctgccaccccatctgggaagtgaggagcatctctgcctggccgcccatcgtctg                                                                    **********************************************************************
    """
    worldbase.dir('Bio.Seq.Genome.HUMAN') 
   
    hg17 = worldbase.Bio.Seq.Genome.HUMAN.hg17()

    print len(hg17)

    print hg17.keys()

    chr1 = hg17['chr1']

    print len(chr1)

    s = chr1[100000000:100001000]

    print len(s)

    print repr(s)
   
    print s

if __name__ == "__main__":
    import doctest
    doctest.testmod()
