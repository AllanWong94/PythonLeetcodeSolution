from itertools import zip_longest
class Solution(object):
    # Runtime: 432ms Beats or equals to 43%
    def multiply(self, num1, num2):
        result='0'
        if num1=='0' or num2=='0': return result
        scale=0
        for i in num1[::-1]:
            temp=self.multiplyby1digit(i,num2)
            for j in range(scale):
                temp+='0'
            result=self.add(result,temp)
            scale+=1
        return result
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

    def multiplyby1digit(self,num, longNum):
        carry=0
        res=[]
        n=ord(num)-ord('0')
        temp=longNum[::-1]
        for i in temp:
            multiRes=n*(ord(i)-ord('0'))+carry
            res.append(str(multiRes%10))
            carry=multiRes//10
        if carry>0:
            res.append(str(carry))
        return ''.join(res[::-1])

    def add(self,num1,num2):
        carry=0
        res=[]
        z=zip_longest(num1[::-1],num2[::-1],fillvalue='0');
        carry, zero2, res=0,2*ord('0'),[]
        for i in z:
            sum=ord(i[0])+ord(i[1])+carry-zero2
            res.append(str(sum%10))
            carry=sum//10
        return ('1' if carry else '')+''.join(res[::-1])



obj=Solution()
print(obj.multiply("9","9"))
