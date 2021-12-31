# MinMaxDivision
You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
The array can be divided, for example, into the following blocks:

[2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
[2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
[2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
[2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function:

def solution(K, M, A)

that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and K are integers within the range [1..100,000];
M is an integer within the range [0..10,000];
each element of array A is an integer within the range [0..M].

* #### Solution:
If I have a large sum l, there should be only 1 way to divide the array to have the minimal block number k.

In other words, I need to divide the array in to at least k blocks to have the large sum l.

For example:

A = [2, 1, 5, 1, 2, 2, 2], l = 6 , The way to divide the array is: 2, 1    5, 1    2, 2, 2  

So I at least need to divide A in to 3 blocks. k = 3.

The l and k have a kind of relation. If l goes bigger, k gose smaller, vice versa. In particular, if l = sum(A) then k=1. 

l's value is in region [max(A), sum(A)].

So I can implement binary search for l. And I also need a function to transform l to k. If k is bigger than the target k, then l should be increased, vice versa.

```python
def check(A, large_sum):
    block = 0
    block_sum = 0
    for i in A:
        if block_sum + i > large_sum:
            block += 1
            block_sum = 0
        block_sum += i
    return block + 1


def solution(K, M, A):
    beg = max(A)
    end = sum(A)
    result = -1
    while beg <= end:
        mid = int((beg + end) // 2)
        if check(A, mid) > K:
            beg = mid + 1
        else:
            end = mid - 1
            result = mid
    return result
```
![image](https://github.com/spsc83/codility/blob/main/Lesson14_Binary_search_algorithm/Screen%20Shot%202021-12-31%20at%204.13.02%20PM.png)
