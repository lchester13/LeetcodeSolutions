


class Solution:

    #20. Valid Parentheses
    def isValid(s):
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
                print('stack line 13:', stack)
            elif ch in ")}]":
                if not stack:
                    return False
                else:
                    stack.pop()
                print('stack line 16', stack)
        return True
        



    s = "()"
    s2 = "()[]{}"
    s3 = "(]"
    isValid(s3)





        