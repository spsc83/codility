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

# NailingPlanks
You are given two non-empty arrays A and B consisting of N integers. These arrays represent N planks. More precisely, A[K] is the start and B[K] the end of the K−th plank.

Next, you are given a non-empty array C consisting of M integers. This array represents M nails. More precisely, C[I] is the position where you can hammer in the I−th nail.

We say that a plank (A[K], B[K]) is nailed if there exists a nail C[I] such that A[K] ≤ C[I] ≤ B[K].

The goal is to find the minimum number of nails that must be used until all the planks are nailed. In other words, you should find a value J such that all planks will be nailed after using only the first J nails. More precisely, for every plank (A[K], B[K]) such that 0 ≤ K < N, there should exist a nail C[I] such that I < J and A[K] ≤ C[I] ≤ B[K].

For example, given arrays A, B such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10
four planks are represented: [1, 4], [4, 5], [5, 9] and [8, 10].

Given array C such that:

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
if we use the following nails:

0, then planks [1, 4] and [4, 5] will both be nailed.
0, 1, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, 3, then all the planks will be nailed.
Thus, four is the minimum number of nails that, used sequentially, allow all the planks to be nailed.

Write a function:

def solution(A, B, C)

that, given two non-empty arrays A and B consisting of N integers and a non-empty array C consisting of M integers, returns the minimum number of nails that, used sequentially, allow all the planks to be nailed.

If it is not possible to nail all the planks, the function should return −1.

For example, given arrays A, B, C such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..30,000];

each element of arrays A, B and C is an integer within the range [1..2*M];

A[K] ≤ B[K].
* #### Solution:
1 For each plank, try to find the minimum number of nails (n) to hammer this plank.

2 Traverse all the planks, and find the maximum n (maxN).

For Step 1, first look for the smallest position of nails to hammer the plank (p_smallest). 

To do this, C should be sorted with the position (the oraginal index should also be recorded) 

and I will implement binary search. If p_smallest exist, then I need to find the smallest number of nails 

( oraginal index + 1 ) which can hammer the plank.

Because I am looking for the maximum n, for the current plank if there is a number of nails can hammer the

current plank and the number is smaller than the current maxN, there is no necessary to look for the smallest 

number of nails for the current plank. In other words, with the current maximum n, it is enough to hammer this plank. 

```python
def minNailsForPlank(a, b, nails, globalMinNailNum):
    beg = 0
    end = len(nails) - 1
    minNailPosIdx = -1
    NailNum = -1
    while beg <= end:
        mid = int((beg+end)//2)
        if nails[mid][1]<a:
            beg = mid + 1
        elif nails[mid][1]>b:
            end = mid - 1
        else:
            end = mid - 1
            minNailPosIdx = mid
            NailNum = nails[mid][0] + 1
            if NailNum <= globalMinNailNum:
                return NailNum  # It is enough to hammer this plank with number of nails less then globalMinNailNum
    if minNailPosIdx == -1:
        return -1
    minNailNum = nails[minNailPosIdx][0] + 1
    for i in range(minNailPosIdx, len(nails)):
        if nails[i][1] > b:
            break
        if nails[i][0] + 1 < minNailNum:
            minNailNum = nails[i][0] + 1
            if minNailNum <= globalMinNailNum:
                return minNailNum
    return minNailNum
    
def solution(A, B, C):
    nails = sorted(enumerate(C), key=lambda x: x[1])
    minNailNum = -1
    for i in range(len(A)):
        a = A[i]
        b = B[i]
        curr = minNailsForPlank(a, b, nails, minNailNum)
        if curr > 0:
            if curr > minNailNum:
                minNailNum = curr
        if curr < 0:
            return -1
    return minNailNum
```
