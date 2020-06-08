# 1152. Analyze User Website Visit Pattern

# We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

# A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  
# (The websites in a 3-sequence are not necessarily distinct.)

# Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

 

# Example 1:

# Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], 
# website = ["home","about","career","home","cart","maps","home","home","about","career"]
# 
# Output: ["home","about","career"]
# Explanation: 
# The tuples in this example are:
# ["joe", 1, "home"]
# ["joe", 2, "about"]
# ["joe", 3, "career"]
# ["james", 4, "home"]
# ["james", 5, "cart"]
# ["james", 6, "maps"]
# ["james", 7, "home"]
# ["mary", 8, "home"]
# ["mary", 9, "about"]
# ["mary", 10, "career"]
# The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
# The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
# The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
# The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
# The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.

from typing import List
from collections import defaultdict, Counter
from itertools import combinations
class Solution:


    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        def combination(websites: List[str], result: List[tuple], temp: List[str], start: int):
            # exit 
            if len(temp) == 3:
                # skip duplicate
                if tuple(temp) not in result:
                    result.append(tuple(temp))
            else:
                for i in range(start, len(websites)):
                    # skip duplicates
                    # if 
                    temp.append(websites[i])
                    combination(websites, result, temp, i + 1)
                    temp.pop()

        user_websites = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            user_websites[u].append(w)
        print("user_websites", user_websites)
        patterns_map = defaultdict(int)
        for websites in user_websites.values():
            print("websites", websites)
            patterns = []
            combination(websites, patterns, [], 0)
            print("patterns", patterns)
            for pattern in patterns:
                patterns_map[pattern] += 1
        print("patterns_map", patterns_map)
        return min(patterns_map, key= lambda k: (-patterns_map[k], k))

sol = Solution()
# username = ["u1","u1","u1","u2","u2","u2"]
# timestamp = [1,2,3,4,5,6]
# websites = ["a","b","c","a","b","a"]
# username = ["ed","kgckntxmqd","iunjfam","iunjfam","iunjfam","ed","kgckntxmqd","hmlnzerzg"]
# timestamp = [544382452,777341379,844327903,116460449,394864737,48322095,742628675,791673656]
# websites = ["lrlxnhyeyq","za","p","oedqw","qewze","xihrl","xsk","qewze"]
# username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
# timestamp = [1,2,3,4,5,6,7,8,9,10]
# websites = ["home","about","career","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]

username = ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]
timestamp = [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]
websites = ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]
print(sol.mostVisitedPattern(username, timestamp, websites))