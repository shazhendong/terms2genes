# This python file is used to read the gene set libary.
# Author: Zhendong Sha

def read_Enrichr_Lib(file_name):
    # read the gene set library
    # return the list of terms and the list of gene sets
    with open(file_name) as fi:
        lines = fi.read().splitlines()
    # split line by tab
    list_terms = []
    list_geneSets = []
    for line in lines:
        line = line.split("\t")
        list_terms.append(line[0]) # the first element is the term name
        list_geneSets.append(line[2:-1]) # the rest elements starting from the third are genes till the last-1 in the gene set
    return list_terms, list_geneSets