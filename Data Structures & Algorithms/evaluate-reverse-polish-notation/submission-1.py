from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        t = ['+', '*', '-', '/']
        thislist = []
        for i in range(len(tokens)):
            if tokens[i] in t:
                k = int(thislist.pop())
                r = int(thislist.pop())

                if tokens[i] == '+':
                    result = int(r) + int(k)
                elif tokens[i] == '*':
                    result = int(r) * int(k)
                elif tokens[i] == '-':
                    result = int(r) - int(k)
                elif tokens[i] == '/':
                    result = int(r / k)
                thislist.append(int(result))
            else:
                thislist.append(tokens[i])
        return int(thislist.pop())


