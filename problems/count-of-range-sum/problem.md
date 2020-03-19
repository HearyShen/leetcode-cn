#### [327. 区间和的个数](https://leetcode-cn.com/problems/count-of-range-sum/)

难度困难63收藏分享切换为英文关注反馈

给定一个整数数组 `nums`，返回区间和在 `[lower, upper]` 之间的个数，包含 `lower` 和 `upper`。
区间和 `S(i, j)` 表示在 `nums` 中，位置从 `i` 到 `j` 的元素之和，包含 `i` 和 `j` (`i` ≤ `j`)。

**说明:**
最直观的算法复杂度是 *O*(*n*2) ，请在此基础上优化你的算法。

**示例:**

```
输入: nums = [-2,5,-1], lower = -2, upper = 2,
输出: 3 
解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
```

通过次数2,622

提交次数7,996

---

#### [327. Count of Range Sum](https://leetcode-cn.com/problems/count-of-range-sum/)

难度困难63收藏分享切换为中文关注反馈

Given an integer array `nums`, return the number of range sums that lie in `[lower, upper]` inclusive.
Range sum `S(i, j)` is defined as the sum of the elements in `nums` between indices `i` and `j` (`i` ≤ `j`), inclusive.

**Note:**
A naive algorithm of *O*(*n*2) is trivial. You MUST do better than that.

**Example:**

```
Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
```

通过次数2,622

提交次数7,996