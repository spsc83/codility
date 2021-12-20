# CountNonDivisible
You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N].


* #### Here is the solution I found:
Take a look at A[0] and A[3]. They have the same value which is 3. And they have the same amount of non-divisors. <br>
So I do not need to calculate the amount of non-divisors for 3 the second time. What I need to do is just to record the result in a dict.<br>
1 Record all the count of elements of array A in num_dict.<br>
2 For every element in A if this element has been handled before, get the result from the dict. <br>
  If it is a new element, calculate all the factor of this element (Lesson 10). For each factor update the amount of divisors with num_dict.<br>
  The amout of non-divisors = the length of array - the amount of divisors<br>
 
 ```python
 def solution(A):
    N = len(A)
    num_dict = {}
    for i in A:  
        if i not in num_dict:
            num_dict[i] = 1
        else:
            num_dict[i] += 1
    ele2amount_dict = {}
    ret=[]
    for ele in A:  
        if ele in ele2amount_dict:
            ret.append(ele2amount_dict[ele])
            continue
        factorNum = 0
        
        # Here is something tricky. Do not use the while loop.  It is not as efficient as the for loop.
        # i = 1
        # while i*i < ele:
        #     if ele % i == 0:
        #         otherFactor = int(ele/i)
        #         if i in num_dict:
        #             factorNum += num_dict[i]
        #         if otherFactor in num_dict:
        #             factorNum += num_dict[otherFactor]
        #     i += 1
        # if i*i == ele:
        #     if i in num_dict:
        #         factorNum += num_dict[i]
        for i in range(1,int(ele**0.5)+1):
            if ele % i == 0:
                otherFactor = int(ele/i)
                if i in num_dict:
                    factorNum += num_dict[i]
                if otherFactor != i:
                    if  otherFactor in num_dict:
                        factorNum += num_dict[otherFactor]

        ret.append(N - factorNum)
        ele2amount_dict[ele] = ret[-1]
    return ret
 ```
  
