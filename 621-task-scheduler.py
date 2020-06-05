# 621. Task Scheduler

# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different
# letters represent different tasks.Tasks could be done without original order. Each task could be done
# in one interval. For each interval, CPU could finish one task or just be idle.
#
# However, there is a non-negative cooling interval n that means between two same tasks,
# there must be at least n intervals that CPU are doing different tasks or just be idle.
#
# You need to return the least number of intervals the CPU will take to finish all the given tasks.
#
# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # store the number of each char in an array in an increasing order
        least_to_most = [0] * 26
        for c in tasks:
            least_to_most[ord(c) - ord("A")] += 1

        # 因为最多26个task，所以这里的sorting是constant time
        least_to_most.sort()

        # we need to add one more for each task with the most occurrences
        # number_of_max_freq is the number of tasks with highest frequencies of occurrences
        # 假设i出现最多次，i的次数存在least_to_most[25]中，max_freq为出现次数同i一样的最多的元素数量，
        # number_of_max_freq < 25保证不出现index out of bound
        number_of_max_freq = 0
        while number_of_max_freq < 25 and least_to_most[25 - number_of_max_freq] == least_to_most[-1]:
            number_of_max_freq += 1

        # 前面有(least_to_most[25] - 1)组，每组(n+1)个，最后加上加在最后面的多出来的number_of_max_freq
        # 如果不同len(tasks)比较的话，比如["A","A","A","B","B","B"], n = 0的话，结果就是3 * 1 + 2 = 5, GG
        return max((least_to_most[-1] - 1) * (n + 1) + number_of_max_freq, len(tasks))
