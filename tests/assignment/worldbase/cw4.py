
from pygr import worldbase

def main():
    """This function returns the argument.
    Example:
    >>> main()
    ['Bio.MSA.UCSC.hg17_multiz17way', 'Bio.MSA.UCSC.hg18_multiz17way', 'Bio.MSA.UCSC.hg18_multiz28way', 'Bio.MSA.UCSC.hg18_multiz44way']
    ['petMar1', 'mm9', 'gorGor1', 'cavPor3', 'eriEur1', 'pteVam1', 'panTro2', 'anoCar1', 'micMur1', 'galGal3', 'proCap1', 'ponAbe2', 'loxAfr2', 'rn4', 'oryLat2', 'vicPac1', 'danRer5', 'canFam2', 'dipOrd1', 'echTel1', 'sorAra1', 'tetNig1', 'equCab2', 'bosTau4', 'ochPri2', 'myoLuc1', 'oryCun1', 'rheMac2', 'turTru1', 'xenTro2', 'speTri1', 'otoGar1', 'dasNov2', 'choHof1', 'taeGut1', 'calJac1', 'tarSyr1', 'ornAna1', 'tupBel1', 'fr2', 'gasAcu1', 'hg18', 'felCat3', 'monDom4']   
    116467    
    197195432 
    35 
    CTAAACTA chr1[9098273:9098281]
    CTGAAATT dasNov2.scaffold_203475

    TCGGAGCTAAACTA chr1[9098267:9098281]
    AGGAAGCTATTCCT calJac1.Contig7152

    TCGGAGCTAAACTA chr1[9098267:9098281]
    AGTCAACTAATCTT canFam2.chr29

    TCGGAGCTAAACTA chr1[9098267:9098281]
    AGGAGGCTATTCTT otoGar1.scaffold_81178.1-424864

    TCGGAGCTAAACTA chr1[9098267:9098281]
    AAATGGCTATTCGT pteVam1.scaffold_7567

    """
    print worldbase.dir('hg[0-9]+_multi', matchType='r')      

    msa = worldbase.Bio.MSA.UCSC.hg18_multiz44way()

    print msa.seqDict.prefixDict.keys()

    turTru1 = msa.seqDict.prefixDict['turTru1']

    print len(turTru1)

    chr1 = msa.seqDict['mm9.chr1']

    print len(chr1)

    print len(chr1.db)

    ival = chr1[9098000:9099000]

    idDict = ~(msa.seqDict)

    for src,dest,e in msa[ival].edges():
        print src, repr(src), '\n', dest, idDict[dest], '\n'


if __name__ == '__main__':
        import doctest
        doctest.testmod()



