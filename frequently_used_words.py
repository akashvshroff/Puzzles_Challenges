from collections import Counter
import re


def top_3_words(text):
    words = re.findall("[\s]?([']?[A-Za-z]+'?[A-Za-z']*)[\s,:]?", text)
    count = Counter()
    for x in words:
        count[x.lower()] += 1
    return [x[0] for x in count.most_common(3)]
