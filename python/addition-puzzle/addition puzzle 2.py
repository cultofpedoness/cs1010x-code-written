from itertools import permutations

def addition_puzzle(*args):
    for arg in args[:-1]:
        if len(arg)>len(args[-1]):
            return False
    s = " + ".join(args[:-1]) + "  == " + args[-1]
    chars = set(''.join(args))         # characters to be substituted
    if len(chars) > 10:
        return False
    firsts = set(w[0] for w in args)   # first letters of each of word
    chars = ''.join(firsts) + ''.join(chars - firsts)
    n = len(firsts)                     # chars[:n] cannot be assigned zero
    for perm in permutations('0123456789', len(chars)):
        if '0' not in perm[:n]:
            equation = s.translate(s.maketrans(dict(zip(tuple(chars), perm))))
            try:
                if eval(equation):
                    return dict(zip(tuple(chars), list(map(lambda x: int(x),perm))))
            except ArithmeticError:
                pass
    return False
