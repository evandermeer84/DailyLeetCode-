class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        '''
        if k < 1:
            return 0 
        if len(costs) <= 2*candidates:
            costs.sort()
            return sum(costs[0:k])
        modlist = costs[0:candidates+1] + costs[-(candidates+1):len(costs)]
        temp = min(modlist)
        ind = modlist.index(temp)
        if ind < candidates:
            costs.pop(ind)
        else:
            costs.pop(len(costs)-candidates+(ind%candidates))
        ans = temp + self.totalCost(costs, k-1, candidates)
        print(ans)
        return ans
        '''
        i = 0
        j = len(costs) - 1
        pq1 = []
        pq2 = []

        ans = 0
        while k > 0:
            while len(pq1) < candidates and i <= j:
                heapq.heappush(pq1, costs[i])
                i += 1
            while len(pq2) < candidates and i <= j:
                heapq.heappush(pq2, costs[j])
                j -= 1

            t1 = pq1[0] if pq1 else float('inf')
            t2 = pq2[0] if pq2 else float('inf')

            if t1 <= t2:
                ans += t1
                heapq.heappop(pq1)
            else:
                ans += t2
                heapq.heappop(pq2)

            k -= 1
        return ans
            
