c = 0


def hanoi(n, source, helper, target):
    global c
    if n > 0:
        hanoi(n - 1, source, target, helper)
        c += 1
        if source:
            target.append(source.pop())
        hanoi(n - 1, helper, source, target)


source, target, helper = [4, 3, 2, 1], [], []

hanoi(len(source), source, helper, target)
print(target, c)
