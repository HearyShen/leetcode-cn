import time
from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # TODO: 2020.4.9
        """Solve with BFS"""
        if not rooms:
            return True

        roomCount = len(rooms)
        bfsQueue = deque()
        bfsQueue.append(0)
        unlocked = {0}
        while bfsQueue and len(unlocked) < roomCount:
            curRoom = bfsQueue.popleft()
            nextRooms = [room for room in rooms[curRoom] if room not in unlocked]
            bfsQueue.extend(nextRooms)
            unlocked.update(nextRooms)
        
        return True if len(unlocked) == roomCount else False
        

if __name__ == "__main__":
    testCases = [([[1],[2],[3],[]], True), ([[1,3],[3,0,1],[2],[0]], False)]
    for i, testCase in enumerate(testCases):
        rooms, ans = testCase
        tic = time.time()
        ret = Solution().canVisitAllRooms(rooms)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")