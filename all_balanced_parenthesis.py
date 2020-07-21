def balance_parenthesis(str_para):
    """
    Given a string of parenthesis - (),{} or [] - Return whether it is fully
    balanced and correctly oriented or not.
    """
    if not str_para:
        return True
    paren = {'(': ')', '{': '}', '[': ']'}
    curr_stack = [str_para[0]]
    for para in str_para[1:]:
        if not curr_stack or paren[curr_stack[-1]] != para:
            curr_stack.append(para)
        else:
            curr_stack.pop()
    return not len(curr_stack)


print(balance_parenthesis("([])[]({})"))
