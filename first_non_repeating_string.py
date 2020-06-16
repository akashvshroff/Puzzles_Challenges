def first_non_repeating_letter(string):
    string_lower = string.lower()
    for index, l in enumerate(string_lower):
        if string_lower.count(l) == 1:
            return string[index]
    return ''


print(first_non_repeating_letter(''))
