# AbsDistinct
A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
array A is sorted in non-decreasing order.
* #### Solution:
It is too simple for python. Just use the concept of set.
```python
def solution(A):
    setA = set([])
    for i in A:
        setA.add(abs(i))
    return len(setA)
```
![image](https://github.com/spsc83/codility/blob/main/Lesson15_Caterpiller_method/Screen%20Shot%202022-01-04%20at%2012.13.58%20AM.png)

---
# CountDistinctSlices
An integer M and a non-empty array A consisting of N non-negative integers are given. All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. 

A distinct slice is a slice consisting of only unique numbers. That is, no individual number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:

def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];

M is an integer within the range [0..100,000];

each element of array A is an integer within the range [0..M].
* #### Solution:
Here is the above example:<br>
```
index  0     1     2     3     4
A = [  3,    4,    5,    5,    2  ]
     (0,0) (1,1) (2,2) (3,3) (4,4)
     (0,1) (1,2)       (3,4)
     (0,2) 
num:   3     2     1     2     1     
```
Let's take a look another example:<br>
```
index  0     1     2     3     4     5     6     7
A = [  3,    5,    4,    2,    5,    8,    4,    7  ]
     (0,0) (1,1) (2,2) (3,3) (4,4) (5,5) (6,6) (7,7)
     (0,1) (1,2) (2,3) (3,4) (4,5) (5,6) (6,7)
     (0,2) (1,3) (2,4) (3,5) (4,6) (5,7)
     (0,3)       (2,5) (3,6) (4,7)
                       (3,7)
num:   4     3     4     5     4     3     2     1
```
So the result are the sum of some arithmetic sequences. The common difference is -1.

For a arithmetic sequence:
```
sum of arithmetic sequence = (first_element + last_element)*count/2 
```
For the second example, [num[0], num[1]] is an arithmetic sequence. The first element num[0] is 4. 

It is the length of the caterpillar's body. The caterpillar's tail and head are initialized as 0.

I need to increase the head until I meet a duplicate value (A[4]). Then I will calculate the sum

of the arithmetic sequence. The first element of the arithmetic sequence is head - tail = 4 - 0 = 4. 

The count of the arithmetic sequence depends on the position of the duplicated value (A[1]) in the 

body (A[0]~A[3]). 

```
(last_element - first_element)/common_difference + 1 = count  and  common_difference=-1
last_element = first_element - count + 1
```
So now I can get the sum of the first arithmetic sequence. Then I need to increase the tail of the caterpillar

by count (from 0 to 2), and continue increasing the head until meet another duplicate value (A[6]), then calculate

the sum of the next arithmetic sequence, so on and so for.

When the caterpillar's head reach the last element of A, there is a last arithmetic sequence (num[3] ~ num[7]) left.

```python
def solution(M, A):
    ret = 0
    tail = 0
    body_dict = {} # To record the position of the duplicate element in body
    for head in range(len(A)):
        # Here is the trick to get 100 performance score. Use dict or set instead of list.
        if A[head] in body_dict:  
            first = head - tail
            # If you use set, you also need to record a body list to calculate count.
            count = body_dict[A[head]] - tail + 1
            last = first - count + 1
            ret += (first + last) * count / 2
            if ret > 1000000000:
                return 1000000000
            for i in range(count):
                body_dict.pop(A[tail + i])
            tail = tail + count
        body_dict[A[head]] = head
    ret += (len(A) - tail + 1)*(len(A) - tail)/2 # the last arithmetic sequence 
    if ret > 1000000000:
        return 1000000000
    return int(ret)
```
![image](https://github.com/spsc83/codility/blob/main/Lesson15_Caterpiller_method/Screen%20Shot%202022-01-04%20at%2012.06.58%20AM.png)

---

# CountTriangles
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
There are four triangular triplets that can be constructed from elements of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the number of triangular triplets in this array.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000];

each element of array A is an integer within the range [1..1,000,000,000].

* #### Solution:
This is the same as the exercise in the reading material.

The only difference is this time A is unsorted. So I sort A first.

Then I implemanted the caterpillar method. For the indexs p, q, r (p<q<r),

if A[p] + A[q] > A[r], (p, q, r) is a triplet. To find triplet, for a fixed p 

