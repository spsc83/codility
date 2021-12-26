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
  
![image](https://github.com/spsc83/codility/blob/main/Lesson11_Sieve_of_Eratosthenes/Screen%20Shot%202021-12-19%20at%2011.51.26%20PM.png)

# CountSemiprimes
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:

def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P and Q is an integer within the range [1..N];
P[i] ≤ Q[i].


* #### I found 2 solutions for this question:
### Solution 1:
1 Find the prime numbers from 1 to N using sieve method.
2 Find the semiprime number from 1 to N using the prime numbers found in step 1.
3 Calculate the prefix sum to accelerate the random slice
4 Calculate the result with P, Q and prefix sum

 ```python
 def solution(N, P, Q):
    if N < 4:
        return [0]*(len(P))
    prime = [1] * (N+1)
    prime[0] = prime[1] = 0
    for i in range(2,int(N**0.5)+1):
        k = i*i
        while k <= N:
            if prime[k] == 1:
                prime[k] = 0
            k = k + i
    semi_prime = [0] * (N + 1)
    for i in range(1, N+1):
        if prime[i] != 1:
            continue
        for j in range(i, N+1):
            if prime[j] !=1:
                continue
            product = i*j
            if product <= N:
                semi_prime[product] = 1
            else:
                break # Here is the magic to save the performance score! 
                #The rest 'j's are all bigger than the current 'j'. Not necessary to check the rest.
    prefix_sum = [0] * (N+1)
    for i in range(1,N+1):
        prefix_sum[i] = prefix_sum[i-1] + semi_prime[i]
    ret = []
    for i in range(len(P)):
        p = P[i]
        q = Q[i]
        ret.append(prefix_sum[q] - prefix_sum[p - 1])
    return ret
 ```
 ### Solution 2:
 Since semiprime number is the product of 2 prime numbers. So the two prime numbers are 2 factors of this semiprime number. So the factors of this semiprime number should be 1, prime number 1, prime number 2 and semiprime number. In particular case, prime number 1 == prime number 2, the factors of this semiprime number should be 1, prime number 2 and semiprime number.<br>
 Semiprime numbers should have 4 or 3 factors. For example, 4's factors are 1, 2, 4. And 6's factors are 1, 2, 3, 6. <br>
 But not all the numbers with 4 factors are semiprime numbers. For example, 8's factors are 1, 2, 4, 8. And 8 is not semiprime. In this case, the third factor is the second factor's square.
1 Find the semiprime numbers from 1 to N according the above discription(lesson 10).
2 Calculate the prefix sum to accelerate the random slice
3 Calculate the result with P, Q and prefix sum
 ```python
 def solution(N, P, Q):
    if N<4:
        return [0]*len(P)
    semi_prime =[0] * (N+1)
    for i in range(1, N+1):
        factor_num = 0
        flag = False
        for f1 in range(1,int(i**0.5)+1):
            if i % f1 == 0:
                factor_num += 1
                f2 = i / f1
                if f2 != f1:
                    factor_num += 1
                    if f2 == f1**2:
                        flag = True
                        break
                if factor_num >4: # Here is the magic to save the performance score!
                #You don't need to know the exact number of factors. You just need to know the number of factor is bigger than 4.
                    flag = True
                    break
        if not flag and factor_num<5 and factor_num>2:
            semi_prime[i] = 1

    prefix = [0]*(N+1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + semi_prime[i]
    
    result_list = [] 
    for i, j in zip(P, Q):
        result_list.append(prefix[j] - prefix[i-1])
    return result_list
 ```
![image](https://github.com/spsc83/codility/blob/main/Lesson11_Sieve_of_Eratosthenes/Screen%20Shot%202021-12-26%20at%203.39.14%20PM.png)
