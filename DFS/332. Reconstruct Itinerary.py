# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

# Note:

# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.

# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.

# JFK-SFO-ATL - JFK - ATL - SFO
#             - SFO - xxx

# JFK-ATL-JFK - SFO - ATL - SFO
#        -SFO - ATL - JFK - SFO

# JFK: [SFO]
# SFO: [ATL]
# ATL: [SFO]

# JFK - ATL - JFK - SFO - ATL - SFO


# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

# JFK: [MUC]
# MUC: [LHR]
# LHR: [SFO]
# SFO: [SJC]

import collections


class Solution:
    def build_itinerary(self, arr):
        if not arr or not arr[0]:
            return []
        data = collections.defaultdict(list)
        res = ["JFK"]
        for orig, dest in arr:
            data[orig].append(dest)

        self.dfs(data, res)
        return res

    def dfs(self, data, res):
        key = res[-1]
        if not data:
            return True
        if key not in data:
            return False
        n = len(data[key])
        data[key].sort()
        dests = data[key]
        for i in range(n):
            cur_val = dests[i]
            res.append(cur_val)
            dests.remove(cur_val)
            if not data[key]:
                del data[key]
            if self.dfs(data, res):
                return True
            res.pop()
            data[key].insert(i, cur_val)
        return False


sol = Solution()
arr1 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
arr2 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(sol.build_itinerary(arr2))

# iterative #stack
import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        flights = collections.defaultdict(list)
        for ticket in tickets:
            dep = ticket[0]
            arv = ticket[1]
            flights[dep].append(arv)
        for arv_list in flights.values():
            arv_list.sort(reverse=True)

        stack = ['JFK']
        res = []

        while stack:
            while flights[stack[-1]]:
                stack.append(flights[stack[-1]].pop())
            res.append(stack.pop())

        return res[::-1]


# JFK: [SFO, PHX, ATL]
# SFO: [ATL]
# ATL: [SFO, ]

stack = [JFK, ATL, JFK, SFO, ATL, SFO
         res = [ATL,