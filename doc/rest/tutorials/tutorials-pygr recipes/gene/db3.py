
from pygr import worldbase, annotation, mapping, seqdb

def main():
    """This function returns the argument.
    Example:
    >>> main()
    """
    hg17 = worldbase.Bio.Seq.Genome.HUMAN.hg17()

    exonSlices = {1:('chr1', 1000, 1300), 2:('chr1', 2000, 2099), 3:('chr1', 3000, 3600)}

    exons = annotation.AnnotationDB(exonSlices, hg17, sliceAttrDict=dict(id=0, start=1, stop=2))

    spliceGraph = {exons[1]:{exons[2]:None, exons[3]:None}, exons[2]:{exons[3]:None}}

    class GFF3Row(object):

        def __init__(self, line):
            cols = line.split()
            self.type = cols[2]
            self.id = cols[0] # sequence ID
            self.start = int(cols[3]) - 1 # correct for 1-based coords
            self.stop = int(cols[4])
      
            if cols[6] == '+': # convert to Pygr convention
                self.orientation = 1
          
            elif cols[6] == '-':
                self.orientation = -1
      
            else:
                raise ValueError('Bad strand: %s' % cols[6])
      
            for s in cols[8].split(';'): # parse attributes
                attr,val = s.split('=')
         
                if ',' in val:
                    setattr(self, attr, val.split(','))
         
                else:
                    setattr(self, attr, val)


    def read_gff3(eden, genome):
   
        d = {} # for different types of sliceDBs
        ifile = file(eden)
   
        for line in ifile: # parse all the GFF3 lines
    
            if line.startswith('#'): # ignore this line
               continue
     
            row = GFF3Row(line)
      
            try:
                d.setdefault(row.type, {})[row.ID] = row
                
            except AttributeError:
                pass # no type or ID so ignore...
   
        ifile.close()
   
        annotations = {}
   
        for atype,sliceDB in d.items(): # create annotation DBs
            adb = annotation.AnnotationDB(sliceDB, 'genome')
            annotations[atype] = adb
  
        return annotations


        annots = read_gff3('eden.gff3', 'genome')

        print 'annotation types:', len(annots)

        print 'mRNAs:', len(annots['mRNA'])


if __name__ == "__main__":
    import doctest
    doctest.testmod()


