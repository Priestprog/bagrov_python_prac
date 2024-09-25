M, N = eval(input())
print([el for el in range(M,N) if all(el % k for k in range(2,el))])