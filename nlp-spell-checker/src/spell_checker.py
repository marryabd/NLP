from src.edit_distance import min_edit_dist

def correct_word(input_word, dictionary, topk=1):
    """
    Find the closest matching word(s) from the dictionary based on edit distance.

    Args:
        input_word (str): the word to correct
        dictionary (list of str): list of valid words
        topk (int): how many suggestions to return

    Returns:
        List of (word, distance) tuples sorted by distance
    """
    # lowercasing everything
    input_word = input_word.lower()

    # compute (word, distance) for each word
    candidates = []
    for dict_word in dictionary:
        dist = min_edit_dist(input_word, dict_word)
        candidates.append((dict_word, dist))
    # sort by distance
    candidates.sort(key=lambda x: x[1])

    # return top-k
    return candidates[:topk]