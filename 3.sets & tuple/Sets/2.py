primes={3,5,7,11};
print(primes)

primes.add(19);
print(primes)

plist=[12,14,15,16];
primes.update(plist);
print(primes)

primes.discard(34)  # Not Error
primes.discard(12);

primes.remove(11);
primes.remove(30);  # Error
primes.clear()
