def fact(x):
    print(x)
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
    
fact(3)

# This looks the same as the Recursion algorithm, can't notice the difference.
# Thus, I guess this means most recursions use stack data structure 