import itertools

def slide(seq, n):
    iters = list(itertools.tee(seq, len(seq)-n+1))
    for i, it in enumerate(iters):
        window = itertools.islice(it, i, n+i)
        yield from window

import sys
exec(sys.stdin.read())