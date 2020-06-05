# 93. Restore IP Addresses

# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# Example:
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(s, index, path, result):
            # exit
            if index == 4:
                if not s:
                    # path[:-1] do not include the final "."
                    result.append(path[:-1])
                return
            for i in range(1, 4):
                # the digits we choose should no more than the length of s
                # choose one digit:
                if i <= len(s):
                    # choose one digit
                    # or choose two digits, the first one should not be "0"
                    # choose three digits, the first one should not be "0", and should less than 256
                    if (i == 1) or (i == 2 and s[0] != "0") or (s[0] != "0" and int(s[:3]) < 256):
                        # print("s[i:]",s[i:])
                        # print(index)
                        # print()
                        dfs(s[i:], index + 1, path + s[:i] + ".", result)

        result = []
        dfs(s, 0, "", result)
        return result

sol = Solution()
print(sol.restoreIpAddresses("1111"))