def factorial(n):
    fact=0
    if n==0 or n==1:
        fact=1
        
    elif n> 1:
        fact= n * factorial(n-1)
    
    return fact


print(factorial(4))