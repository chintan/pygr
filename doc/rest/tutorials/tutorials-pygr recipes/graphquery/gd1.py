
from pygr import sqlgraph

from pygr.metabase import ManyToManyRelation

from pygr.mapping import Collection

from load_alignments import * # load the alignments

from pygr.graphquery import * # import the graph query code

# draw a graph using a dict. Note: edge 2->3 must come from swiss_features

queryGraph = {1:{2:None},2:{3:dict(dataGraph=swiss_features)},3:{}}

def main():
    """This function returns the argument.
    Example:
    >>> main()
    4703
    """
# run the query and save the mappings

    l = [dict(d) for d in GraphQuery(mRNA_swiss,queryGraph)]

    print len(l)

if __name__ == '__main__':
        import doctest
        doctest.testmod()








