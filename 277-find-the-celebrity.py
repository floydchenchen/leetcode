# 277. Find the Celebrity

# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity.
# The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
#
# Now you want to find out who the celebrity is or verify that there is not one.
# The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?"
# to get information of whether A knows B. You need to find out the celebrity (or verify there is not one)
# by asking as few questions as possible (in the asymptotic sense).
#
# You are given a helper function bool knows(a, b) which tells you whether A knows B.
# Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.
#
# Note: There will be exactly one celebrity if he/she is in the party.
# Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    pass

# 名人不认识其他人，其他人都认识名人
# 想象一个directed graph，名人就是这个graph的sink（所有其他node的终点）
# 思路：因为所有人都有一个共同的指向的sink，所以把所有人loop一遍，一定会找到那个名人（sink）
class Solution:
    def findCelebrity(self, n):
        candidate = 0
        # loop一遍找名人
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        # 判断名人是否真的存在
        for i in range(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        return candidate

