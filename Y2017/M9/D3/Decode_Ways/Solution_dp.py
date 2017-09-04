# Runtime: 39ms Beats or equals to 90%
check = []


class Solution(object):
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s)==1:
            return 1
        global check
        check = [0] * len(s)
        check[0] = 1
        if s[1]=='0':
            if 0<int(s[:2])<27:
                check[1]=1
        else:
            check[1]=1
            if 0<int(s[:2])<27:
                check[1]+=1
        ptr=2
        while ptr<len(s):
            if 0<int(s[ptr])<27:
                check[ptr]+=check[ptr-1]
            if s[ptr-1]!='0' and 0<int(s[ptr-1:ptr+1])<27:
                check[ptr]+=check[ptr-2]
            ptr+=1
        return check[len(s)-1]


# def numDecodings(self, s):
#     v, w, p = 0, int(s>''), ''
#     for d in s:
#         v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
#     return w



solution = Solution()
print(solution.numDecodings('301'))

