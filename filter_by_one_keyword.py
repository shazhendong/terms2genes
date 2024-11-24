# This python program extract genes from terms using one keyword.

import sys 
from scr.read_lib import read_Enrichr_Lib
from scr.search import filter_terms_by_keyword

# main function
if __name__ == '__main__':

    # read input arguments
    
    file_path = sys.argv[1] # first argument is the file name of the gene set library
    
    keyword = sys.argv[2] # second argument is the keyword

    # read the gene set library

    list_terms, list_geneSets = read_Enrichr_Lib(file_path) # read the gene set library

    # filter terms by keyword

    index = filter_terms_by_keyword(list_terms, keyword) # filter terms by keyword

    # get unique genes from the matched terms
    genes = []
    for i in index:
        genes += list_geneSets[i]
    genes = list(set(genes)) # get unique genes

    # output result
    
    file_name = file_path.split("/")[-1]
    file_name_prefix = file_name.split(".")[0] + "_" + keyword + "_"

    with open(file_name_prefix + "matched_terms.txt", "w") as f: # output the matched terms to txt
        for i in index:
            f.write(list_terms[i] + "\n")
    f.close()

    with open(file_name_prefix + "matched_genes.txt", "w") as f: # output the matched genes to txt
        for gene in genes:
            f.write(gene + "\n")
    f.close()

