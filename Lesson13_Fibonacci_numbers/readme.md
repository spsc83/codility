 # FibFrog
 The Fibonacci sequence is defined using the following recursive formula:

    F(0) = 0
    F(1) = 1
    F(M) = F(M - 1) + F(M - 2) if M >= 2
A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position −1) and wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of the bank at position N.

The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent consecutive positions from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:

0 represents a position without a leaf;
1 represents a position containing a leaf.
The goal is to count the minimum number of jumps in which the frog can get to the other side of the river (from position −1 to position N). The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.

For example, consider array A such that:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the minimum number of jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.

For example, given:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.


* #### Solution:
Consider the 2 banks are 2 leaves. So the frog is on the first leaf, and it needs to jump to the last leaf. 

So first I will collect fibonacci numbers which are smaller than N + 2 (The last leaf's index is N + 1). 

To know the minimum jumps to reach a particular leaf (T),

you need to know all the minimun jumps to reach the previous leaves. Then you should try all the fibonacci numbers,

to see 

1 if the frog can jump from a previous leaf (P) to T, with a fibonacci number

2 if the previous leaf (P) can be reached

Then update the T's minimum jump number. 

For the first leaf, the minimum jump number is 0 (The frog begins from the first leaf). 

Then try it for the second leaf, so on and so far.

```python
def fib(n):
    fib_list = [1, 1]  # the frog need to jump, so exclude 0.
    while fib_list[-1] + fib_list[-2] <= n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


def solution(A):
    A = [1] + A + [1]
    length = len(A)
    fib_list = fib(length-1)
    min_jump_list = [length] * length
    min_jump_list[0] = 0
    for idx in range(1, length):
        if A[idx] == 0:
            continue
        for jump in fib_list:
            left_leaf_idx = idx - jump
            if left_leaf_idx >= 0:
                if A[left_leaf_idx] == 1 and min_jump_list[left_leaf_idx] != length and min_jump_list[left_leaf_idx] + 1 < min_jump_list[idx]:
                    min_jump_list[idx] = min_jump_list[left_leaf_idx] + 1
            else:
                break
    if min_jump_list[-1] < length:
        return min_jump_list[-1]
    else:
        return -1
```
![image](https://github.com/spsc83/codility/blob/main/Lesson13_Fibonacci_numbers/Screen%20Shot%202021-12-30%20at%2010.53.18%20AM.png)



* #### BFS solution (performance not good):

Everyone said BFS abount this question. I tried BFS, but the performance is not good enough. I will appreciate it if anyone can tell me what I did wrong.

![image](https://github.com/spsc83/codility/blob/main/Lesson13_Fibonacci_numbers/Screen%20Shot%202021-12-30%20at%2010.57.00%20AM.png)

```python
def fib(n):
    ret=[1,1]
    while ret[-1] + ret[-2]<=n:
        ret.append(ret[-1] + ret[-2])
    return ret

def solution(A):
    A = [1] + A + [1]
    fib_list = fib(len(A)-1)
    lengthA = len(A)
    queue = [[0,0]]
    
    while len(queue) > 0:
        curr_node, counter = queue.pop(0)
        for f in fib_list:
            next_idx = curr_node + f
            if next_idx >= lengthA:
                break
            if next_idx == lengthA - 1:
                return counter + 1
            if A[next_idx] == 1:
                queue.append([next_idx, counter + 1]) 
    return -1
```


 # Ladder
 You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:

with your first step you can stand on rung 1 or 2,
if you are on rung K, you can move to rungs K + 1 or K + 2,
finally you have to stand on rung N.
Your task is to count the number of different ways of climbing to the top of the ladder.

For example, given N = 4, you have five different ways of climbing, ascending by:

1, 1, 1 and 1 rung,
1, 1 and 2 rungs,
1, 2 and 1 rung,
2, 1 and 1 rungs, and
2 and 2 rungs.
Given N = 5, you have eight different ways of climbing, ascending by:

1, 1, 1, 1 and 1 rung,
1, 1, 1 and 2 rungs,
1, 1, 2 and 1 rung,
1, 2, 1 and 1 rung,
1, 2 and 2 rungs,
2, 1, 1 and 1 rungs,
2, 1 and 2 rungs, and
2, 2 and 1 rung.
The number of different ways can be very large, so it is sufficient to return the result modulo 2P, for a given integer P.

Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2^B[I].

For example, given L = 5 and:

    A[0] = 4   B[0] = 3
    A[1] = 4   B[1] = 2
    A[2] = 5   B[2] = 4
    A[3] = 5   B[3] = 3
    A[4] = 1   B[4] = 1
the function should return the sequence [5, 1, 8, 0, 1], as explained above.

Write an efficient algorithm for the following assumptions:

L is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..L];
each element of array B is an integer within the range [1..30].

* #### Solution:
1 Since you can only ascend by 1 or 2 rungs, there are only 2 "way"s to stand on rung N.

N - 1  ---->  N

N - 2  ---->  N

Let's say the ways to climb to rung N is W(n). It is obviously W(n) = W(n-1) + W(n-2). 

The base cases are W(1) = 1, W(2) = 2. So they are Fibonacci numbers.

It is better to store the Fibonacci numbers somewhere. In my case, I use a list to store it.

2 Here is another trick:

"the number of different ways of climbing the ladder with A[I] rungs modulo <strong>2^B[I]</strong>"

Since the base number is 2, it is better to use bitwise operation instead of "%".

```python
def ways(n, mem):
    while len(mem) - 1 < n:
        mem.append(mem[-1] + mem[-2])
    return mem[n]

def solution(A, B):
    mem = [0, 1, 2] # The value of mem[0] is useless. The element of A is larger than 0.
    ret = []
    for i in range(len(A)):
        a = A[i]
        b = B[i]
        w = ways(a, mem)
        w2 = w>>b<<b
        ret.append(w - w2)
    return ret
```
![image](https://github.com/spsc83/codility/blob/main/Lesson13_Fibonacci_numbers/Screen%20Shot%202021-12-30%20at%2012.18.51%20PM.png)
