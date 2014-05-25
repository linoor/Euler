import Data.List

triangleNumbers = [((n+1)*n) `div` 2 | n <- [1..]]

--numberOfDivisors n = (length $ 1 : filter ((==0) . rem n) [2..n `div` 2]) + 1
numberOfDivisors n = product $ map ((+1) . length) (group (primeFactors n))

primes = 2 : [x | x <- [3..], isPrime x]
isPrime x = all (\p -> x `mod` p > 0) (factorsToTry x) where
	factorsToTry x = takeWhile (\p -> p*p <= x) primes

primeFactors n = factor n primes
  where
    factor n (p:ps) 
        | p*p > n        = [n]
        | n `mod` p == 0 = p : factor (n `div` p) (p:ps)
        | otherwise      = factor n ps

problem12 = find ((>=500).numberOfDivisors) triangleNumbers
