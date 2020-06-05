# 957. Prison Cells After N Days
# There are 8 prison cells in a row, and each cell is either occupied or vacant.

# Each day, whether the cell is occupied or vacant changes according to the following rules:

# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

# We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

# Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

# Example 1:

# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation: 
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

# Example 2:

# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]

class Solution:
    # & 1: The value of expression (x & 1) would be 1 only if x is odd, otherwise the value would be zero.
    # a good way to check if x is odd
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        # find patterns
        N = N % 14
        if not N: 
            N = 14
        while N > 0:
            for i in range(1, len(cells) - 1):
                # if cells[i - 1] and cells[i + 1] are both odd or even
                if cells[i - 1] & 1 == cells[i + 1] & 1:
                    # cells[i] = 11 (binary) or 10 (binary)
                    cells[i] = 3 if cells[i] & 1 else 2
            for i in range(len(cells)):
                cells[i] >>= 1
            N -= 1
        return cells         