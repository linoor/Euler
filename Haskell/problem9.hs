triplets l = [ [a,b,c] | a <- [3..(l-3) `div` 3], b <- [a+1..(l-1-a) `div` 2], let c = l-a-b, c*c == a*a + b*b]