and q, I will find the smallest r make A[r]>=A[p] + A[q] first time. Then r in 

[q + 1, r - 1] can make triplets. The number of triplets is:
```
r - 1 - (q + 1) + 1 = r - q - 1
```
Then I will increase q. Here is something important:
```
array A (sorted):     p -------- q, q+1 --------- r-1, r----------
If A[p] + A[q] > A[r-1], then A[p] + A[q+1] > A[r-1]. So there is no need to check 
r in [q+2, r-1].
```
---
```python 
def solution(A):
    A.sort()
    ret = 0
    for p in range(len(A) - 2):
        r = p + 2
        for q in range(p + 1, len(A)-1):
            while r<len(A) and A[p] + A[q]> A[r]:
                r += 1
            ret += r - q - 1
    return ret
```
![image](https://github.com/spsc83/codility/blob/main/Lesson15_Caterpiller_method/Screen%20Shot%202022-01-04%20at%202.23.28%20PM.png)

---

# MinAbsSumOfTwo

Let A be a non-empty array consisting of N integers.

The abs sum of two for a pair of indices (P, Q) is the absolute value |A[P] + A[Q]|, for 0 ≤ P ≤ Q < N.

For example, the following array A:

  A[0] =  1
  A[1] =  4
  A[2] = -3
has pairs of indices (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2). 
The abs sum of two for the pair (0, 0) is A[0] + A[0] = |1 + 1| = 2. 
The abs sum of two for the pair (0, 1) is A[0] + A[1] = |1 + 4| = 5. 
The abs sum of two for the pair (0, 2) is A[0] + A[2] = |1 + (−3)| = 2. 
The abs sum of two for the pair (1, 1) is A[1] + A[1] = |4 + 4| = 8. 
The abs sum of two for the pair (1, 2) is A[1] + A[2] = |4 + (−3)| = 1. 
The abs sum of two for the pair (2, 2) is A[2] + A[2] = |(−3) + (−3)| = 6. 

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the minimal abs sum of two for any pair of indices in this array.

For example, given the following array A:

  A[0] =  1
  A[1] =  4
  A[2] = -3
the function should return 1, as explained above.

Given array A:

  A[0] = -8
  A[1] =  4
  A[2] =  5
  A[3] =-10
  A[4] =  3
the function should return |(−8) + 5| = 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];

each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

* #### Solution:

The abs sum of two must be bigger or equal to 0 always. So 0 is the possible minimal value. For example |-4 + 4|.

If all elements are positive or negative the question would be very easy. 

If there is only 1 element in the array, the question would be even more easy:)

If partial elements are negative and partial elements are positive, that is the case we should consider.

First I sorted the array. The negative pointer (pn) point to the most left element. The positive pointer (pp)

point to the most right element.
```
A = [  -10    -8    3    4    5  ]
       pn                     pp 
```
If abs(A[pn]) > abs(A[pp]) I will move pn to the right to make the abs sum smaller.

If abs(A[pp]) > abs(A[pn]) I will move pp to the left to make the abs sum smaller.

If abs(A[pn]) == abs(A[pp]) I got the global smallest abs sum. In this case, I should return directly.

In the whold above process I will record the smallest abs sum.

```python
def solution(A):
    if len(A) == 1:
        return 2 * abs(A[0])
    A.sort()
    pn = 0
    pp = len(A) - 1
    if A[0] >= 0:
        return A[0] * 2
    if A[-1] <= 0:
        return abs(A[-1] * 2)
    ret = abs(A[pn] + A[pp])
    while A[pn] <= 0 and A[pp] > 0:
        if abs(A[pn]) > abs(A[pp]):
            pn += 1
            curr_abs_sum = abs(A[pn] + A[pp])
            if curr_abs_sum < ret:
                ret = curr_abs_sum
        elif abs(A[pn]) == abs(A[pp]):
            return 0
        else:
            pp -= 1
            curr_abs_sum = abs(A[pn] + A[pp])
            if curr_abs_sum < ret:
                ret = curr_abs_sum
    return ret
```

![image](https://github.com/spsc83/codility/blob/main/Lesson15_Caterpiller_method/Screen%20Shot%202022-01-07%20at%2012.16.27%20PM.png)
