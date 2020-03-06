import time
from typing import List
from collections import defaultdict


class UnionFindSet:
    def __init__(self):
        self.parents = defaultdict()

    def find(self, x) -> int:
        """Return node(id=x)'s root node id."""
        self.parents.setdefault(x, x)   # set as default if x not exists
        if x != self.parents[x]:
            # [compress path] by directly assign every node's parent as root node
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        """Union x's set and y's set by assigning x's root's parent to y's root."""
        self.parents[self.find(x)] = self.find(y)
    

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        unionFindSet = UnionFindSet()
        email2name = defaultdict(str)

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                email2name[email] = name
                unionFindSet.union(email, emails[0])
        
        root2emails = defaultdict(list)
        for email in email2name.keys():
            setRootEmail = unionFindSet.find(email)
            root2emails[setRootEmail].append(email)

        return [[email2name[rootEmail]] + sorted(root2emails[rootEmail]) for rootEmail in root2emails.keys()]

        
if __name__ == "__main__":
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    # Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]

    # accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]

    tic = time.time()
    ret = Solution().accountsMerge(accounts)
    toc = time.time()

    print(f"Found :\n{ret}\nin {toc-tic:.3f}s.")
