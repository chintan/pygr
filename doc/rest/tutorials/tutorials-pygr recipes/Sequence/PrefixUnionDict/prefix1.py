
from pygr import seqdb

from pygr import worldbase

def main():
    
    """This function returns argument.
    Example:
    >>> main()    
    125
    125
    ['rn4.chr6_random', 'rn4.chr19_random', 'rn4.chr8_random', 'rn4.chrX', 'rn4.chr13', 'rn4.chr12', 'rn4.chr11', 'rn4.chr15_random', 'rn4.chr17', 'rn4.chr16', 'rn4.chr15', 'rn4.chr14', 'rn4.chr19', 'rn4.chr18', 'rn4.chrM', 'rn4.chr1_random', 'rn4.chr13_random', 'rn4.chr3_random', 'rn4.chr9_random', 'rn4.chr14_random', 'rn4.chr10', 'rn4.chrUn_random', 'rn4.chr4_random', 'rn4.chr18_random', 'rn4.chr2_random', 'rn4.chr20_random', 'rn4.chr20', 'rn4.chr10_random', 'rn4.chr11_random', 'rn4.chr7', 'rn4.chr6', 'rn4.chr5', 'rn4.chr4', 'rn4.chr3', 'rn4.chr2', 'rn4.chr1', 'rn4.chr7_random', 'rn4.chrX_random', 'rn4.chr9', 'rn4.chr8', 'rn4.chr16_random', 'rn4.chr5_random', 'rn4.chr17_random', 'rn4.chrUn', 'rn4.chr12_random', 'mm8.chrY_random', 'mm8.chr8_random', 'mm8.chrY', 'mm8.chrX', 'mm8.chr13', 'mm8.chr12', 'mm8.chr11', 'mm8.chr10', 'mm8.chr17', 'mm8.chr16', 'mm8.chr15', 'mm8.chr14', 'mm8.chr5_random', 'mm8.chr19', 'mm8.chr18', 'mm8.chrM', 'mm8.chr1_random', 'mm8.chr13_random', 'mm8.chr9_random', 'mm8.chrUn_random', 'mm8.chr10_random', 'mm8.chr7', 'mm8.chr6', 'mm8.chr5', 'mm8.chr4', 'mm8.chr3', 'mm8.chr2', 'mm8.chr1', 'mm8.chr7_random', 'mm8.chrX_random', 'mm8.chr9', 'mm8.chr8', 'mm8.chr15_random', 'mm8.chr17_random', 'hg17.chr6_random', 'hg17.chr19_random', 'hg17.chr8_random', 'hg17.chrY', 'hg17.chrX', 'hg17.chr13', 'hg17.chr12', 'hg17.chr11', 'hg17.chr15_random', 'hg17.chr17', 'hg17.chr16', 'hg17.chr15', 'hg17.chr14', 'hg17.chr19', 'hg17.chr18', 'hg17.chrM', 'hg17.chr1_random', 'hg17.chr13_random', 'hg17.chr3_random', 'hg17.chr6_hla_hap2', 'hg17.chr9_random', 'hg17.chr22_random', 'hg17.chr10', 'hg17.chr4_random', 'hg17.chr18_random', 'hg17.chr2_random', 'hg17.chr22', 'hg17.chr20', 'hg17.chr21', 'hg17.chr10_random', 'hg17.chr6_hla_hap1', 'hg17.chr7', 'hg17.chr6', 'hg17.chr5', 'hg17.chr4', 'hg17.chr3', 'hg17.chr2', 'hg17.chr1', 'hg17.chr7_random', 'hg17.chrX_random', 'hg17.chr9', 'hg17.chr8', 'hg17.chr16_random', 'hg17.chr5_random', 'hg17.chr17_random', 'hg17.chr12_random']
    """    
    mm8 = worldbase.Bio.Seq.Genome.MOUSE.mm8()
    
    rn4 = worldbase.Bio.Seq.Genome.RAT.rn4()
        
    hg17 = worldbase.Bio.Seq.Genome.HUMAN.hg17()
    
    pud = seqdb.PrefixUnionDict(dict(hg17=hg17, mm8=mm8, rn4=rn4))
    
    print len(pud)

    print len(hg17) + len(rn4) + len(mm8)

    print pud.keys()
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()