# ChocolatesByNumbers
Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:

def solution(N, M)

that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..1,000,000,000].

* #### Bad solution:
It is very easy to simulate the process.
```python
def solution(N, M): # This is the first thing come into my mind.
# But obviousely this algrithm's performance is not good enough.
    ret = set([])
    i = 0
    while i not in ret:
        ret.add(i)
        i = i + M
        if i >= N:
            i = i % N
    return len(ret)
```

* #### Good solution:
Here are two facts:

1 If he eat x times the position is (x-1) * M % N.

Before the second fact, Let's take a look at some examples:

N = 10, M = 1: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0

N = 10, M = 2: 0, 2, 4, 6, 8, 0

N = 10, M = 3: 0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0

N = 10, M = 4: 0, 4, 8, 2, 6, 0

N = 10, M = 5: 0, 5, 0

N = 10, M = 6: 0, 6, 2, 8, 4, 0

2 They all stop eating when they encounter an empty wrapper at position 0!

So I am looking for a smallest x to make (x - 1) * M % N == 0 where x - 1 > 0 and x - 1 is an integer. 

Oberviously, x - 1 = N can fit the equeition. But it is not the smallest because M and N may have common divisor. So we should reduce the fraction first. Then 

x - 1 equals the denominator which is N / gcd(M, N). So x = N / gcd(M, N) + 1. Since the last time he encounter an empty wrapper. So the chocolate number is 

x - 1 = N / gcd(M, N).

```python
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
def solution(N, M):
    return int(N / gcd(N, M)) 
        
```


![image](https://github.com/spsc83/codility/blob/main/Lesson12_Euclidean_algorithm/Screen%20Shot%202021-12-26%20at%206.30.29%20PM.png)

# CommonPrimeDivisors

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

N = 15 and M = 75, the prime divisors are the same: {3, 5};
N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

Z is an integer within the range [1..6,000];
each element of arrays A and B is an integer within the range [1..2,147,483,647].


* #### Solution:
For every corresponding a in A and b in B, I can get the gcd of a and b. Let's say it is g. The statement, a and b have the same prime divisor set equals to a's prime divisor set is in g's prime divisor set and b's prime divisor set is also in g's prime divisor set.

The statement, a's prime divisor set is in g's prime divisor set equals to a == 1 or a > 1 and (gcd(a, g)>1 and (a / gcd(a, g))'s prime divisor set should also in g's prime divisor set).

```python
def gcd(a, b):
    if a % b==0:
        return b
    return gcd(b, a % b)
def judge(a, b): # to see if a's prime divisor set is in b's
    if a == b:
        return True
    g = gcd(a, b)
    while a != 1 and g != 1:
        a = int(a / g)
        g = gcd(a, b)
    return a == 1
def solution(A, B):
    ret = 0
    for i in range(len(A)):
        a = A[i]
        b = B[i]
        if a == b:
            ret += 1
            continue
        g = gcd(a, b)
        if judge(a, g) and judge(b, g):
            ret += 1
    return ret
```


![image](https://github.com/spsc83/codility/blob/main/Lesson12_Euclidean_algorithm/Screen%20Shot%202021-12-28%20at%202.01.39%20PM.png)
