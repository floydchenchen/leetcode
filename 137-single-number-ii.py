# 137. Single Number II


# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,3,2]
# Output: 3
# Example 2:

# Input: [0,1,0,1,0,1,99]
# Output: 99

class Solution:
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		ones, twos = 0, 0
		# ˼·����x ^ 0s = x �� x ^ x = 0
        # ����state machine��˼�룬��һ��������3�ε�ʱ�򣬽������SO:   
        # SO: 00  ->  S1: 01  -> s2: 10  -> s3/s0: 00
        # 00->01->10,.m->00(0->1->2->3/0
        # ��ones��twos����ÿ�α仯��ʱ��ÿ��bit��state������ֱ�����һλ��ڶ�λ��
        # For 'ones', we can get 'ones = ones ^ A[i]; if (twos == 1) then ones = 0', that can be tansformed to 'ones = (ones ^ A[i]) & ~twos'.
        # Similarly, for 'twos', we can get 'twos = twos ^ A[i]; if (ones* == 1) then twos = 0' and 'twos = (twos ^ A[i]) & ~ones'
		for num in nums:
			ones = (ones ^ num) & ~twos
			twos = (twos ^ num) & ~ones
		return ones