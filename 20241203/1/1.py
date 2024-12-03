import sys
data = sys.stdin.buffer.read()
N = data[0]
tail = data[1:]
L = len(tail)
sys.stdout.buffer.write(bytearray([N]) + b"".join( sorted([tail[round(i * L / N):round((i + 1) * L / N)] for i in range(N)])))
