# 904. Fruit Into Baskets
# In a row of trees, the i-th tree produces fruit with type tree[i].
#
# You start at any tree of your choice, then repeatedly perform the following steps:
#
# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1,
# then step 2, then back to step 1, then step 2, and so on until you stop.
#
# You have two baskets, and each basket can carry any quantity of fruit,
# but you want each basket to only carry one type of fruit each.
#
# What is the total amount of fruit you can collect with this procedure?

# Example 1:
#
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
# Example 2:
#
# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
# Example 3:
#
# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
# Example 4:
#
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.

# 这个问题能被简化为找一个array里最长的最多包含两个不同元素的subarray
# sliding window

# This question can be reduced to find the "longest subarray with at most two distinct numbers"
# use l and r to represent the left and right boundary of the current window.
# use a dictionary/map to store the count of different type of fruits
# when len(dic) == 2 and tree[r] not in dic, we need to move the left boundary until the len(dic) < 2.
# remember when dic[key] == 0, remove the entry from the dictionary.

class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        # 用dictionary存当前window里的不同元素的数量，如果len(dic) > 2，移动left boundary直到len(dic) == 2
        l, r = 0, 0
        dic = {}
        max_len = 0
        while r < len(tree):
            if len(dic) == 2 and tree[r] not in dic:
                while len(dic) > 1:
                    if dic[tree[l]] == 1:
                        dic.pop(tree[l])
                    else:
                        dic[tree[l]] -= 1
                    l += 1
                dic[tree[r]] = 1
            else:
                dic[tree[r]] = dic.get(tree[r], 0) + 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
sol = Solution()
print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))