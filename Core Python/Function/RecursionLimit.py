import sys
print(sys.getrecursionlimit())  # Get Recursion Limit ( BY Default Limit is 1000)
sys.setrecursionlimit(4000)     # here we change Manualy Limit as we want
print(sys.getrecursionlimit())  # modified Limit 