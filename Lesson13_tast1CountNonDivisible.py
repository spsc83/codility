def solution(A):
    N = len(A)
    num_dict = {}
    for i in A:   # O(N)
        if i not in num_dict:
            num_dict[i] = 1
        else:
            num_dict[i] += 1
    ele2amount_dict = {}
    ret=[]
    for ele in A:  # O(N**1.5)
        if ele in ele2amount_dict:
            ret.append(ele2amount_dict[ele])
            continue
        i = 1
        factorNum = 0
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
