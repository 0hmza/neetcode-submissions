class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        stack: list[str] = []

        if len(digits) == 1:
            return phone[digits]
        p = []
        for num in digits:
            if num in phone.keys():
                p.append(phone[num])
        res = p[0]
        new_list = []
        i = 1
        while i < len(p):
            new_list = []
            j = 0
            while j < len(res):
                k = 0
                while k < len(p[i]):
                    new_list.append(res[j] + p[i][k])
                    k += 1
                j += 1
            res = new_list
            i += 1
        return new_list