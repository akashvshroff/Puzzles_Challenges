def simple_assembler(program):
    """
    See also: https://www.codewars.com/kata/58e24788e24ddee28e000053/train/python
    A fun programming challenge to write a python program to parse interpreter instructions.
    """
    reg = {}
    i = 0
    while i < len(program):
        cmd, var, val = (program[i] + ' 0').split()[:3]
        if cmd == 'inc':
            reg[var] += 1
        elif cmd == 'dec':
            reg[var] -= 1
        elif cmd == 'mov':
            reg[var] = reg[val] if val in reg else int(val)
        elif cmd == 'jnz' and (reg[var] if var in reg else int(var)):
            i += int(val)
            continue
        i += 1
    return reg
