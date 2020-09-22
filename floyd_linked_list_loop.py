def loop_size(node):
    """
    Given a linked list that has a loop in it, find the lenght of the loop.
    See also:
    https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/solutions/python
    """
    rabbit, tortoise = node.next.next, node.next
    while rabbit != tortoise:
        rabbit = rabbit.next.next
        tortoise = tortoise.next
    rabbit = rabbit.next  # now that they are together, increment rabbit
    count = 1  # count how many nodes are passed
    while rabbit != tortoise:
        rabbit = rabbit.next
        count += 1
    return count
