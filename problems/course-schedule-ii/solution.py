import time
from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """Topological sort: remove 0 in-degree node until empty."""
        if numCourses < 1:
            return []
        
        nextCourses = defaultdict(set)
        inDegrees = [0 for i in range(numCourses)]
        for prereq in prerequisites:
            post, pre = prereq
            nextCourses[pre].add(post)
            inDegrees[post] += 1

        coursePlan = []
        while len(coursePlan) < numCourses:
            # find a 0 in-degree course
            curCourse = -1
            for course, inDegree in enumerate(inDegrees):
                if inDegree == 0:
                    curCourse = course
                    inDegrees[curCourse] = -99999    # mark as planned
                    break
            if curCourse < 0:   # if can't find 0 in-degree course while plan is not finished
                return []
            
            coursePlan.append(curCourse)
            for nextCourse in nextCourses[curCourse]:
                inDegrees[nextCourse] -= 1
        return coursePlan

if __name__ == "__main__":
    testCases = [(2, [[1,0]], [0,1]), (4, [[1,0],[2,0],[3,1],[3,2]], [0,1,2,3]), (1, [], [0])]
    for i, testCase in enumerate(testCases):
        n, pairs, ans = testCase
        tic = time.time()
        ret = Solution().findOrder(n, pairs)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")