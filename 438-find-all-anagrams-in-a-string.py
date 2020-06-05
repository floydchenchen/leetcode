# 438. Find All Anagrams in a String

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# 典型的sliding window问题
def find_all_anagram_substring(txt, pattern):
	result = []
	if not txt or len(pattern) > len(txt):
		return result

	pattern_dic = dict()
	for i in range(len(pattern)):
		pattern_dic[pattern[i]] = pattern_dic.get(pattern[i], 0) + 1
	dic = dict()

	for i in range(len(txt)):
		# deal with left boundary, add back to the dic
		if i >= len(pattern):
			if txt[i-len(pattern)] in dic:
				if dic[txt[i-len(pattern)]] == 1:
					dic.pop(txt[i-len(pattern)])
				else:
					dic[txt[i-len(pattern)]] -= 1

		# deal with new right boundary: if in dic, remove from dic
		dic[txt[i]] = dic.get(txt[i], 0) + 1
		# check if the dic matches pattern dic
		if dic == pattern_dic:
			result.append(txt[i-len(pattern)+1:i+1])

	return result
# print(find_all_anagram_substring("AAABABAA", "AABA"))


# counter solution
from collections import Counter
def findAnagrams(s, p):
	"""
	:type s: str
	:type p: str
	:rtype: List[int]
	"""
	result = []
	p_dic = Counter(p)
	s_dic = Counter(s[:len(p)-1])
	for i in range(len(p)-1,len(s)):
		s_dic[s[i]] += 1   # include a new char in the window
		if s_dic == p_dic:    # This step is O(1), since there are at most 26 English letters
			result.append(i-len(p)+1)   # append the starting index
		s_dic[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
		if s_dic[s[i-len(p)+1]] == 0:
			del s_dic[s[i-len(p)+1]]   # remove the count if it is 0
	return result

print(findAnagrams("AAABABAA", "AABA"))
