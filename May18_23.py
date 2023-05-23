class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        num_list = [0 for k in range(n)]
        for edge in edges:
            num_list[edge[1]] += 1
        answer = []
        for i in range(n):
            if num_list[i] == 0:
                answer.append(i)
        return answer
