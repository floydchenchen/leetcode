# 320. Generalized Abbreviation

# Write a function to generate the generalized abbreviations of a word.
#
# Note: The order of the output does not matter.
#
# Example:
#
# Input: "word"
# Output:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

# 思路：for every character, we can keep it or abbreviate it
# To keep it, we add it to the current solution and carry on backtracking.
# To abbreviate it, we omit it in the current solution, but increment the count,
# which indicates how many characters have we abbreviated

class Solution:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def backtrack(word, cur, result, pos, count):
            if pos == len(word):
                result.append(cur + str(count) if count else cur)
            else:
                # Skip current position, and increment count => use abbreviation
                backtrack(word, cur, result, pos + 1, count + 1)
                # Include current position, and zero-out count => don't use abbr
                backtrack(word, cur + (str(count) if count else "") + word[pos], result, pos + 1, 0)
        result = []
        backtrack(word, "", result, 0, 0)
        return result
