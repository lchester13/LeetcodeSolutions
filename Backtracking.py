
class LeetCodeSolutions:
    
    # 17. Letter Combinations of a Phone Number

    def letterCombinations(digits):
        output = []
        numDict = {
            '2': 'abc',
            '3': 'def',
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                output.append(currStr) # adding a new letter combination to output list 
                return
            
            for ch in numDict[digits[i]]:
                backtrack(i+1, currStr+ch)
            
        if digits:
            backtrack(0, "")
        
        return output

    # 22. Generate Parentheses
    def generateParenthesis(n):
        # add open parenthesis if open < n 
        # add closed parenthesis if closed < open
        # valid if closed == open == n
        stack = []
        output = []
        def backtrack(openCount, closedCount):
            if openCount == closedCount == n:
                output.append("".join(stack))
                return
            
            if openCount < n:
                stack.append('(')
                backtrack(openCount+1, closedCount)
                stack.pop()
            if closedCount < openCount:
                stack.append(")")
                backtrack(openCount, closedCount+1)
                stack.pop()
        backtrack(0,0)
        return output



