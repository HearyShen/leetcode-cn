#### [面试题 02.08. 环路检测](https://leetcode-cn.com/problems/linked-list-cycle-lcci/)

难度中等10收藏分享切换为英文关注反馈

给定一个有环链表，实现一个算法返回环路的开头节点。
有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。



**示例 1：**

```
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
```





**示例 2：**

```
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。
```





**示例 3：**

```
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
```





**进阶：**
你是否可以不用额外空间解决此题？

通过次数1,856

提交次数3,632

---

#### [面试题 02.08. Linked List Cycle LCCI](https://leetcode-cn.com/problems/linked-list-cycle-lcci/)

难度中等10收藏分享切换为中文关注反馈

Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.

**Example 1:**

```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
```

**Example 2:**

```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
```

**Example 3:**

```
Input: head = [1], pos = -1
Output: no cycle
```

**Follow Up:**
Can you solve it without using additional space?

通过次数1,856

提交次数3,632