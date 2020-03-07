#### [957. N 天后的牢房](https://leetcode-cn.com/problems/prison-cells-after-n-days/)

难度中等40收藏分享切换为英文关注反馈

8 间牢房排成一排，每间牢房不是有人住就是空着。

每天，无论牢房是被占用或空置，都会根据以下规则进行更改：

- 如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。
- 否则，它就会被空置。

（请注意，由于监狱中的牢房排成一行，所以行中的第一个和最后一个房间无法有两个相邻的房间。）

我们用以下方式描述监狱的当前状态：如果第 `i` 间牢房被占用，则 `cell[i]==1`，否则 `cell[i]==0`。

根据监狱的初始状态，在 `N` 天后返回监狱的状况（和上述 N 种变化）。

 



**示例 1：**

```
输入：cells = [0,1,0,1,1,0,0,1], N = 7
输出：[0,0,1,1,0,0,0,0]
解释：
下表概述了监狱每天的状况：
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
```

**示例 2：**

```
输入：cells = [1,0,0,1,0,0,1,0], N = 1000000000
输出：[0,0,1,1,1,1,1,0]
```

 

**提示：**

1. `cells.length == 8`
2. `cells[i]` 的值为 `0` 或 `1` 
3. `1 <= N <= 10^9`

通过次数5,665

提交次数16,888

---

#### [957. Prison Cells After N Days](https://leetcode-cn.com/problems/prison-cells-after-n-days/)

难度中等40收藏分享切换为中文关注反馈

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

- If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
- Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: `cells[i] == 1` if the `i`-th cell is occupied, else `cells[i] == 0`.

Given the initial state of the prison, return the state of the prison after `N` days (and `N` such changes described above.)

 

**Example 1:**

```
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
```

**Example 2:**

```
Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
```

 

**Note:**

1. `cells.length == 8`
2. `cells[i]` is in `{0, 1}`
3. `1 <= N <= 10^9`

通过次数5,665

提交次数16,888