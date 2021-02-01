import string


def column_name(id: int) -> str:
    """
    Spreadsheets often use this alphabetical encoding for its
    columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

    Given a column number, return its alphabetical column id. 
    For example, given 1, return "A". Given 27, return "AA".
    """
    res = []
    if id <= 26:
        return string.ascii_uppercase[id-1]
    while id:
        id, rem = divmod(id, 26)
        if not rem:
            id -= 1
        res.append(string.ascii_uppercase[rem - 1])
    return ''.join(reversed(res))


print(column_name(26))
print(column_name(51))
print(column_name(52))
print(column_name(80))
print(column_name(676))
print(column_name(702))
print(column_name(705))

"""
Z
AY 
AZ 
CB 
YZ 
ZZ 
AAC
"""
