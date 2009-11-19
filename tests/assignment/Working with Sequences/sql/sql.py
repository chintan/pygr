
from pygr import worldbase

from pygr import sqlgraph

class UCSCmRNA(sqlgraph.RNASQLSequence):
    """This function returns the argument.
    Example:
    >>> UCSCmRNA()
    37428
    888
    gttatgaagaaggtccggtgttttcttacccacctccttccctcctttttataataccagtgaaacttggtttggagcatttctttcacataaaggtaactgcagaggctatttcctggaatgaatcaacgagtgaaacgaataactctatggtgactgaattcatttttctgggtctctctgattctcaggaactccagaccttcctatttatgttgttttttgtattctatggaggaatcgtgtttggaaaccttcttattgtcataacagtggtatctgactcccaccttcactctcccatgtacttcctgctagccaacctctcactcattgatctgtctctgtcttcagtcacagcccccaagatgattactgactttttcagccagcgcaaagtcatctctttcaagggctgccttgttcagatatttctccttcacttctttggtgggagtgagatggtgatcctcatagccatgggctttgacagatatatagcaatatgcaagcccctacactacactacaattatgtgtggcaacgcatgtgtcggcattatggctgtcacatggggaattggctttctccattcggtgagccagttggcgtttgccgtgcacttactcttctgtggtcccaatgaggtcgatagtttttattgtgaccttcctagggtaatcaaacttgcctgtacagatacctacaggctagatattatggtcattgctaacagtggtgtgctcactgtgtgttcttttgttcttctaatcatctcatacactatcatcctaatgaccatccagcatcgccctttagataagtcgtccaaagctctgtccactttgactgctcacattacagtagttcttttgttctttggaccat
    tgcagaggctatttcctggaatgaatcaacgagtgaaacgaataactctatggtgactgaattcatttttctgggtctctctgattctcaggaactccagaccttcctat
    ataggaaggtctggagttcctgagaatcagagagacccagaaaaatgaattcagtcaccatagagttattcgtttcactcgttgattcattccaggaaatagcctctgca
    """

    #'interpret row objects as sequence object a la known GeneMrna'
    
    def __len__(self): # get length by running SQL query
        return self._select('length(seq)') # SQL SELECT expression

    serverInfo = sqlgraph.DBServerInfo(host='genome-mysql.cse.ucsc.edu', user='genome')

    mrna = sqlgraph.SQLTable('hg18.knownGeneMrna', serverInfo=serverInfo,itemClass=UCSCmRNA, itemSliceClass=seqdb.SeqDBSlice)

    print len(mrna)

    s = ucsc_mrna.mrna['uc009vjh.1']
 
    print s

    t = s[100:210]
    
    print t
     
    print -t

    # When your done using the database close it 
    # serverinfo.close()

if __name__ == "__UCSCmRNA__":
    import doctest
    doctest.testmod()
