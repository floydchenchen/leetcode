# 681. Next Closest Time
# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
# There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid.
# For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
# which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

class Solution:
    def nextClosestTime(self, time):

        result = []
        for i in range(24 * 60):
            # https://stackoverflow.com/questions/3377688/what-do-these-symbolic-strings-mean-02d-01d
            # %02d means "format the integer with 2 digits, left padding it with zeroes", so:
            # Format  Data   Result
            # %02d    1      01
            # %02d    11     11

            #  '%02d:%02d' % divmod(i, 60) the % is  part of the string formatting
            for t in ['%02d:%02d' % divmod(i, 60)]:
                # if set(t) is a subset of set(time)
                if set(t) <= set(time):
                    result.append((t <= time, t))

        return min(result)[1]

sol = Solution()
print(sol.nextClosestTime("19:34"))
