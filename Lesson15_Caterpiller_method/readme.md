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
