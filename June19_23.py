class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0
        current = 0
        for i in range(len(gain)):
            current += gain[i]
            if current > max:
                max = current
        return max
