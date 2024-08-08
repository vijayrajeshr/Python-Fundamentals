def is_prime(n):
  if n < 2:
    return False  # Not prime
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False  # Not prime
  return True  # Prime

for n in range(1, 21):
  if is_prime(n):
    print(n)
