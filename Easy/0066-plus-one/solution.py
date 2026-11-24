class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        sdigits = ""
        for i in digits:
            sdigits += str(i)
            number = int(sdigits)
            added_n = number + 1
            s2digits = str(added_n)
            arr = []
            for u in s2digits:
                arr.append(int(u))
        return arr
        
