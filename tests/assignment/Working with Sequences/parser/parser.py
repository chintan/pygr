
#from pygr import seqdb

import csv

def read_csv(ifile, seq): #'assume 1st col is id, 2nd is sequence'
    """This function returns the argument.
    Example:
    #>>> read_csv(ifile,seq)    
    143
    """

    class seqholder(object):
   
      
        def __init__(self, id, sequence):
            (self.id, self.sequence, self.length) = (id, sequence, len(sequence))
   
    for row in csv.reader(ifile):
            yield seqholder(row[0],row[1]

    
    myseqs = seqdb.SequenceFileDB('someseqs.csv', reader=read_csv)

    print len(myseqs)
    
    print myseqs.keys()

    foo = myseqs['foo']
 
    print len(foo)
   
    print foo
    
    # Don't forget to close the file myseqs.close()

if __name__ == "__read_csv__":
    import doctest
    doctest.testmod()
