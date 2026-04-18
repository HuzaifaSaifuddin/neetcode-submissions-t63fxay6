class Solution:
    def isValid(self, s: str) -> bool:
        arr = []

        bracketList = list(s)

        for bracket in bracketList:
            if bracket == '(':
                arr.append(bracket)
            elif bracket == '[':
                arr.append(bracket)
            elif bracket == '{':
                arr.append(bracket)
            elif bracket == ')':
                if not arr or arr[-1] != '(':
                    return False
                else:
                    arr.pop()
            elif bracket == ']':
                if not arr or arr[-1] != '[':
                    return False
                else:
                    arr.pop()
            elif bracket == '}':
                if not arr or arr[-1] != '{':
                    return False
                else:
                    arr.pop()
        
        return not arr
            