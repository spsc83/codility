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
