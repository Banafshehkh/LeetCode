class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        symb = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        for i in range(len(s)):
            value = symb[s[i]]

            if i < len(s) - 1 and symb[s[i+1]] > value:
                sum -= value

            else:
                sum += value
            

        return sum



sln = Solution()
result = sln.romanToInt("IXL")
print(result)



