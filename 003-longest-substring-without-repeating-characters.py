# 3. Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

class Solution:
	# dictionary: (character, character_position)
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		# 维护一个sliding window，left boundary是left，right boundary是right
		# 用char_pos_dict记录每个char的最右的位置
		left, max_len, char_pos_dict = 0, 0, {}
		for right in range(len(s)):
			# <=: e.g. "aaab", we need equal sign to move the left pointer right
			# 如果 s[i] in char_pos_dic，说明遇到重复的字符了
			# 这时候看这个重复的字符的是否在window中（left <= char_pos_dict[s[i]]）
			# 如果这个重复的字符在Window中，更新window的left boundary
			if s[right] in char_pos_dict and left <= char_pos_dict[s[right]]:
				left = char_pos_dict[s[right]] + 1
			# 如果没有重复字符，说明window继续往右扩大，这时候更新max_len
			else:
				max_len = max(max_len, right - left + 1)
			# 最后更新当前字符的最新位置
			char_pos_dict[s[right]] = right
		return max_len

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))