##################################################################################################################################################################################
PROBLEM STATEMENT:- Input: a list of sentences(each element may be a word or a sentence), keyword
                    Output: a list that contains the indexes from the input list that contains the keyword I
                   For Example:
                   Input=['I love casino','I went there by a car','Casino was huge grand']
                   Output=[0,2]
##################################################################################################################################################################################
                   
def word_search(doc_list, keyword):
    indices = [] 
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:
            indices.append(i)
    return indices
