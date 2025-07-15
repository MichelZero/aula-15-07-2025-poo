##
# autor: Michel
# data: 15/07/2025
#
#

# fatorial
# 0! = 1
# 1! = 1 x 0! = 1
# 2! = 2 x 1! = 2 x 1 x 0! = 2
# 3! = 3 x 2! = 3 x 2 x 1 x 0! = 6
# 4! = 4 x 3! = 4 x 3 x 2 x 1 x 0! = 24
# 5! = 5 x 4! = 5 x 4 x 3 x 2 x 1 x 0! = 120

# f(x)! = x * (x -1)!
            # f(x-1)!

def fatorial(x):
  if x == 0:
    return 1
  else:
    return x * fatorial(x-1)


# 
for i in range(10):
  print(fatorial(i))  