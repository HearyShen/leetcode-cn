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
    
    @staticmethod
    def scanSurfaceParentheses(formula: str) -> list:
        surfaceParenteses = []
        idxStack = []
        pStack = []
        for i, char in enumerate(formula):
            if char in {'(', ')'}:
                if pStack and pStack[-1] == '(' and char == ')':
                    indexLeft = idxStack.pop()
                    parenthesis = pStack.pop()
                    if len(pStack) == 0:    # if the surface layer
                        surfaceParenteses.append((indexLeft, i))    # left, right index
                else:
                    idxStack.append(i)
                    pStack.append(char)
        return surfaceParenteses
            
        
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
        sectionToRemove = []
        surfaceParenthesisIndexes = Solution.scanSurfaceParentheses(formula)
        for leftParenthesisIndex, rightParenthesisIndex in surfaceParenthesisIndexes:
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
                sectionToRemove.append((leftParenthesisIndex, innerFormulaEnding))
                self.recursiveCountOfAtoms(formula[leftParenthesisIndex+1:rightParenthesisIndex], innerMultiply * multiply)
        
        # deal with the formula left
        formulaLeft = ''
        lastEnding = 0
        for leftIndex, rightIndex in sectionToRemove:
            formulaLeft += formula[lastEnding:leftIndex]
            lastEnding = rightIndex + 1
        formulaLeft += formula[lastEnding:]

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
    testCases = [("H2O", "H2O"), ("Mg(OH)2", "H2MgO2"), ("K4(ON(SO3)2)2", "K4N2O14S4"), ("((HHe28Be26He)9)34", "Be7956H306He8874"), ("((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14", "B18900Be18984C4200H5446He1386Li33894N50106O22638")]

    for i, testCase in enumerate(testCases):
        formula, ans = testCase
        tic = time.time()
        ret = Solution().countOfAtoms(formula)
        toc = time.time()
        print(f"{i}: {ret == ans}, {ret} in {toc-tic:.3f}s.")
