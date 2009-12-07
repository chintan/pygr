from pygr import seqdb, metabase, worldbase

from pygr.downloader import SourceURL

from pygr.nlmsa_utils import NLMSABuilder

import os
# WORLDBASEPATH: '.,http://biodb2.bioinformatics.ucla.edu:5000'
# WORLDBASEPATH has one writable location: '.', current directory
os.environ['WORLDBASEPATH'] = '.,http://biodb2.bioinformatics.ucla.edu:5000'

from pygr import metabase
mdb = metabase.MetabaseList()

print mdb.dir() # Print all XMLRPC resources
print mdb.dir(download=True) # Print all downloadable resources

bosTau4 = mdb('Bio.Seq.Genome.COW.bosTau4')

bosTau4_multiz4way = mdb('Bio.MSA.UCSC.bosTau4_multiz4way')
