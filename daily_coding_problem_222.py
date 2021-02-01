def shortest_path(absolute_path):
    """
    Given an absolute pathname that may have . or .. as
    part of it, return the shortest standardized path.

    For example, given "/usr/bin/../bin/./scripts/../",
    return "/usr/bin/".
    """
    units = absolute_path.split('/')
    stack = []
    for unit in units:
        if unit == '..' and stack:
            stack.pop()
        elif unit != '.':
            stack.append(unit)
    return '/'.join(stack)


print(shortest_path("/usr/bin/../bin/./scripts/../"))
