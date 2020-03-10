import time
from collections import defaultdict

class Solution:
    def __init__(self):
        self.atomsCount = defaultdict(int)

    @staticmethod
    def parseDigits(digits: str, fallback = 1):
        if digits:
            return int(digits)
        else:
            return fallback
        
    def countOfAtoms(self, formula: str) -> str:
        self.recursiveCountOfAtoms(formula)
        retStr = ''
        atomNames = sorted(self.atomsCount.keys())
        for atomName in atomNames:
            atomCount = ''
            if self.atomsCount[atomName] > 1:
                atomCount = str(self.atomsCount[atomName])
            retStr += (atomName + atomCount)
        return retStr

    def recursiveCountOfAtoms(self, formula: str, multiply=1):
        # call recursive function to deal with inner formula
        leftParenthesisIndex = formula.find('(')
        rightParenthesisIndex = formula.rfind(')')
        innerFormulaEnding = rightParenthesisIndex
        if leftParenthesisIndex >=0 and rightParenthesisIndex < len(formula):
            digitStr = ''
            for i in range(rightParenthesisIndex + 1, len(formula)):
                if formula[i].isdigit():
                    digitStr += formula[i]
                else:
                    break
            innerFormulaEnding = rightParenthesisIndex + len(digitStr)
            innerMultiply = Solution.parseDigits(digitStr)
            self.recursiveCountOfAtoms(formula[leftParenthesisIndex+1:rightParenthesisIndex], innerMultiply * multiply)
        else:
            leftParenthesisIndex = 0
            rightParenthesisIndex = 0
        
        # deal with the formula left
        formulaLeft = formula[0:leftParenthesisIndex] + formula[innerFormulaEnding+1:]
        atomName, atomDigits = '', ''
        for char in formulaLeft:
            if char.isupper():
                # 1. save the complete one if it exists
                if atomName:
                    self.atomsCount[atomName] += Solution.parseDigits(atomDigits) * multiply   # accumulate
                # 2. start scan next one
                atomName = char
                atomDigits = ''
            elif char.islower():
                atomName += char
            elif char.isdigit():
                atomDigits += char
        if atomName:    # the last one hasn't been written to dict in the loop
            self.atomsCount[atomName] += Solution.parseDigits(atomDigits) * multiply

        
if __name__ == "__main__":
    testCases = [("H2O", "H2O"), ("Mg(OH)2", "H2MgO2"), ("K4(ON(SO3)2)2", "K4N2O14S4"), ("((HHe28Be26He)9)34", "Be7956H306He8874")]

    for i, testCase in enumerate(testCases):
        formula, ans = testCase
        tic = time.time()
        ret = Solution().countOfAtoms(formula)
        toc = time.time()
        print(f"{i}: {ret == ans}, {ret} in {toc-tic:.3f}s.")
