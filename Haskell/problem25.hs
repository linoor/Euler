digs :: Integral x => x -> [x]
digs 0 = []
digs x = digs (x `div` 10) ++ [x `mod` 10]

fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

problem25 = last (takeWhile (<10^1000) fibs)