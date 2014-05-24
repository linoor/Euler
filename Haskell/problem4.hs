isPalindrome w = w == reverse w

digs 0 = []
digs x = digs (x `div` 10) ++ [x `mod` 10]

products = [product | x <- [100..999], y <- [x..999], let product = x*y, isPalindrome $ digs product]

problem_4 = maximum products