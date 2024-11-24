# This python file is used to subset term names by keywords.
# Author: Zhendong Sha

def filter_terms_by_keyword(list_terms, keyword):
    # return the index of the terms that contain the keyword
    return [i for i, term in enumerate(list_terms) if keyword in term]