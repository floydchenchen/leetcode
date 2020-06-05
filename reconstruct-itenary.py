# 332. Reconstruct Itinerary

# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
# reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
#
# Note:
#
# If there are multiple valid itineraries, you should return the itinerary that has
# the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:
#
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:
#
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.

from heapq import *


class Solution:
    def travel(self, airports, departure, path):
        while airports[departure]:
            self.travel(airports, heappop(airports[departure]), path)
        path.append(departure)
        return path

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        airports = {}
        # priority queue -> smallest lexical order
        for ticket in tickets:
            if ticket[0] not in airports:
                airports[ticket[0]] = [ticket[1]]
            else:
                heappush(airports[ticket[0]], ticket[1])

            if ticket[1] not in airports:
                airports[ticket[1]] = []

        return self.travel(airports, "JFK", [])[::-1]
