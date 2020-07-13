def meeting(s):
    # your code
    """
    Take in a string with a list of names - convert to upper case and then sort
    by last name, if last name is first then sort by first name.
    """
    res = ''
    s = s.upper()
    names = s.split(';')
    names_list = []
    for name in names:
        first, last = name.split(':')
        names_list.append((last, first))
    names_list.sort()
    for first, last in names_list:
        res += '{},{}'.format(first, last)
    return res


names = "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
print(meeting(names))
