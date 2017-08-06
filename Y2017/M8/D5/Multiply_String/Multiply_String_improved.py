class Solution(object):
    #Runtime: 128ms Beats or equals to 82% without using int()!
    def multiply(self, num1, num2):
        if num1 is '0' or num2 is '0': return '0'
        l1,l2,zero=len(num1),len(num2),ord('0')
        num1=num1[::-1]
        num2=num2[::-1]
        num3=[0 for _ in range(l1+l2)]
        for i in range(l1):
            for j in range(l2):
                num3[i+j]+=(ord(num1[i])-zero)*(ord(num2[j])-zero)
        carry=0
        for i in range(l1+l2-1):
            carry,num3[i]=num3[i]//10,str(num3[i]%10)
            num3[i+1]+=carry
        num3=[str(num3[l1+l2-1-i]) for i in range(l1+l2)]
        res=''.join(num3).lstrip('0')
        return ('0' if not res else res)

    # def multiply(self, num1, num2):
    #     """
    #     :type num1: str
    #     :type num2: str
    #     :rtype: str
    #     """
    #
    #     l1 = len(num1)
    #     l2 = len(num2)
    #     num1 = [int(num1[l1 - i - 1]) for i in range(l1)]
    #     num2 = [int(num2[l2 - i - 1]) for i in range(l2)]
    #     l3 = l1 + l2
    #     num3 = [0 for _ in range(l3)]
    #     for i in range(l1):
    #         for j in range(l2):
    #             num3[i + j] += num1[i] * num2[j]
    #     for i in range(l3 - 1):
    #         carry, num3[i] = num3[i] / 10, num3[i] % 10
    #         num3[i + 1] += carry
    #     num3 = [str(num3[l3 - 1 - i]) for i in range(l3)]
    #     num3 = ''.join(num3)
    #     return str(int(num3))

        """
        :type num1: str
        :type num2: str
        :rtype: str
        """


obj=Solution()
print(obj.multiply('25','14'))