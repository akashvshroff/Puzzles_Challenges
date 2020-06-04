# The idea is to check whether two numbers are the same without using ==
def check_equality(a, b):
    return True if not a ^ b else False


print(check_equality(4, 4))
