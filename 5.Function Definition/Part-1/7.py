def calSq(n):
  return n*n


nums = (1, 2, 3, 4)
res = map(calSq, nums)
numSq = set(res)
print(numSq)