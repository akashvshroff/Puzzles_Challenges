def find_reconstruction(words, match):
    """
    Given a dictionary of words and a string made up of those words (no spaces),
    return the original sentence in a list. If there is more than one possible
    reconstruction, return any of them. If there is no possible reconstruction,
    then return null.
    For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
    string "thequickbrownfox", you should return
    ['the', 'quick', 'brown', 'fox'].
    Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
    string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond]
    or ['bedbath', 'and', 'beyond'].
    """
    seq = []
    temp_word = ''
    for letter in match:
        temp_word += letter
        if temp_word in words:
            seq.append(temp_word)
            words.remove(temp_word)
            temp_word = ''
    if temp_word:  # didn't find the last word
        return None
    else:
        return seq


print(find_reconstruction(['bed', 'bath', 'bedbath', 'and', 'beyond'], 'bedbathandbeyond'))
print(find_reconstruction(['quick', 'brown', 'the', 'fox'], 'thequickbrownfox'))

# now with a word missing
print(find_reconstruction(['quick', 'brown', 'fox'], 'thequickbrownfox'))
