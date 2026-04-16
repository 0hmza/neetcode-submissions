class Solution:
    def isValid(self, s: str) -> bool:
        ferme = [')', '}', ']']
        ouvert = ['(', '{', '[']
        res = []
        for i in s:
            if i in ouvert:
                res.append(i)
            elif i in ferme:
                if not res:
                    return False
                t = res.pop()
                if i == ']' and t != '[':
                    return False
                if i == ')' and t != '(':
                    return False
                if i == '}' and t != '{':
                    return False
        return len(res) == 0   