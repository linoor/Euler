primes = 2 : [x | x <- [3,5..], isPrime x]

isPrime x = all (\p -> x `mod` p > 0) (factors x) where
	factors x = takeWhile (\p -> p*p <= x) primes