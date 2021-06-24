def find_min_payment(lines):
    """
    MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written.
    They would like to give the smallest positive amount to each worker consistent with the constraint
    that if a developer has written more lines of code than their neighbor, they should receive more money.

    Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.
    For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].
    """
    n = len(lines)
    if n == 1:
        return [1]
    pay = [1 for _ in range(n)]
    for f in range(1, n):  # forward pass
        if lines[f] > lines[f-1]:
            pay[f] = pay[f-1]+1
    for b in range(n-2, -1, -1):  # backward pass
        if lines[b] > lines[b+1]:
            pay[b] = max(pay[b], pay[b+1]+1)
    return pay


print(find_min_payment([10, 40, 200, 1000, 900, 800, 30]))
