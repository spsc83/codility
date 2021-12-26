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
def solution(N, M):
    ret = set([])
    i = 0
    while i not in ret:
        ret.add(i)
        i = i + M
        if i >= N:
            i = i % N
    return len(ret)
```
But obviousely this algrithm's performance is not good enough.

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

So I am looking for a smallest x make (x - 1) * M % N == 0 where x - 1 > 0 and x - 1 is an integer. 

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
    g = gcd(N, M)
    return int(N / g) 
        
```




