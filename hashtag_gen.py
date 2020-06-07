def generate_hashtag(s):
    res = '#'
    if not s:
        return False
    words = s.split()
    for word in words:
        res += word.capitalize()
    return res if len(res) <= 140 else False


print(generate_hashtag('codeWars  is  nice'))
