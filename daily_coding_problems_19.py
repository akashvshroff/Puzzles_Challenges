def find_min_cost(cost_matrix):
    """
    A builder is looking to build a row of N houses that can be of K different
    colors. He has a goal of minimizing cost while ensuring that no two
    neighboring houses are of the same color.

    Given an N by K matrix where the nth row and kth column represents the cost
    to build the nth house with kth color, return the minimum cost which achieves
    this goal.

    A DP question where you can build a resultant cost matrix that calculates
    the min the cost so far.
    """
    if not cost_matrix:
        return 0
    n = len(cost_matrix)
    k = len(cost_matrix[0])
    res_cost_matrix = [[0 for i in range(k)] for j in range(n)]
    res_cost_matrix[0] = cost_matrix[0]
    for i in range(1, n):
        for j in range(k):
            res_cost_matrix[i][j] = cost_matrix[i][j] + \
                min((res_cost_matrix[i-1][a] for a in range(k) if a != j))

    return min(res_cost_matrix[-1])


cost = [[7, 3, 8, 6, 1, 2],
        [5, 6, 7, 2, 4, 3],
        [10, 1, 4, 9, 7, 6],
        [10, 1, 4, 9, 7, 6]]
print(find_min_cost(cost))
