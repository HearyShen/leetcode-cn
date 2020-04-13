import time


class Solution:
    def solveEquation(self, equation: str) -> str:
        # TODO: 2020.4.11
        coef = 0
        rightNum = 0
        parseStack = []
        leftStr, rightStr = equation.strip().split('=')
        # parse left part
        for i in range(len(leftStr)):
            ch = leftStr[i]
            
            if (ch == '+' or ch == '-') and parseStack:
                num, hasX = self.parseItem(parseStack)
                parseStack.clear()
                if hasX:
                    coef += num
                else:
                    rightNum -= num

            parseStack.append(ch)
        if parseStack:
            num, hasX = self.parseItem(parseStack)
            parseStack.clear()
            if hasX:
                coef += num
            else:
                rightNum -= num
        # print(f"left parse: {coef}x={rightNum}")

        # parse right part
        for i in range(len(rightStr)):
            ch = rightStr[i]
            
            if (ch == '+' or ch == '-') and parseStack:
                num, hasX = self.parseItem(parseStack)
                parseStack.clear()
                if hasX:
                    coef -= num
                else:
                    rightNum += num

            parseStack.append(ch)
        if parseStack:
            num, hasX = self.parseItem(parseStack)
            parseStack.clear()
            if hasX:
                coef -= num
            else:
                rightNum += num
        # print(f"all parse: {coef}x={rightNum}")

        # solve
        if coef == 0 and rightNum != 0:
            return "No solution"
        elif coef == 0 and rightNum == 0:
            return "Infinite solutions"
        else:
            return f"x={int(rightNum/coef)}"
    

    def parseItem(self, parseStack):
        sign = -1 if parseStack[0] == '-' else 1
        hasX = True if parseStack[-1] == 'x' else False
        num = 0
        hasNum = False
        for ch in parseStack:
            if ch.isdigit():
                hasNum = True
                num = num * 10 + int(ch)
        # if 'x', num should be reset as 1; if '2x', initial num should be 0.
        num = 1 if hasX and not hasNum else num
        return sign * num, hasX



if __name__ == '__main__':
    testCases = [("x+5-3+x=6+x-2", "x=2"), ("x=x", "Infinite solutions"), ("2x=x", "x=0"), ("2x+3x-6x=x+2", "x=-1"),
                 ("x=x+2", "No solution"), ("0x=0", "Infinite solutions")]
    for i, testCase in enumerate(testCases):
        equation, ans = testCase
        tic = time.time()
        ret = Solution().solveEquation(equation)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")
