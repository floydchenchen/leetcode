# 763. Partition Labels

# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, 
# and return a list of integers representing the size of these parts.

# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

from collections import defaultdict
class Solution:
    # sliding window
    def partitionLabels(self, S: str) -> List[int]:
        # a map to store a char's last occurring location
        pos = defaultdict(int)
        for i, char in enumerate(S):
            pos[char] = i
            
        partition = []
        l, r = 0, 0
        for i, char in enumerate(S):
            # update the right index
            r = max(r, pos[char])
            if i == r:
                partition.append(r - l + 1)
                l = r + 1
        return partition
                
            
            