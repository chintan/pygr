
from pygr import sqlgraph

from pygr.metabase import ManyToManyRelation

from pygr.mapping import Collection

ens_genes = Collection(filename='genes.db', mode='c', itemClass = 'Transcript')

for gene_id, gene_data in geneList:
    gene = Transcript(gene_id, gene_data, ens_genes)
    ens_genes[gene_id] = gene # store in our database


gene_exons = Mapping(ens_genes, exon_db, multiValue=True,
                     inverseAttr='gene_id', filename='gene_exons.db', mode='c')
for exon in exon_db:
    gene = ens_genes[exon.gene_id] # get its gene
    exons = gene_exons.get(gene, []) # get its list of exons, or an empty list
    exons.append(exon) # add our exon to its list
    gene_exons[gene] = exons # save expanded exon mapping list

splicegraph = sqlgraph.SQLGraphClustered('PYGRDB_JAN06.splicegraph_hg17', source_id='left_exon_form_id',
target_id='right_exon_form_id', edge_id='splice_id', sourceDB=exons, targetDB=exons, edgeDB=splices, 
clusterKey='cluster_id')

worldbase.Bio.ASAP2.hg17.splicegraph = splicegraph

worldbase.schema.Bio.ASAP2.hg17.splicegraph = ManyToManyRelation(exons, exons, splices, bindAttrs = ('next', 'previous', 'exons'))

worldbase.commit() # SAVE ALL PENDING DATA TO THE METABASE












