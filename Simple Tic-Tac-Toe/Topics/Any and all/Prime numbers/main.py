prime_numbers = [i for i in range(2, 1000 + 1) if all(i % j for j in range(2, i))]
