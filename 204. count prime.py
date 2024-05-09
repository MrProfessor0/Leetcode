# This have Big of O(n^2) complexity
# def countPrimes(n: int):
#     if n<2:
#         return 0
#     if n == 2:
#         return 1

#     count = 1
    
#     for num in range(3,n,2):
#         flag = True
#         for i in range(2,num):
#             if num % i == 0:
#                 flag = False
#         if flag:
#             count += 1

#     return count




# Algorithm Sieve of Eratosthemes 
def countPrimes(n: int):
    if n<=2:
        return 0
    # if n == 2:
        # return 1

    count = 1
    prime = [True] * (n+1)
    prime[0] = prime[1] = False

    for i in range(3,n):
        if prime[i]:
            count += 1
            for j in range(i*2,n,i):
                prime[j] = False

    return count


print(countPrimes(n=10))